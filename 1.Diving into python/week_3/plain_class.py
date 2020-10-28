class FileReader:

    def __init__(self, file):
        self.file = file

    def read(self):
        try:
            with open(self.file, 'r') as r:
                return r.read()
        except:
            return ''


with open('/Users/jsabina/PycharmProjects/text.txt', 'w') as f:
    f.write("SHO ZA?")
    f.close()

reader = FileReader('/Users/jsabina/PycharmProjects/text.txxt')
text = reader.read()
print(text)
