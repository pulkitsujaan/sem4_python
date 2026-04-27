class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, "w") as f:
            f.write(data)
        print("File written.")

    def read(self):
        with open(self.filename, "r") as f:
            return f.read()

    def append(self, data):
        with open(self.filename, "a") as f:
            f.write(data)
        print("Data appended.")

fm = FileManager("test.txt")
fm.write("Hello!\n")
fm.append("More data.\n")
print(fm.read())