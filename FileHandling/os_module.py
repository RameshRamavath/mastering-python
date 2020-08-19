import os

# get current working dir and files list in it
print( os.getcwd())
print( os.listdir('/Users/313248/PycharmProjects/mastering-python/FileHandling'))

# change working dir
os.chdir('/Users/313248/Desktop')
print( os.getcwd())
print( os.listdir('/Users/313248/Desktop'))

# create new folders in working dir

os.mkdir('mkdir-test')  # create dir in cwd
os.makedirs('mkdir-test2/sub-folder1')  # creates sub-folders {create complete path} - tree structure

# delete folders

os.rmdir('mkdir-test')
# os.removedirs('mkdir-test2')

