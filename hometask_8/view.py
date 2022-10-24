def print_data():
    with open('School.csv','r', encoding='utf-8') as f:
        data = f.readlines()
    for line in data:
        print(line.replace(';', '   ').replace('\n', ''))
    f.close()


def view_resultat(res):
    print()
    for i in res:
        print(i.replace(';', '   ').replace('\n', ''))


def view_line(line):
    line = str(line)
    print(line.replace(';', ' '))