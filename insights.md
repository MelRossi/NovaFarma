# Insights — calculados sobre datos reales (salesdaily.csv)

## Insight 1 — Concentración extrema en una sola categoría
**Finding:** N02BE (analgésicos tipo paracetamol) representa el 49,4% de todas las unidades vendidas en el período 2014-2019, más que las siete categorías restantes combinadas.
**Evidence:** contribución calculada sobre el total de unidades vendidas por categoría (N02BE: 63.005 de 128.000 unidades aprox.).
**Business Impact:** un quiebre de stock en esta única categoría tiene un impacto desproporcionado en la disponibilidad general de la farmacia, comparado con cualquier otra categoría individual.
**Recommendation:** definir para N02BE un nivel de stock de seguridad y una frecuencia de reposición diferenciada (más frecuente y con mayor buffer) respecto al resto del catálogo.

## Insight 2 — Categorías respiratorias en fuerte expansión
**Finding:** la categoría R03 (fármacos respiratorios) creció 54,3% entre 2015 y 2018, y R06 (antihistamínicos) 21,7% en el mismo período — el crecimiento más marcado del catálogo.
**Evidence:** comparación de unidades vendidas totales por año, 2015 vs. 2018.
**Business Impact:** el negocio muestra un giro estructural hacia mayor demanda de productos respiratorios, posiblemente asociado a cambios en el mix de pacientes atendidos.
**Recommendation:** aumentar la proporción de presupuesto de compra asignado a la categoría Respiratory y renegociar condiciones con proveedores de esa línea ante el mayor volumen proyectado.

## Insight 3 — Declive sostenido en analgésicos salicílicos
**Finding:** N02BA cayó 30,1% entre 2015 y 2018, la mayor caída de todo el catálogo.
**Evidence:** comparación interanual de unidades vendidas 2015 vs. 2018 y serie YoY 2016-2018 (con caída de -22,2% solo en 2017).
**Business Impact:** capital inmovilizado en stock de una categoría en declive estructural reduce la eficiencia de inventario.
**Recommendation:** reducir gradualmente el nivel de stock objetivo de N02BA y evaluar reasignar ese espacio/presupuesto hacia categorías en crecimiento (R03, N05C).

## Insight 4 — Estacionalidad marcada de enero y octubre
**Finding:** enero concentra el mayor volumen promedio de ventas del año (~13.971 unidades/mes en promedio), seguido de octubre (~12.051); julio es el mes más bajo (~8.759).
**Evidence:** promedio de unidades totales agrupado por número de mes, sobre todo el período.
**Business Impact:** un patrón estacional predecible que hoy no está siendo aprovechado sistemáticamente para planificar compras.
**Recommendation:** anticipar pedidos de reposición en diciembre (para el pico de enero) y en septiembre (para el pico de octubre), en particular para categorías respiratorias que se acentúan en esos meses.

## Insight 5 — Alta volatilidad en categorías de bajo volumen
**Finding:** N05C (hipnóticos/sedantes) tiene el coeficiente de variación más alto del catálogo (184%), muy por encima del resto (rango 52%-117%).
**Evidence:** coeficiente de variación (desvío estándar / media) calculado por categoría sobre la serie diaria.
**Business Impact:** aunque N05C es una categoría pequeña en volumen (~1% del total), su demanda es la más impredecible, lo que eleva el riesgo relativo de quiebre o sobre-stock puntual.
**Recommendation:** aplicar un modelo de reposición más frecuente y en lotes pequeños para N05C, en lugar de pedidos grandes espaciados, para absorber mejor su variabilidad.

## Insight 6 — Patrón semanal moderado, con fin de semana más fuerte
**Finding:** sábado (19.768 unidades promedio) y domingo (18.401) son los días de mayor demanda total; jueves es el más bajo (17.212) — una diferencia de ~13% entre el día más alto y el más bajo.
**Evidence:** promedio de unidades totales agrupado por día de la semana.
**Business Impact:** el patrón semanal es real pero moderado, por lo que no justifica cambios drásticos de dotación de stock por día, aunque sí resulta relevante para la planificación de reposición de fin de semana.
**Recommendation:** asegurar niveles de stock reforzados antes del fin de semana, especialmente para la categoría dominante N02BE.

---

## Recomendaciones de negocio consolidadas (5)

1. **Diferenciar la política de reposición por categoría según su peso relativo**, priorizando N02BE (49% del volumen) con mayor frecuencia y buffer de stock.
2. **Reasignar presupuesto de compra hacia la categoría Respiratory (R03, R06)**, dado su crecimiento sostenido (+54% y +22% respectivamente entre 2015-2018).
3. **Reducir gradualmente el stock objetivo de N02BA**, categoría en declive estructural (-30% en el mismo período), liberando capital de trabajo.
4. **Anticipar compras en diciembre y septiembre** para cubrir los picos estacionales de enero y octubre respectivamente, en particular en categorías respiratorias.
5. **Aplicar reposición en lotes pequeños y frecuentes para categorías de alta volatilidad relativa (N05C, R03)**, en lugar de pedidos grandes espaciados, para reducir el riesgo de quiebre o sobre-stock.
