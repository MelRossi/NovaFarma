-- =====================================================================
-- NovaFarma Category Demand Analytics — Analysis Queries
-- Asume las tablas FactSales(Date, CategoryCode, UnitsSold)
-- y DimCategory(CategoryCode, TherapeuticGroup, CategoryGroup)
-- =====================================================================

-- 1) Ranking de categorías por volumen total
SELECT
    c.CategoryCode,
    c.CategoryGroup,
    SUM(f.UnitsSold) AS TotalUnits,
    ROUND(100.0 * SUM(f.UnitsSold) / SUM(SUM(f.UnitsSold)) OVER (), 2) AS ContributionPct
FROM FactSales f
JOIN DimCategory c ON f.CategoryCode = c.CategoryCode
GROUP BY c.CategoryCode, c.CategoryGroup
ORDER BY TotalUnits DESC;

-- 2) Evolución anual de unidades vendidas por categoría
SELECT
    EXTRACT(YEAR FROM f.Date) AS SalesYear,
    f.CategoryCode,
    SUM(f.UnitsSold) AS TotalUnits
FROM FactSales f
GROUP BY EXTRACT(YEAR FROM f.Date), f.CategoryCode
ORDER BY SalesYear, f.CategoryCode;

-- 3) Crecimiento interanual (YoY %) por categoría, usando LAG
WITH yearly AS (
    SELECT
        EXTRACT(YEAR FROM f.Date) AS SalesYear,
        f.CategoryCode,
        SUM(f.UnitsSold) AS TotalUnits
    FROM FactSales f
    GROUP BY EXTRACT(YEAR FROM f.Date), f.CategoryCode
)
SELECT
    SalesYear,
    CategoryCode,
    TotalUnits,
    LAG(TotalUnits) OVER (PARTITION BY CategoryCode ORDER BY SalesYear) AS PrevYearUnits,
    ROUND(
        100.0 * (TotalUnits - LAG(TotalUnits) OVER (PARTITION BY CategoryCode ORDER BY SalesYear))
        / NULLIF(LAG(TotalUnits) OVER (PARTITION BY CategoryCode ORDER BY SalesYear), 0), 1
    ) AS YoY_Pct
FROM yearly
ORDER BY CategoryCode, SalesYear;

-- 4) Estacionalidad mensual (promedio de unidades por mes, todas las categorías)
SELECT
    EXTRACT(MONTH FROM f.Date) AS MonthNumber,
    SUM(f.UnitsSold) AS TotalUnits
FROM FactSales f
GROUP BY EXTRACT(MONTH FROM f.Date)
ORDER BY MonthNumber;

-- 5) Patrón por día de la semana
SELECT
    TO_CHAR(f.Date, 'Day') AS WeekdayName,
    SUM(f.UnitsSold) AS TotalUnits
FROM FactSales f
GROUP BY TO_CHAR(f.Date, 'Day')
ORDER BY TotalUnits DESC;

-- 6) Volatilidad relativa por categoría (coeficiente de variación)
SELECT
    CategoryCode,
    AVG(UnitsSold) AS AvgUnits,
    STDDEV(UnitsSold) AS StdDevUnits,
    ROUND(100.0 * STDDEV(UnitsSold) / NULLIF(AVG(UnitsSold), 0), 1) AS CV_Pct
FROM FactSales
GROUP BY CategoryCode
ORDER BY CV_Pct DESC;


