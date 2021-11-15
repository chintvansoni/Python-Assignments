class OpenFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


if __name__ == "__main__":
    with OpenFile('Demo.txt', 'r') as opened_file:
        print(opened_file.read())
