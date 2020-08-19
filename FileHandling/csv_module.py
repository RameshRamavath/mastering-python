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

## read file with specific delimiter

with open('new_names.csv', 'r') as new_file:
    csv_reader = csv.reader(new_file)

    csv_reader2 = csv.reader(new_file, delimiter = '\t')

    # for line in csv_reader:
    #     print line   # gives list of single element [bcz by default it expects ',' delimiter]

    for line in csv_reader2:
        print (line)