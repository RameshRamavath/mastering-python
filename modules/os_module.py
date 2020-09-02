import os

# get current working dir and files list in it
print(os.getcwd())
print(os.listdir('/Users/313248/PycharmProjects/mastering-python/FileHandling'))

# change working dir
os.chdir('/Users/313248/Desktop')
print(os.getcwd())
print(os.listdir('/Users/313248/Desktop'))

# create new folders in working dir

os.mkdir('mkdir-test')  # create dir in cwd
# os.makedirs('mkdir-test2/sub-folder1')  # creates sub-folders {create complete path} - tree structure

# delete folders

os.rmdir('mkdir-test')
# os.removedirs('mkdir-test2')

os.chdir('/Users/313248/Desktop/mkdir-test2')

# change file name

# os.rename('python_test.py','python_renamed.py')
# print(os.listdir(os.getcwd()))

# *** get the info about the file

# print(os.stat('python_renamed.py'))  # will get file size, time created, time modified etc
# from datetime import datetime
# modfied_time = os.stat('python_renamed.py').st_mtime
# print(datetime.fromtimestamp(modfied_time)) # 2020-08-18 11:33:56.086586


# *** get environment variables

print(os.environ.get('HOME'))  # /Users/313248

# create a file text.txt in home dir

file_name = 'test.txt'
file_path = os.environ.get('HOME') + file_name
print(file_path)  # /Users/313248test.txt  ** easy to forget the backslash after home dir

# better to use os.path module while working with paths

print(os.path.join(os.environ.get('HOME'), file_name))  # /Users/313248/test.txt

# get the file name and dir name

print(os.path.basename('/Users/Ramesh/test.txt'))  # test.txt
print(os.path.dirname('/Users/Ramesh/test.txt'))  # /Users/Ramesh
print(os.path.split('/Users/Ramesh/test.txt'))  # ('/Users/Ramesh', 'test.txt')

print(os.path.exists('/Users/Ramesh/test.txt'))  # False

print(os.path.isdir('/Users/313248/docker-compose.yml'))  # False
print(os.path.isdir('/Users/313248'))  # True
print(os.path.isfile('/Users/313248/docker-compose.yml'))  # True

# get the file root and the file extension

print(os.path.splitext('/Users/313248/docker-compose.yml'))   # ('/Users/313248/docker-compose', '.yml')
