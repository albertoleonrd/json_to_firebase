# JSON a Firebase

## Descripción

Esta herramienta permite importar datos desde archivos JSON a una base de datos Firestore de Firebase. Puede ser utilizada para importar cualquier tipo de datos estructurados en formato JSON a Firestore, facilitando la migración o carga masiva de información.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `json_to_firebase.py`: Script principal que maneja la importación de datos a Firebase.
- `example_data.json`: Archivo de ejemplo que contiene datos de muestra en formato JSON.
- `.gitignore`: Archivo para excluir archivos específicos del control de versiones.

## Requisitos

- Python 3.6 o superior
- Cuenta de Firebase con Firestore habilitado
- Archivo de credenciales de cuenta de servicio de Firebase

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias:

```bash
pip install firebase-admin
```

3. Coloca tu archivo de credenciales de cuenta de servicio de Firebase (`firebase-service-account.json`) en el directorio del proyecto.

## Configuración

Abre el archivo `json_to_firebase.py` y modifica las siguientes variables según sea necesario:

```python
# Reemplaza con la ruta a tu archivo de clave de cuenta de servicio
SERVICE_ACCOUNT_KEY_PATH = "firebase-service-account.json"

# Reemplaza con la ruta a tu archivo JSON
JSON_FILE_PATH = "example_data.json"

# Nombre de la colección en Firestore donde quieres importar los datos
COLLECTION_NAME = "words"

# Tamaño del lote para escrituras (Firestore tiene un límite de 500 operaciones por lote)
BATCH_SIZE = 499
```

## Uso

Ejecuta el script principal:

```bash
python json_to_firebase.py
```

El script realizará las siguientes acciones:

1. Inicializará la conexión con Firebase utilizando las credenciales proporcionadas.
2. Cargará los datos del archivo JSON especificado.
3. Importará los datos a la colección de Firestore especificada, utilizando lotes para optimizar el rendimiento.
4. Mostrará información sobre el progreso y los resultados de la importación.

## Estructura de Datos

El archivo `example_data.json` contiene un array de objetos con la siguiente estructura:

```json
[
  {
    "id": "001",
    "name": "Smartphone XYZ",
    "category": "Electronics",
    "price": 599.99,
    "specifications": {
      "brand": "TechCorp",
      "model": "XYZ-2000",
      "color": "Black",
      "storage": "128GB",
      "features": ["5G", "Water Resistant", "Dual Camera"]
    },
    "inStock": true,
    "reviews": [
      {
        "user": "user123",
        "rating": 4.5,
        "comment": "Great phone, excellent camera quality!"
      }
    ]
  }
]
```

## Notas Importantes

- El script está configurado para manejar grandes cantidades de datos utilizando lotes (batches) para evitar exceder los límites de Firestore.
- Por defecto, se generan IDs automáticos para cada documento en Firestore. Si deseas utilizar un campo específico de tus datos como ID, puedes modificar la función `import_data_to_firestore`.
- Asegúrate de tener los permisos adecuados en tu proyecto de Firebase para escribir en la base de datos.

## Licencia

Este proyecto está disponible como código abierto bajo los términos de la licencia MIT.