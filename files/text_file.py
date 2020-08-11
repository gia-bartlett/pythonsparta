class Text_File:

    def __init__(self, file_path, text_storage=None):  # no default created for file_path so we must provide one when calling this class
        self.__file_path = file_path
        self.__text_storage = text_storage

    # read in two ways and write in two ways

    def read_text(self):
        file = open(self.file_path, "r")  # open file in read mode ("r")
        # read file
        # self.text_storage = file.read()  # file.read() putting a number in () will print the number of characters
        # for line in file:
        #     print(line)  # can be used to print a certain amount of the file
        # self.text_storage = file.readline()  # will read the first line of the file
        # self.text_storage = file.readline()  # will read the next line of the file
        # print(file.tell())  # prints where the pointer is in the file
        # file.seek()  # sends the pointer to a chosen location in the file
        # self.text_storage = file.readlines()  # will read the first line of the file
        # file.close()  # close file
        # return self.text_storage


    def write_text(self):
        file = open("write.txt", "w")  # open file in write mode ("w")
        # (new file will be created if new filename used)
        file.write("My first edit")
        file.close()
        file = open("write.txt", "a")  # a is append mode
        file.write("\nMy second edit")  # \n = new line
        file.seek(0)
        file.close()
        print(file.closed)  # give me the status of the file
        print(file.name)
        print(file.mode)
        return self.text_storage
        pass

    def read_text_with(self):  # no need to close when using with open
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage
        pass

    def write_text_with(self):
        with open("writer.txt", "w+") as file:
            file.write("Using write with functionality")
            file.seek(0)
            self.text_storage = file.read()
            return self.text_storage
        pass

    def os_module(self):
        import os
        print(os.getcwd())  # current working directory
        # os.remove("writer.txt")  # removes the file named
        print(os.listdir())  # lists the file within current directory
        # os.rename("order.txt", "orders.txt")  # rename a file
        os.chdir("C:\\Users\\gia_b\\Documents\\Caving")
        print(os.getcwd())
        os.open("caving_is_cool.txt", os.O_RDWR, mode = 0o777, dir_fd = None)
        os.mkdir("cave")  # create directory
        os.rmdir("cave")  # remove directory
        pass