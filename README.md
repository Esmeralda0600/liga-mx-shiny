Modularización de app.py
Para evitar la saturación del archivo principal app.py, mejorar el mantenimiento del código y aplicar buenas prácticas de desarrollo, se separaron las responsabilidades de la interfaz de usuario (ui) y del servidor en módulos independientes dentro de la carpeta components/.

1. Módulo de Interfaz: components/paneles.py
Este archivo contiene exclusivamente la estructura visual y los elementos de entrada de la aplicación. Se divide en funciones independientes por cada panel.

2. Módulo de Lógica: components/server.py
Contiene todas las funciones de backend que manejan la reactividad de los componentes, filtran dataframes y renderizan los gráficos interactivos de Plotly.

3. Por lo que ahora app.py cuenta con modularización, asi el archivo principal se redujo y estructuro de mejor manera. Su única función actual es importar los componentes y ensamblarlos en la estructura global.