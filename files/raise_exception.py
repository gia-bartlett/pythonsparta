class Text_File_Except:

    def __init__(self, file_path, text_storage=None):  # no default created for file_path so we must provide one when calling this class

        self.file_path = file_path
        self.text_storage = text_storage

    def raise_exception(self):
        name = str(input("Enter your name: "))
        while (len(name)) == 0:
            try:
                name = str(input("Please enter a name!"))
                if (len(name)) == 0:
                    raise Exception
            except Exception:
                print("Sorry, we don't accept blank names")
            else:
                print(f"Thank you! {name}")
