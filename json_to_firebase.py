import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# --- CONFIGURACIÓN ---
# Reemplaza con la ruta a tu archivo de clave de cuenta de servicio
SERVICE_ACCOUNT_KEY_PATH = "firebase-service-account.json"

# Reemplaza con la ruta a tu archivo JSON
JSON_FILE_PATH = "english_profile.words.json"

# Nombre de la colección en Firestore donde quieres importar los datos
# Puedes cambiarlo si lo deseas
COLLECTION_NAME = "words"

# Tamaño del lote para escrituras (Firestore tiene un límite de 500 operaciones por lote)
BATCH_SIZE = 499
# --- FIN DE LA CONFIGURACIÓN ---

def initialize_firebase():
    """Inicializa la aplicación Firebase Admin."""
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK inicializado correctamente.")
        return firestore.client()
    except Exception as e:
        print(f"Error al inicializar Firebase Admin SDK: {e}")
        print("Asegúrate de que la ruta a SERVICE_ACCOUNT_KEY_PATH sea correcta y el archivo sea válido.")
        return None

def load_json_data(file_path):
    """Carga los datos desde un archivo JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Datos cargados correctamente desde {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: Archivo JSON no encontrado en {file_path}")
    except json.JSONDecodeError:
        print(f"Error: El archivo {file_path} no contiene JSON válido.")
    except Exception as e:
        print(f"Error inesperado al cargar el archivo JSON: {e}")
    return None

def import_data_to_firestore(db, data_to_import, collection_name):
    """Importa datos a una colección de Firestore usando lotes."""
    if not isinstance(data_to_import, list):
        print("Error: Los datos a importar deben ser una lista de objetos (diccionarios).")
        return

    if not data_to_import:
        print("No hay datos para importar.")
        return

    collection_ref = db.collection(collection_name)
    batch = db.batch()
    imported_count = 0
    batch_item_count = 0

    print(f"Iniciando importación de {len(data_to_import)} documentos a la colección '{collection_name}'...")

    for i, item in enumerate(data_to_import):
        if not isinstance(item, dict):
            print(f"Advertencia: El ítem {i} no es un diccionario y será omitido: {item}")
            continue

        # Crea una referencia a un nuevo documento con un ID generado automáticamente
        # Si tienes un campo 'id' en tus datos JSON que quieres usar como ID del documento:
        # doc_id = str(item.pop('id')) # Extrae y elimina 'id' del item, asegúrate que sea string
        # doc_ref = collection_ref.document(doc_id)
        # Si no, Firestore generará un ID automáticamente:
        doc_ref = collection_ref.document()

        batch.set(doc_ref, item)
        batch_item_count += 1

        if batch_item_count >= BATCH_SIZE:
            try:
                batch.commit()
                imported_count += batch_item_count
                print(f"Lote de {batch_item_count} documentos confirmado. Total importados: {imported_count}")
                batch = db.batch() # Inicia un nuevo lote
                batch_item_count = 0
            except Exception as e:
                print(f"Error al confirmar el lote: {e}")
                # Podrías agregar lógica aquí para reintentar o guardar los ítems fallidos

    # Confirma cualquier ítem restante en el último lote
    if batch_item_count > 0:
        try:
            batch.commit()
            imported_count += batch_item_count
            print(f"Lote final de {batch_item_count} documentos confirmado. Total importados: {imported_count}")
        except Exception as e:
            print(f"Error al confirmar el lote final: {e}")

    print(f"Importación completada. Total de documentos importados: {imported_count} de {len(data_to_import)}.")

def main():
    """Función principal para ejecutar el script de importación."""
    db = initialize_firebase()
    if not db:
        return

    data_to_import = load_json_data(JSON_FILE_PATH)
    if not data_to_import:
        return

    import_data_to_firestore(db, data_to_import, COLLECTION_NAME)

if __name__ == "__main__":
    main()