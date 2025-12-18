# Google Sheets accessor
import gspread
import json
# Atproto protocol for accessing Bluesky
from atproto import Client
# Google API authorization 
from google.oauth2.service_account import Credentials

# Define the scope
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate Google Sheets with credentials
# MUST HAVE A SERVICE_ACCOUNTS.JSON, KEEP THIS PRIVATE ON YOUR LOCAL DEVICE 
creds = Credentials.from_service_account_file("service_accounts.json", scopes=scopes)
gc = gspread.authorize(creds)

# Open the Google Sheet
sheet = gc.open('Nuclear_challenge_data').sheet1

# Bluesky Connection
# Load in credentials from credentials.json
with open("Communication_Subproblem/secrets/credentials.json", "r") as f: 
    creds = json.load(f)

username = creds["BLUESKY_USERNAME"]
password = creds["BLUESKY_PASSWORD"]

# Authorize Bluesky connection
client = Client()
client.login(username, password)

def get_latest_alert_data(sheet):
    # Fetch all records from the sheet as a list of dictionaries
    # This automatically uses row 1 as the keys for each dictionary
    records = sheet.get_all_records()
    
    if not records:
        return None

    time_format = "%m/%d/%Y %H:%M:%S"
    
    # Find the record with the maximum (latest) timestamp
    def parse_time(row):
        try:
            return datetime.strptime(str(row.get("Timestamp")), time_format)
        except (ValueError, TypeError):
            # Return a very old date for rows with missing/bad timestamps
            return datetime.min

    # Use the 'max' function with our custom key to find the latest row
    latest_row = max(records, key=parse_time)

    # Extract the required values
    alert_message = latest_row.get("Alert Message")
    lat_long = latest_row.get("Latitude & Longitude")
    actual_time = latest_row.get("Timestamp")

    return {
        "Timestamp": actual_time,
        "Alert Message": alert_message,
        "Location": lat_long
    }


sheetdata = get_latest_alert_data(sheet)
location = data['Timestamp']
alert_message = data["Alert Message"]
time = data["Timestamp"]

# Publish post
post = client.send_post('Major alert for ' + location + ": " + alert_message + '. ')
