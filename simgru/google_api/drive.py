from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def upload_file(credentials, file_path, folder_id):
    drive_service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': file_path.split('/')[-1],
        'parents': [folder_id]
    }

    media_body = MediaFileUpload(file_path, resumable=True)

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media_body,
        fields='id'
    ).execute()

    print('File ID:', file.get('id'))


"""
Para poder llamar en otro archivo:
from drive import upload_file

Idea de como generar archivo y guardarlo

def generar_y_guardar_archivo(request):
    # Generar el archivo en la ruta deseada
    # ...
    Cosas de codigo para poder crear el archivo
    # ID de la carpeta de destino en Google Drive
    folder_id = 'FOLDER_ID'

    # Ruta completa del archivo generado
    file_path = '/ruta/completa/del/archivo'

    # Guardar el archivo en Google Drive
    upload_file(credentials, file_path, folder_id)

    return HttpResponse('Archivo guardado en Google Drive')


"""
