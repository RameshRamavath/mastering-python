"""

Suppose we have files with names in below format.

January - Google #1.txt
February - Google #2.txt
March - Google #3.txt
April - Google #4.txt
May - Google #5.txt
December - Google #12.txt

because files started with month names -- they will be look like below - how to automate renaming them and
display in order of month

December - Google #12.txt
February - Google #2.txt
January - Google #1.txt
March - Google #3.txt

"""

import os

print(os.getcwd())
path = '/Users/313248/Desktop/python-learning'
# change path as working dir

os.chdir(path=path)
print(os.getcwd())

# get the list of files

list_files = os.listdir(path=path)

# for file in list_files:
#     f_name, f_ext = os.path.splitext(file)
#     # print(f_name, "--", f_ext)
#     # split f_name
#     month, company = f_name.split('-')
#     month = month.strip()
#     company = company.strip()
#
#     f_company, f_num = company.split(' ')
#     # print(f_company, f_num)
#     # remove # from number and make all number double digit {zfill}
#     f_num = f_num[1:].zfill(2)
#     # print(f_num)
#
#     new_name = f"{f_num} {month}{f_ext}"
#     print(new_name)
#
#     # rename files
#
#     os.rename(file, new_name)


# check if files are in order now

for f in list_files:
    f_num, f_name = f.split(' ')
    new_name = f"{f_num}-{f_name}"
    # print(new_name)
    os.rename(f,new_name)


