# Author: Dexter Dai
# Collaborators/references:
# The program is to help librarians to enter the book read by each participants
# generate a report for a given participant that summarizes how many books they have read and
# what level they are currently on
# see a summary of the club activity so far

import multiprocessing

# 将您的所有函数移至这里...

def main():
    '''
    make basic changes of birthday months and prepare some important lists for operation
    Input: n/a
    Return: None
    '''
    welBanner()

    global year, month1, month2,date1,date2,calBirth,fNameList,lNameList,nameMax,cardnum
    name = []
    nameMax = 8                             # maximum of first name letters printed
    openDoc('participants.txt', ',',name)  
    fNameList = []
    lNameList = []
    cardnum = []
    birth = []
    createList(name,0,fNameList)            # prepare a list that only contain first name
    createList(name,1,lNameList)            # last name list
    createList(name,2,cardnum)              # card number list
    createList(name,3,birth)                # birthday list
    birthday = []
    for i in birth:
        if ' ' in i:
            i = birth[birth.index(i)].replace(' ','')
        birthday.append(i)
    numBirth = []
    for item in birthday:
        if item[:3] == 'Jan':
            bir = item.replace(item[:3],'11')    # for calculating age, it cannot be calculated from eg.09 - 01, so change 0 to 1, i.e. 19 - 11 = 8, it works for calculating age
        elif item[:3] == 'Feb':
            bir = item.replace(item[:3],'12')
        elif item[:3] == 'Mar':
            bir = item.replace(item[:3],'13')
        elif item[:3] == 'Apr':
            bir = item.replace(item[:3],'14')
        elif item[:3] == 'May':
            bir = item.replace(item[:3],'15')
        elif item[:3] == 'Jun':
            bir = item.replace(item[:3],'16')
        elif item[:3] == 'Jul':
            bir = item.replace(item[:3],'17')
        elif item[:3] == 'Aug':
            bir = item.replace(item[:3],'18')
        elif item[:3] == 'Sep':
            bir = item.replace(item[:3],'19')
        elif item[:3] == 'Oct':
            bir = item.replace(item[:3],'20')
        elif item[:3] == 'Nov':
            bir = item.replace(item[:3],'21')
        elif item[:3] == 'Dec':
            bir = item.replace(item[:3],'22')            
        numBirth.append(bir)
    # calculate age
    changeBirth = []
    for num in numBirth:
        if len(num) < 8:
            listNum = list(num)
            listNum.insert(2,'0')                       # to make a 8-digit date since some are 7 digits date 
            num = ''.join(listNum)
        changeBirth.append(num)
    finalBirth = list(map(int, changeBirth))
    calBirth = []                                       # birthdays of each participant     
    for i in finalBirth:
        i = i + 100000                                  # for calculating age, change days of 01,02,03...to 11,12,13 and 21,22,23 to 31, 32, 33, it works for ages!
        calBirth.append(i)
    calBirth = list(map(str, calBirth))
    calBirth = calBirth
    year = (enterDate[:4])
    month1 = (enterDate[4:6])
    month2 = int(month1) + 10                           # for calculating age, change months of 01,02,03...to 11,12,13, it works for ages!
    date1 = (enterDate[6:8])
    date2 = int(date1) + 10    
    clubTheme()

if __name__ == "__main__":
    # create pool
    pool = multiprocessing.Pool()

    # start pool
    for _ in range(multiprocessing.cpu_count()):  # 使用CPU核心数的数量来启动进程
        pool.apply_async(main)

    # 关闭进程池
    pool.close()
    pool.join()

                