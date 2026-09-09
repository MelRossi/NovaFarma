# NovaFarma — Category Demand Analytics

Proyecto de Business Intelligence que analiza 6 años de demanda de una farmacia minorista por categoría terapéutica, con el objetivo de mejorar la planificación de compras e inventario a partir de estacionalidad, tendencias y volatilidad de la demanda.


## Business Problem

NovaFarma no tiene visibilidad centralizada de cómo varía la demanda de cada categoría terapéutica a lo largo del tiempo. Esto genera quiebres de stock en picos estacionales (ej. antigripales en invierno) y sobre-stock en categorías de baja rotación, afectando capital de trabajo y disponibilidad de producto.

**Objetivo:** entender evolución, estacionalidad y volatilidad de la demanda por categoría para optimizar decisiones de reposición e inventario.

**Stakeholders:** gerencia de farmacia, equipo de compras, dirección comercial.


## Dataset

**Pharma Sales Data** — Milan Zdravković, vía Kaggle: [kaggle.com/datasets/milanzdravkovic/pharma-sales-data](https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data) (CC BY-NC 4.0). Ventas diarias de una farmacia entre 2014 y 2019, clasificadas en 8 categorías del sistema ATC (Anatomical Therapeutic Chemical).

> **Decisión de scope:** el dataset no incluye ID de cliente, producto individual, precio ni costo. Por eso el proyecto se enfoca en **análisis de demanda y estacionalidad por categoría** en lugar de análisis de clientes o rentabilidad monetaria.


## Herramientas

Power BI (Power Query + DAX) · Python (pandas) para EDA y generación del modelo estrella · SQL para consultas analíticas equivalentes.


## Metodología

1. **Exploración y auditoría de calidad de datos** — 0 nulos, 0 duplicados, pero se detectó un campo `Hour` inválido en el archivo diario (residuo del dataset horario original), eliminado en Power Query.
2. **Transformación en Power Query**, incluyendo un **unpivot** de las 8 columnas de categoría (formato ancho → largo) para construir una tabla de hechos real.
3. **Modelo de datos en esquema estrella:** `FactSales` (16.848 filas) + `DimCategory` (8 filas) + `DimDate` (generada con DAX).
4. **14 medidas DAX** para KPIs, time intelligence, contribución, estacionalidad y volatilidad.
5. **Dashboard de 5 páginas** (portada + 4 páginas de análisis) con storytelling, tema de color personalizado e interactividad (slicers, drill-through, bookmarks).


### Nota técnica — validación de datos durante la construcción

Al importar los CSV a Power BI, un desajuste de configuración regional (locale) hizo que el separador decimal del dataset (punto) se interpretara como separador de miles, inflando los valores de venta entre 10x y 100x según la cantidad de decimales de cada número — un error silencioso que no rompía la carga, solo distorsionaba los totales. Se detectó comparando los totales de Power BI contra los calculados de forma independiente en Python, y se corrigió especificando explícitamente el locale (`English (United States)`) al tipar la columna en Power Query.


## Data Model

```
DimDate (1) ──< FactSales >── (1) DimCategory
```

- **FactSales:** `Date`, `CategoryCode`, `UnitsSold` — grano: unidades vendidas de una categoría en un día.
- **DimCategory:** `CategoryCode`, `TherapeuticGroup`, `CategoryGroup` (Pain & Inflammation / Mental Health / Respiratory).
- **DimDate:** tabla calendario generada con `CALENDAR()` en DAX, marcada como Date Table.


## Dashboard

| Página | Responde |
|---|---|
| **Portada** | Presentación del proyecto y navegación |
| **Executive Overview** | ¿Cómo está funcionando la demanda global y qué categorías la explican? |
| **Category & Trend Analysis** | ¿Cómo evoluciona cada categoría y cuáles crecen o caen? |
| **Seasonality & Inventory Risk** | ¿Cuándo anticipar compras y qué categorías son más impredecibles? |
| **Category Deep Dive** | Drill-through al detalle diario/mensual de una categoría puntual |


## Insights principales (calculados sobre datos reales)

- **N02BE (analgésicos tipo paracetamol) concentra el 49% del volumen total** vendido en 6 años — la categoría dominante, con el mayor impacto potencial ante un quiebre de stock.
- **Categorías respiratorias en fuerte expansión:** R03 +54% y R06 +22% entre 2015 y 2018.
- **N02BA en declive estructural:** -30% en el mismo período.
- **Enero y octubre son los meses de mayor demanda**; julio el más bajo — patrón estacional claro y aprovechable para planificación de compras.
- **N05C es la categoría más volátil** (coeficiente de variación ~184%), pese a representar solo ~1% del volumen — mayor riesgo relativo de quiebre o sobre-stock puntual.
