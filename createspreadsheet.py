import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'connection/gs-credentials.json', scope)
client = gspread.authorize(credentials)
print(client)
sheet = client.create("Firstsheet")

sheet.share('sana.soibam2014@gmail.com', perm_type='user', role='owner')
