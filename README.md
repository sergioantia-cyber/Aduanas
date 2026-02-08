# Dashboard de Aduanas (DrillDown)

Una herramienta de inteligencia de negocios para visualizar y analizar trámites aduaneros.

## Características

- 📊 **Visualización de Datos**: Gráficos interactivos de volumen por cliente.
- 📅 **Filtros Avanzados**: Filtrado por rango de fechas y buscador global.
- 📂 **Carga de Datos**: Soporte *Drag & Drop* para archivos Excel (.xlsx, .xls) y CSV.
- 📥 **Exportación**: Descarga de datos filtrados en formato CSV.
- ⚡ **Rápido y Ligero**: Funciona directamente en el navegador sin backend complejo.

## Uso

1. Abre `index.html` en tu navegador.
2. Arrastra tu archivo de datos de aduana.
3. Analiza los resultados.

## Formato de Datos Esperado

El sistema espera un archivo Excel/CSV con columnas similares a:
- CLIENTE / IMPORTADOR
- FECHA
- REFERENCIA
- CHOFER / CONDUCTOR
- ANTIDROGA / DROGA
- ADUANA

## Tecnologías

- HTML5 / JS
- TailwindCSS
- Chart.js
- SheetJS
