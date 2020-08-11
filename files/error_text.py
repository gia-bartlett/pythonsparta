class Text_File_Errors:

    def __init__(self, file_path, text_storage=None):  # no default created for file_path so we must provide one when calling this class

        self.file_path = file_path
        self.text_storage = text_storage



    def read_text(self):

        try:
            file = open(self.file_path, "r")  # open file in read mode ("r")
        except Exception as e:
            print(e)
            print("File is not present")
        else:
            self.text_storage = file.readline()
            file.close()
        finally:  # will always run
            file.close()
            print("Always running")
            return self.text_storage



