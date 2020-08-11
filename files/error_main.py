from error_text import Text_File_Errors

file_path = "orders.txt"
# by putting the file path here and importing the class we only need to change the file path once if we need to

text_file = Text_File_Errors(file_path)

# print(text_file.read_text())  # reads the whole document with read
# text_file.write_text()  # this won't print anything but will write to the txt file
# print(text_file.write_text())

#print(text_file.write_text_with())
# print(text_file.text_storage)

print(text_file.raise_exception())