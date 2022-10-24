import os

def clear_screen():
    os.system('cls')


def recording_file(data):
    with open('School.csv', 'w', encoding='utf-8') as file:
        for line in data:
            file.writelines(line)
    file.close()


def add_contact(name, date_birth, sch_class, mid_ball):
    with open('School.csv','r', encoding='utf-8') as f:
        data = f.readlines()
        last_line = data[-1]
    f.close()
    
    new_line = []
    id = str(int(last_line[0]) + 1)
    new_line = [id, name, date_birth, sch_class, mid_ball]
    res = ';'.join(new_line)+'\n'
    data.append(res)
    
    return data
    

def dell_contact(num):
    with open('School.csv','r', encoding='utf-8') as f:
        data = f.readlines()
    with open('School.csv', 'w', encoding='utf-8') as file:        
        for line in data:
            id = int(line[0])
            if id != num:
                file.writelines(line)
    file.close()


def find_contact(name, date_birth, sch_class):
    
    tip = [name, date_birth, sch_class]
    with open('School.csv','r', encoding='utf-8') as f:
        data = f.readlines()
    res = []
    for el in tip:
        if el:
            for line in data:
                if el in line:
                    res.append(line)
        
    return(res)


def edit_contact(num, name, date_birth, sch_class, mid_ball):
    tip = [name, date_birth, sch_class, mid_ball]
    with open('School.csv','r', encoding='utf-8') as f:
        data = f.readlines()
    f.close()
    
    for line in data:
        id = int(line[0])
        if id == num:
            
            lst = line.split(';')
            for el in tip:
                if el == 0:
                    continue
                else:
                    ind = tip.index(el)
            
                    for i in lst:
                        index = lst.index(i)
                        if index == ind+1:
                            lst[index] = el
                            
                            res = ';'.join(lst)
            data[id] = res     
    return data