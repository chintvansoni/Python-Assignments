class OpenFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


def read_file(name):
    text_string = ""

    with OpenFile(name, 'r') as opened_read_file:
        for line in opened_read_file:

            if "Aqua" in line:
                text_string += "Azure #007fff\n"
            else:
                text_string += line

    return text_string


def write_file(name, text_string):
    with OpenFile(name, 'w') as opened_file:
        opened_file.write(text_string)
    

if __name__ == "__main__":
    colour_text = ""

    colour_text = read_file('colours.txt')

    write_file('colours.txt', colour_text)
