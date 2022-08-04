import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BMvxIvhkfCiAEy686BykoWj0WOhojZYYhQoxJ5jhr4u2nywKnfGgQ87lo4RpRa8Cdn1KPposcW6FV_Boj3IkDqcBb5uZlwg52hV_p19pOHTT3IOWCHAYuyV0xM1ES7ueFYIal1I'
    transferData = TransferData(access_token)

    file_from = input("Enter the path")
    file_to = input("Enter the dropbox path")

    transferData.upload_file(file_from, file_to)
    print("File has been moved")
main()