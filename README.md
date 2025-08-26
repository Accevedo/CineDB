# 🎮 CineDex – Tu gestor personal de películas

Proyecto desarrollado por **Edward Terrero** – *Estudiante de Ingeniería de Datos*
💻 **Python** • **Streamlit** • **TMDB API** • **pandas** • **Plotly**

---

## 📌 Descripción

**CineDex** es una aplicación modular desarrollada en Python que permite consultar, guardar y analizar películas usando la API de TMDB, todo desde una interfaz visual creada con Streamlit.

Desde esta app puedes:

* 🔍 **Buscar películas** por nombre
* 🧾 **Consultar detalles** como géneros, países, votaciones y recaudación
* 📂 **Guardar resultados** en un CSV con control de auditoría
* 📊 **Generar visualizaciones** con Plotly a partir de tus películas favoritas

---

## 🧠 Tecnologías utilizadas

| Tecnología | Uso principal                |
| ---------- | ---------------------------- |
| Python     | Lenguaje base                |
| Streamlit  | Interfaz web                 |
| Plotly     | Gráficos interactivos        |
| pandas     | Análisis de datos            |
| requests   | Consumo de API               |
| TMDB API   | Fuente de datos de películas |

---

## 🗂️ Estructura del Proyecto

```
CINE_DB/
├── app.py                    # Archivo principal de Streamlit
├── main2.py                 # Archivo alternativo de ejecución
├── mian.py                  # (Error tipográfico de pruebas)
│
├── .gitignore               # Ignora carpetas/envs locales
│
├── auditoria/               # Registro de eventos del sistema
│   └── logs_auditoria.py
│
├── config/                  # Variables globales y claves
│   └── my_globals.py
│
├── core/                    # Lógica principal del proyecto
│   ├── api_handler.py
│   ├── get_genre.py
│   ├── registrar_peliculas.py
│   └── analisis.py
│
├── data/                    # Datos persistentes del usuario
│   ├── peliculas.csv
│   ├── logs.csv
│   └── logo.png
│
├── logic/                   # Lógica de negocio
│   └── bussiness_context.py
│
├── helper/                  # Funciones de soporte y limpieza
│   └── limpieza.py
│
└── env/                     # Entorno virtual (ignorado)
```

---

## 🚀 Cómo ejecutar el proyecto

1. **Clona el repositorio:**

```bash
git clone https://github.com/tuusuario/cinedex.git
cd cinedex
```

2. **Crea el entorno virtual:**

```bash
python -m venv env
```

3. **Activa el entorno virtual:**

* En Windows:

```bash
.\env\Scripts\activate
```

* En macOS/Linux:

```bash
source env/bin/activate
```

4. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

5. **Ejecuta la aplicación:**

```bash
streamlit run app.py
```

---

## 🎨 Visualizaciones Incluidas

* 🌍 **Promedio de votaciones por país**
* 🎭 **Distribución de géneros**
* ⏱️ **Duración promedio de películas por género**
* 💰 **Recaudación acumulada**

---

## 🧪 Próximos pasos

* [ ] Agregar búsqueda avanzada por año o país
* [ ] Integrar base de datos relacional (SQLite o PostgreSQL)
* [ ] Modo usuario para guardar historial personalizado
* [ ] Exportar gráficas como imagen o PDF

---

## 📣 Créditos

* API de películas proporcionada por [TMDB](https://www.themoviedb.org/)
* Desarrollo por **Edward Terrero**, enfocado en aprendizaje práctico de ingeniería de datos y visualización con Python
* Conecta en LinkedIn: [linkedin.com/in/edward-terrero-acevedo-bb1a99170](https://www.linkedin.com/in/edward-terrero-acevedo-bb1a99170)

---
