🎬 CineDex – Tu gestor personal de películas

Proyecto desarrollado por Edward Terrero – Estudiante de Ingeniería de Datos
💻 Python • Streamlit • TMDB API • pandas • Plotly

📌 Descripción

CineDex es una aplicación modular desarrollada en Python que permite consultar, guardar y analizar películas usando la API de TMDB, todo desde una interfaz visual creada con Streamlit.

Desde esta app puedes:

🔍 Buscar películas por nombre

🧾 Consultar detalles como géneros, países, votaciones y recaudación

💾 Guardarlas en un CSV con control de auditoría

📊 Generar visualizaciones con Plotly a partir de tus películas favoritas

🧠 Tecnologías utilizadas
Tecnología	Uso principal
Python	Lenguaje base
Streamlit	Interfaz web
Plotly	Gráficos interactivos
pandas	Análisis de datos
requests	Consumo de API
TMDB API	Fuente de datos de películas
🗂️ Estructura del Proyecto
CINE_DB/
│
├── app.py                   # Archivo principal de Streamlit
├── main2.py                 # Archivo alternativo de ejecución
├── mian.py                  # (error tipográfico, debe ser main y fue usado para probar la funciones de business contex)
│
├── .gitignore               # Ignora carpetas/envs locales
│
├── auditoria/               # Registro de eventos del sistema
│   ├── logs_auditoria.py
│
├── config/                  # Variables globales y claves
│   └── my_globals.py
│
├── core/                    # Lógica principal del proyecto
│   ├── api_handler.py       # Conexión y procesamiento de TMDB
│   ├── get_genre.py         # Mapeo de ID de géneros
│   ├── registrar_peliculas.py  # Guarda los datos en CSV
│   └── analisis.py          # Cálculos y visualizaciones
│
├── data/                    # Datos persistentes del usuario
│   ├── peliculas.csv        # Películas guardadas
│   ├── logs.csv             # Eventos y auditoría
│   └── logo.png             # Logo de la aplicación
│
├── logic/                   # Lógica de negocio
│   └── bussiness_context.py
│
├── helper/                  # Funciones de limpieza y soporte
│   └── limpieza.py
│
└── env/                     # Entorno virtual (excluido del control de versiones)

🚀 Cómo ejecutar el proyecto

Clona el repositorio:

git clone https://github.com/tuusuario/cinedex.git
cd cinedex


Crea un entorno virtual:

python -m venv env


Activa el entorno virtual:

En Windows:

.\env\Scripts\activate


En macOS/Linux:

source env/bin/activate


Instala las dependencias:

pip install -r requirements.txt


Ejecuta la aplicación:

streamlit run app.py

🎨 Visualizaciones Incluidas

🌍 Promedio de votaciones por país

🎭 Distribución de géneros

⏱️ Duración promedio de películas por género

💰 Recaudación acumulada

🧪 Próximos pasos

 Agregar búsqueda avanzada por año o país

 Integrar base de datos relacional (SQLite o PostgreSQL)

 Modo usuario para guardar historial personalizado

 Exportar gráficas como imagen o PDF

📣 Créditos

API de películas proporcionada por TMDB

Desarrollo por Edward Terrero, enfocado en aprendizaje práctico de ingeniería de datos y visualización con Python

Conecta en LinkedIn:  https://www.linkedin.com/in/edward-terrero-acevedo-bb1a99170/
