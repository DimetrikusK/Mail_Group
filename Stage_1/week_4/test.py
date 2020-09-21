import os
import tempfile
st = 'some_text'
st_2 = 'some_text_2'
dir = "some_dir"
dir_2 = "some_dir_2"
file_dir = 'lol'
print(os.path.join(tempfile.gettempdir(), file_dir))

# with open(dir, 'w') as f:
#     f.write(st)
#
# with open(dir_2, 'w') as f:
#     f.write(st_2)
#     # write(dir, dir_2)
#
#
# with open(os.path.join(tempfile.gettempdir(), file_dir), 'w') as f:
#     with open(dir, 'r') as j:
#         with open(dir_2, 'r') as n:
#             f.write(j.read() + '\n')
#             f.write(n.read())



# creat()


path_to_file = 'some_filename'
os.path.exists(path_to_file)
file_obj = File(path_to_file)
os.path.exists(path_to_file)
file_obj.read()
file_obj.write('some text')
file_obj.read()
file_obj.write('other text')
file_obj.read()
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
isinstance(new_file_obj, File)