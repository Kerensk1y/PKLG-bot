from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import ApiRequestError

def authenticate():
    # Perform authentication with Google Drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

def find_file_by_title(drive, file_title):
    # Find a file on Google Drive by title
    try:
        file_list = drive.ListFile({'q': f"title='{file_title}'"}).GetList()
        return file_list
    except ApiRequestError as e:
        print("An error occurred while searching for the file:", e)
        return []

def update_or_create_xlsx_file(drive, file_title, file_path):
    # Update or create an XLSX file on Google Drive
    file_list = find_file_by_title(drive, file_title)

    if len(file_list) == 1:
        # File exists, update it
        file = file_list[0]
        file.SetContentFile(file_path)
        file.Upload()
        print("File updated successfully.")
    elif len(file_list) == 0:
        # File does not exist, create it
        file = drive.CreateFile({'title': file_title})
        file.SetContentFile(file_path)
        file.Upload()
        print("File created successfully.")
    else:
        print("Multiple files found with the same title.")

def main():
    # Main function to run the program
    drive = authenticate()
    file_title = "test.xlsx"
    file_path = "test.xlsx"
    update_or_create_xlsx_file(drive, file_title, file_path)

if __name__ == "__main__":
    main()