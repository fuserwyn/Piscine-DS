class Research:
    def file_reader(self):
        file = open("data.csv", "r")
        text = file.read()
        return text

if __name__ == '__main__':
    m = Research()
    print(m.file_reader())