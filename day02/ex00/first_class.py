class Must_read:
    file = open("data.csv", "r")
    text = file.read()
    print(text)

if __name__ == '__main__':
    m = Must_read()