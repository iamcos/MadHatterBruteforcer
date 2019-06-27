import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1QbamdU8f6thW2lNdJuo6a_jc7SPKonS-wgH_tF3hAmc/").sheet1
values_list = sheet.row_values(1)
print(values_list)