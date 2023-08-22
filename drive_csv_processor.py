import pickle
import os.path
import requests
import sys

import csv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def get_csv_files_from_folder(service, folder_id):
    query = f"'{folder_id}' in parents and mimeType='text/csv'"
    results = service.files().list(q=query).execute()
    return results.get('files', [])

def download_csv_file(service, file_id):
    request = service.files().get_media(fileId=file_id)
    response = request.execute()
    return response.decode('utf-8').splitlines()

def extract_links_from_csv(csv_content):
    links = []
    try:
        csv.field_size_limit(2**30)  # Set a large field size limit
        reader = csv.reader(csv_content)
        for row in reader:
            for cell in row:
                if cell.startswith(('http', 'https')):
                    links.append(cell)
    except (_csv.Error, OverflowError):  # Catch CSV errors and overflow errors
        print("Skipped a problematic CSV file.")
    return links

def get_csv_files_from_folder(service, folder_id):
    query = f"'{folder_id}' in parents and mimeType='text/csv'"
    results = service.files().list(q=query).execute()
    return results.get('files', [])



def save_links_to_txt(links, filename="links.txt"):
    with open(filename, 'a', encoding='utf-8') as f:
        for link in links:
            f.write(f"{link}\n")

if __name__ == "__main__":
    folder_link = input("Enter the Google Drive folder link: ")
    folder_id = folder_link.split('/')[-1]

    service = get_service()
    csv_files = get_csv_files_from_folder(service, folder_id)

    all_links = []
    for index, file in enumerate(csv_files):
        print(f"Processing file {index + 1}/{len(csv_files)}: {file['name']}...")
        csv_content = download_csv_file(service, file['id'])
        links = extract_links_from_csv(csv_content)
        all_links.extend(links)

    save_links_to_txt(all_links)
    print(f"Links saved to links.txt")
