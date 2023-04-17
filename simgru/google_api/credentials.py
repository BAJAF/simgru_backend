from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

client_secret = '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'
client_id = '141259875889-t9avph5m9dq5l3eni2sv1cpf8hjccjos.apps.googleusercontent.com'
token = "ya29.a0Ael9sCPiioGhe_QaylnBx-sc_tJje0AWE43UdkqODsijHj43FTAzqLcVfG7auPRPsgzbWmyheqvMqtSsnjraVM2ZM_3MJtt8OKYanhxvd2m-UzOEFQWG08wPVL4PmO2TVlf2AqGfV39FayfxvpDcgGRXscgOCwaCgYKAesSARISFQF4udJhYQ_cusFBJxWa7ExdQSA3hg0165"
rToken = "APJWN8cHshvW9OJa6BtO4zK3dG7LS8gUwmsuZ0LookPAxNQGe0GTU2Q0j5u89xBIqHdi8dABCfEHhYtAeLXABKPNPUtTndROHieoK9pAH1E1eqpOykxRTvLHHQkiZB9CIfpisOfJqa9yiwmCGiBv2ThZwsjgr_RbBOWQ2yBiEMLK4QZfVgiiE05R-c7BU2lR2nVNwNXfc23BUDfQcHQoJdGmDUfoaskyaDXqH63tc49RZBHcWydbobZ8-1BPprwmVVdaEPiXPoqUF9DtPKLYJRzxf_dPg-fJ21Aqzt0eaG7mabCmEezQe-dX8bFoApMOC6jmX5aSfvj0BuxNCjmhUsqQEhgIfLIj46AyrIZTo1d6XnaiBYRPVeIr3m7RjTbKMFWkqricLsIdXhdfdKTTHpWvJkKJJaKBzAWVQ1dVKeh3LE5ZgtJZIVs"

def get_user_credentials():
    info = {
        "client_id": client_id,
        "client_secret": client_secret,
        "token": token,
        "token_uri": "https://oauth2.googleapis.com/token",
        "scopes": ["https://www.googleapis.com/auth/classroom.courses.readonly"]
    }

    cred = Credentials.from_authorized_user_info(info)

    if cred and cred.valid:
        print("\nCliente valido:", cred.valid)
        print("\nToken de cred", cred.token)
        print("\nSecreto de cliente", cred.client_secret)

    try:

        service = build('classroom', 'v1', credentials=cred)

        # Call the Classroom API
        results = service.courses().list().execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # Prints the names of the first 10 courses.
        print('Courses:')
        for course in courses:
            print(course['name'])

    except HttpError as error:
        print('An error occurred: %s' % error)

    return cred

if __name__ == "__main__":
    get_user_credentials()

    