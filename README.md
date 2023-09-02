# CSV-Link-extractor
This python script will help you go through all of your csv files and extract all the links from it.
CSV Link Extractor
This Python script is designed to extract links from CSV files located in a specified Google Drive folder. The extracted links are then saved to a text file.

Prerequisites
Python installed on your machine.
Google Drive API enabled and credentials.json file obtained. You can follow the Python Quickstart | Google Drive API to set this up.
How to Use
Clone the repository:

`git clone https://github.com/Mr-Nobody1/CSV-Link-extractor.git`
`cd CSV-Link-extractor`

Install the required Python packages:

`pip install --upgrade google-auth-oauthlib google-auth-httplib2 google-api-python-client`

Place your credentials.json file in the root directory of the cloned repository.

Run the script:

`python drive_csv_processor.py`

The script will prompt you to enter the Google Drive folder link containing the CSV files. Paste the link and press Enter.

On the first run, you'll be asked to authorize the script to access your Google Drive. Follow the provided link, authorize the script, and paste the code back into the terminal.

The script will process each CSV file in the specified folder, extract links, and save them to a file named links.txt.

Once the extraction is complete, you'll see a message indicating that the links have been saved.

Functions Overview
`get_service()`: Authenticates and returns the Google Drive service.
`get_csv_files_from_folder(service, folder_id)`: Retrieves a list of CSV files from the specified Google Drive folder.
`download_csv_file(service, file_id)`: Downloads the content of a specified CSV file.
`extract_links_from_csv(csv_content)`: Extracts links from the provided CSV content.
`save_links_to_txt(links, filename="links.txt")`: Saves the extracted links to a text file.
