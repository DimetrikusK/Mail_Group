import os
import tempfile


class File:
    direct = 'file'

    def __init__(self, dir):
        self.dir = dir
        with open(self.dir, 'w') as f:
            f.write('')

    def __add__(self, other):
        file = File(os.path.join(tempfile.gettempdir(), self.direct))
        with open(file.dir, 'w') as f:
            with open(self.dir, 'r') as j:
                with open(other.dir, 'r') as n:
                    f.write(j.read()), (f.write(n.read()))
        return file

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     tmp = []
    #     with open(self.dir, 'r') as f:
    #         for i in f:
    #             tmp.append(i.split(','))
    #     return tmp

    def __getitem__(self, item):
        tmp = []
        with open(self.dir, 'r') as f:
            for i in f:
                tmp.append(i.split(','))
        return tmp[item]

    def __str__(self):
        return self.dir

    def read(self):
        with open(self.dir, 'r') as f:
            print(f.read())

    def write(self, string):
        with open(self.dir, 'w') as f:
            f.write(string)
            print(len(string))


path_to_file = 'some_filename'
# os.path.exists(path_to_file)
# file_obj = File(path_to_file)
# os.path.exists(path_to_file)
# file_obj.read()
# file_obj.write('some text')
# file_obj.read()
# file_obj.write('other text')
# file_obj.read()
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
# print(new_file_obj)
# print(isinstance(new_file_obj, File))
# print(type(new_file_obj))

for line in new_file_obj:
    print(ascii(line))
