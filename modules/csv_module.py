import csv

# read the file and usr csv.reader() method to read the file

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print type(csv_reader)

# for line in csv_reader:
#     print line            # list of elements

# for line in csv_reader:
#     print line[2]  # print only email id's


# how to skip first line (header)  - using generator's next() method

# next(csv_reader)
# for line in csv_reader:
#     print line[0]


# open the csv file, change the delimiter and write to new csv file

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_names.csv', 'w') as new_file:
#         csv_writer =  csv.writer(new_file, delimiter = '\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

# *** read file with specific delimiter  ***

with open('new_names.csv', 'r') as new_file:
    csv_reader = csv.reader(new_file)

    csv_reader2 = csv.reader(new_file, delimiter='\t')

    # for line in csv_reader:
    #     print line   # gives list of single element [bcz by default it expects ',' delimiter]

    for line in csv_reader2:
        print(line)

# *** CSV data with dict reader and dict writer

with open('names.csv', 'r') as file:
    file_reader = csv.DictReader(file)
    # for line in file_reader:
    #     #print(line)  # {'first_name': 'John', 'last_name': 'Doe', 'email': 'john-doe@bogusemail.com'}
    #     """
    #     to read any value from each line, no need to mention index, instead we can pass key - as we have each line
    #     as dict
    #     """
    #     print(line.get('email'))

    """
    to write data from dict to csv file, we need to give column names as list
    """

    with open('names_dict.csv', 'w') as file_writer:
        # col_names = ['first_name', 'last_name']
        col_names = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(file_writer, fieldnames=col_names, delimiter='\t')
        # write fieldnames a header
        csv_writer.writeheader()

        for line in file_reader:
            # del line['email']
            csv_writer.writerow(line)


