def read_file(path):
    with open(path, 'r') as data:
        f_content = data.read()
        print (f_content)
        # for line in f_content:
        #     print line


def read_file_lines(path):
    with open(path, 'r') as data:
        f_content = data.readlines() # gives list of lines, but reading whole file in memory
        # print (f_content)
        for line in f_content:
             print (line)


def read_file_line_by_line(path):
    with open(path, 'r') as data:
        for line in data:
             print (line)


if __name__ == '__main__':
    read_file_line_by_line("/Users/313248/PycharmProjects/mastering-python/Resources/data.txt")
