# 📊 Evaluaciones de Desempeño

## 📝 Descripción

Esta aplicación web permite obtener datos de evaluaciones de desempeño desde una hoja de **Google Sheets**, calcular el resultado final del personal en base a un porcentaje de **0 a 100%** por mes, y enviar correos electrónicos masivos personalizados para que cada persona reciba sus resultados de manera directa. Esto les permite conocer su rendimiento y los aspectos en los que pueden mejorar para el próximo mes.

---

## 🎯 Objetivos

- **Recopilación de Datos** 📄: Conectar con Google Sheets para obtener las evaluaciones mensuales del personal.
- **Transformación y Cálculo** 📊: Procesar y transformar los datos para calcular un puntaje final de 0 a 100%.
- **Envío de Correos Electrónicos Masivos** 📧: Enviar automáticamente un correo electrónico personalizado a cada persona evaluada, indicando sus resultados y áreas de mejora.
  
## 🛠️ Tecnologías Utilizadas

- **Streamlit** 🌐: Framework para crear la aplicación web interactiva.
- **Python** 🐍: Lenguaje de programación principal.
- **Pandas** 📋: Para la manipulación y análisis de datos.
- **Google Sheets API** 📊: Para acceder a los datos de evaluaciones.
- **smtplib** 📬: Librería para el envío de correos electrónicos.

## 📂 Estructura del Proyecto

- **app**: Contiene el archivo principal `app.py` para ejecutar la aplicación de Streamlit.
- **data**: Almacena cualquier archivo de datos necesario, incluyendo plantillas de correo.
- **config**: Archivo de configuración para las credenciales de Google y detalles de la cuenta de correo electrónico.

## 🎛️ Funcionalidades de la Aplicación
- **Cargar y visualizar los datos de evaluaciones**: Consulta el desempeño del personal basado en los datos de **Google Sheets**.
- **Calcular el puntaje mensual**: Procesa los datos de evaluación para obtener un porcentaje que refleja el rendimiento de cada empleado.
- **Enviar correos electrónicos**: Selecciona el mes deseado y envía automáticamente los resultados a los empleados, con un correo personalizado que incluye su puntaje y recomendaciones para mejorar.

## 📧 Envío de Correos
El correo electrónico se personaliza para cada empleado con el siguiente formato:

- **Asunto**: Evaluación de Desempeño - [Mes]
- **Contenido**: Incluye el puntaje de desempeño, las áreas fuertes y sugerencias de mejora.

## 🤝 Cómo Contribuir
1. Realiza un **fork** del proyecto 🍴.
2. Crea una nueva **rama** para tus cambios 🚧.
3. Haz **commit** de tus cambios y súbelos a tu rama 📝.
4. Abre un **pull request** para revisión y fusión 🔄.

### 📬 Contacto
- **Email**: [gustavoboadalugo@gmail.com](mailto:gustavoboadalugo@gmail.com)
- **LinkedIn**: [Gustavo Boada Lugo](https://www.linkedin.com/in/gboada23/)

