# Author: Dexter Dai
# Collaborators/references:
# The program is to help librarians to enter the book read by each participants
# generate a report for a given participant that summarizes how many books they have read and
# what level they are currently on
# see a summary of the club activity so far

def welBanner():
    '''
    the function display the welcome banner of the club
    Input:n/a
    Returns: None
    '''
    numOfStars = 36
    starLine = '*' * numOfStars
    welcome = "WELCOME TO EPL'S SUMMER READING CLUB"  # welcome banner of club
    print(starLine)
    print(welcome)
    print(starLine)
    clubStart()
    
def clubStart():
    '''
    the function is for user to input a date, and calculate and judge whether it is valid
    Input:n/a
    Returns: enterDate
    '''
    
    global enterDate
    enterDate = input("Please enter the club's start date (YYYYMMDD):")  #
    invalidEnter = 'Invalid date entered'
    months31days = ['01','03','05','07','08','10','12']
    months30days = ['04','06','09','11']
    first9Date = ['01','02','03','04','05','06','07','08','09']
    numList = ['1','2','3','4','5','6','7','8','9','0']
    normalMonth = 31 + 1                                          # in the below code, the int is the upperbound of a range, so plus 1, normal months days have 31 days
    otherMonth = 30 + 1                                           # 4, 6, 9,11 has maximum 30 days.
    leapMonth = 29 + 1                                            # leap year Feb has 29 days
    nonLeap = 28 + 1
    for i in enterDate:
        if i not in numList:   # make sure input is numbers, not letters or others
            print(invalidEnter, end='. ')
            enterDate = clubStart()
            return enterDate
    if enterDate != '' and len(enterDate) == 8:                                         # make sure user indeed input a value not directly press 'Enter' and the date length is equal to 8
        if int(enterDate[:4]) in range(1000,10000):                                     # Entered year can be 1000 - 9999
            if enterDate[4:6] in months31days:                                              # when those months have maximum 31 days
                if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,normalMonth):            # to make sure in each month, the first 9 days the user entered is in form '0X'
                    return enterDate
                else:
                    print(invalidEnter, end='. ')                                       # re-enter
                    enterDate = clubStart()
                    return enterDate
            elif enterDate[4:6] in months30days:                               # when those months have maximum 30 days
                if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,otherMonth):
                    return enterDate
                else:
                    print(invalidEnter, end='. ')
                    enterDate = clubStart()
                    return enterDate                
            elif enterDate[4:6] == '02':                                                # Feb month
                if int(enterDate[0:4]) % 4 == 0:                                        # first requirement for leap year: divided by 4
                    if int(enterDate[0:4]) % 100 == 0:                                  # second requirement for leap year: if is XX00 year, leap year cannot be divided by 100
                        if int(enterDate[0:4]) % 400 == 0:                              # if a XX00 year can be divided by 400, so it is a leap year
                            if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,leapMonth):          # make sure the day is correctly entered
                                return enterDate
                            else:
                                print(invalidEnter, end='. ')
                                enterDate = clubStart()
                                return enterDate                             
                        else:                                                                                       # not divided by 400, so it is not leap year
                            if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,nonLeap):            # make sure the entered day is in nonleap days, i.e. has 28 days since it is
                                return enterDate                                                                    # a XX00 year that can be divided by 100 but not 400           
                            else:
                                print(invalidEnter, end='. ')
                                enterDate = clubStart()
                                return enterDate
                    else:
                        if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,leapMonth):              # not divided by 100,but can be divided by 4, so it is a leap year
                            return enterDate
                        else:
                            print(invalidEnter, end='. ')
                            enterDate = clubStart()
                            return enterDate
                else:
                    if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,nonLeap):                    # not divided by 4, so it is not leap year
                        return enterDate
                    else:
                        print(invalidEnter, end='. ')
                        enterDate = clubStart()
                        return enterDate
            else:
                print(invalidEnter, end='. ')
                enterDate = clubStart()
                return enterDate
    else:
        print(invalidEnter, end='. ')                  # make sure print in the same line
        enterDate = clubStart()
        return enterDate    

def clubTheme():
    '''
    the function is to display the club names line by line
    Input:n/a
    Returns: None
    '''
    
    global themes
    themes = []
    clubsDoc = 'clubLevels.txt'
    for line in open(clubsDoc):
        splitLine1 = line.split(':')
        if splitLine1[0] not in themes:
            themes.append(splitLine1[0])               # get the name of each club
    themes = sorted(themes)                            # alphabetical order
    print('\nThemes to select from:')
    for name in themes:
        print('-',name)                                # print line by line
    selectTheme()

def selectTheme():
    ''' 
    for user to enter the theme, should be exactly for what it displayed in the club.txt
    Input:n/a
    Returns: None
    '''
    
    global pickTheme
    pickTheme = input('Please pick a theme from the list above:')
    if pickTheme not in themes:
        print('Invalid entry.', end=' ')
        selectTheme()
    else:
        menuOpt()

def menuOpt():                                                              # Display service table
    ''' 
    the function is going to display the menus for librarian to select
    Input:n/a
    Returns: None
    '''
    
    ques = 'What would you like to do?'
    choice1 = '1. Record a book that has been read.'
    choice2 = '2. Generate a participant report.'
    choice3 = '3. Summarize club activity.'
    choice4 = '4. Quit'
    print('\n' + ques,'\n'+choice1,'\n'+choice2,'\n'+choice3,'\n'+choice4)  # print line by line
    selectMenu()
    
def selectMenu():
    '''
    display a menu for librarian to pick a function
    '''
    
    pickOne = input('>')
    if pickOne not in ['1','2','3','4']:
        print('Sorry, invalid entry. Please enter a choice from 1 to 4.')
        selectMenu()
    else:
        if pickOne == '1':
            record()                                              # record a book that has been read
            menuOpt()
            return
        elif pickOne == '2':
            report()                                              # generate a participant report that contains name, age, books read, and level
            menuOpt()
            return
        elif pickOne == '3':
            summerize()                                           # display the club activity categorized by age group, shows total books read and top readers
            menuOpt()
            return
        elif pickOne == '4':
            print('Goodbye')                                      # quit the system
            
def record():
    ''' 
    for participants to record the books they read
    Inputs:n/a
    Return:None
    '''
    
    memberDoc = 'participants.txt'
    bkRead = 'booksRead.txt'
    numList = []
    for line in open(memberDoc):
        splitLine2 = line.split(',')
        splitLine2[-1] = splitLine2[-1].strip()                    # get card number
        numList.append(splitLine2[2])
    newList = []
    for num in numList:
        newList.append(num.replace(' ',''))
    cardNum = input('Card number: ')
    if cardNum in newList:
        bookTitle = input('Book title: ')
        branch = input('Library branch: ')
        newRecord = open(bkRead,'a')
        newRecord.writelines('\n'+branch+'#'+cardNum+'#'+bookTitle) # write the content in this format
        print('Record added successfully.')
    else:
        print('Invalid library card number.', end='')
        record()
def report():
    ''' 
    generate a participant report that contains name, age, books read, and level
    Input: n/a
    Returns: None
    '''
    
    global cardNumber,totalBook,level
    noBook = 'None yet...'
    cardNumber = input('Library Card Number: ')
    div = '-' *25
    bookNameMax = 23
    totalBook = 0
    level = ''
    if cardNumber in cardnum:
        if len(fNameList[cardnum.index(cardNumber)]) > nameMax:      # for participants whose fisrt name is longer than 8.
            print('\n'+'Report for: ' + '{:>10}'.format(fNameList[cardnum.index(cardNumber)][:nameMax-1].upper()) + '*' + ' ' + lNameList[cardnum.index(cardNumber)][0].upper()) #print first and last name
            calculateAge(year,month2,date2,cardNumber,calBirth,cardnum)    
        else:
            print('\n'+'Report for: ' + '{:>11}'.format(fNameList[cardnum.index(cardNumber)][:nameMax-1].upper()) + ' ' + lNameList[cardnum.index(cardNumber)][0].upper())
            calculateAge(year,month2,date2,cardNumber,calBirth,cardnum)
    else:
        print('Invalid library card number.')
        menuOpt()
def calculateAge(Y,M,D,enteredCard,birthList,cardList):
    '''
    the function is going to calculate ages and it has another function to display
    the level, age, and total books read
    
    Inputs:
        Y: previously entered year
        M: previously entered months
        D: entered date
        enteredCard: previously entered card number
        birthList: a list contain all participants birthdays
        cardList: a list contains all participants card number
        
    Returns: None
    '''
    
    if int(Y) - int(birthList[cardList.index(enteredCard)][4:]) > 0:                # input year - birthday year
        if M - int(birthList[cardList.index(enteredCard)][:2]) > 0:                 # input month - birthday month
            age = int(Y) - int(birthList[cardList.index(enteredCard)][4:])          # age = input year - birth year
            numberAndLevel(cardNumber,totalBook,level,age)
        elif M - int(birthList[cardList.index(enteredCard)][2:4]) == 0:
            if D - int(birthList[cardList.index(enteredCard)][2:4]) > 0:            # if months are same, date difference is greater than 0
                age = int(Y) - int(birthList[cardList.index(enteredCard)][4:])      # age = input year - birth year
                numberAndLevel(cardNumber,totalBook,level,age)
            elif D - int(birthList[cardList.index(enteredCard)][2:4]) == 0:         # if date are same, that day is his/her birthday
                age = int(Y) - int(birthList[cardList.index(enteredCard)][4:])      # age = input year - birth year
                numberAndLevel(cardNumber,totalBook,level,age)                     
            else:
                age = int(Y) - int(birthList[cardList.index(enteredCard)][4:]) - 1  # age = input year - birth year - 1
                numberAndLevel(cardNumber,totalBook,level,age)                       
        else:
            age = int(Y) - int(birthList[cardList.index(enteredCard)][4:]) - 1
            numberAndLevel(cardNumber,totalBook,level,age)                  
    else:
        age = 0
        numberAndLevel(cardNumber,totalBook,level,age)
def numberAndLevel(enterNum,num,aLevel,howOld):
    '''
    the function is going to display the level, age, and total books read of certain reader
    
    Inputs:
        enterNum: cardNumber of user input
        num: calculate total books read
        aLevel: the level of certain participants
        howOld: how old when the participants on that day
        
    Returns: num and level
    '''
    bkList = []
    levelList = []
    openDoc('booksRead.txt','#',bkList)
    openDoc('clubLevels.txt',':',levelList)
    div = '-' * 25   
    print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(howOld)) + '\n' + div)
    print('Books read:')    
    bookNameMax = 23
    for i in bkList:
        if enterNum in i:
            if len(i[2]) > bookNameMax:
                print('-' + i[2][:bookNameMax] + '*')                           # for those books that title is longer than 23 characters==> Harry Potter and XXX...*
                num += 1
            else:
                print('-' + i[2])
                num += 1
    preList = []
    for i in levelList:
        if pickTheme in i:
            preList.append(i)
    for i in range(len(preList) - 1):                                           # find the level
        if num in range(0,int(preList[0][2]) + 1):                              # participants read 0 to the number of first level books
            aLevel = preList[0][1]
        elif num in range(int(preList[i][2]),int(preList[i+1][2])):             # participants read between i level and i+1 level books
            if num == int(preList[i][2]):                                       # some levels are consistant, just like 6 books -level A, 7 books- level B
                aLevel = preList[i][1]
            else:                                                               # for those who are not consistant levels
                aLevel = preList[i+1][1]
        elif num >= int(preList[-1][2]):                                        # when total read books exceed the number of the highest level
            aLevel = preList[-1][1]                                             # the level will be the highest level
    aLevel = aLevel.upper()    
    if num == 0:                                                                # no books read by a participants, print 'None yet...'
        print('None yet...')
        print('Level:' + '{:>19}'.format(aLevel))
        print(div)
    else:
        print(div)
        print('Total books read:'+str(num).rjust(8))
        print('Level:' + '{:>19}'.format(aLevel))
        print(div)
    return num, aLevel

def summerize():
    '''
    the function is going to summerize the total books read in each age group and display the top reader in that group
    Input: n/a
    Return: None
    '''
    
    horizonLine = '+' + '=' * 13 + '+' + '=' * 18 + '+' + '=' * 12 + '+'
    category = '|  Age Group  | Total Books Read | Top Reader |'
    centralLine = '+' + '-' * 13 + '+' + '-' * 18 + '+' + '-' * 12 + '+'
    ageList = []                                                        # a list that contain ages for those participants,eg. [2,3,4,6,7,3,1,....]
    for i in range(len(calBirth)):
        if int(year) - int(str(calBirth[i])[4:]) > 0:                   # calculate ages as before
            if month2 - int(str(calBirth[i])[:2]) > 0:
                age = int(year) - int(str(calBirth[i])[4:])
                ageList.append(age)                                     # append the age into ageList
            elif month2 - int(str(calBirth[i])[2:4]) == 0:
                if date2 - int(str(calBirth[i])[2:4]) > 0:
                    age = int(year) - int(str(calBirth[i])[4:])
                    ageList.append(age)
                elif date2 - int(str(calBirth[i])[2:4]) == 0:
                    age = int(year) - int(str(calBirth[i])[4:])
                    ageList.append(age)
                else:
                    age = int(year) - int(str(calBirth[i])[4:]) - 1
                    ageList.append(age)
            else:
                age = int(year) - int(str(calBirth[i])[4:]) - 1
                ageList.append(age)
        else:
            age = 0
            ageList.append(age)
    fiveUnderF = [] #  5 under fisrt name
    fiveUnderL = [] #  5 under last name
    fiveUnderC = [] #  5 under card number
    sixToNineF = [] #  same as previous one
    sixToNineL = []
    sixToNineC = []
    tenTo14F = []
    tenTo14L = []
    tenTo14C = []
    ageBar1 = 5
    ageBar2 = 9
    ageBar3 = 13
    for i in range(len(ageList)):
        if ageList[i] in range(0,ageBar1+1):
            final1 = ''
            totalRead1 = 0                
            fiveUnderC.append(cardnum[i])               # create a list that contains card number of participants whose age ranging from 0 - 5
            fiveUnderF.append(fNameList[i])             # create a list that contains first name of participants whose age ranging from 0 - 5
            fiveUnderL.append(lNameList[i])             # create a list that contains last name of participants whose age ranging from 0 - 5   
        elif ageList[i] in range(ageBar1+1,ageBar2+1):
            sixToNineC.append(cardnum[i])               # same as the previous group
            sixToNineF.append(fNameList[i])
            sixToNineL.append(lNameList[i])
            final2 = ''
            totalRead2 = 0       
        elif ageList[i] in range(ageBar2+1,ageBar3+1):
            tenTo14C.append(cardnum[i])
            tenTo14F.append(fNameList[i])
            tenTo14L.append(lNameList[i])
            final3 = ''
            totalRead3 = 0           
    r1c1 = totalAndTopReader(fiveUnderC,fiveUnderF,fiveUnderL,totalRead1,final1)[0]  # row 1 column 1 relative to the main table, i.e. the total read of the age group
    r1c2 = totalAndTopReader(fiveUnderC,fiveUnderF,fiveUnderL,totalRead1,final1)[1]  # row 1 column 2 , i.e. the top reader
    r2c1 = totalAndTopReader(sixToNineC,sixToNineF,sixToNineL,totalRead2,final2)[0]  # row 2 column 1 ...
    r2c2 = totalAndTopReader(sixToNineC,sixToNineF,sixToNineL,totalRead2,final2)[1]  # ...
    r3c1 = totalAndTopReader(tenTo14C, tenTo14F, tenTo14L,totalRead3,final3)[0]
    r3c2 = totalAndTopReader(tenTo14C, tenTo14F, tenTo14L,totalRead3,final3)[1]
    print(horizonLine)
    print(category)
    print(centralLine)
    print('|' + '{:>13}'.format('5 and under') + '|' + '{:^18}'.format(r1c1) + '|' + '{:<12}'.format(r1c2) + '|')
    print('|' + '{:>13}'.format('6-9') + '|'+ '{:^18}'.format(r2c1) + '|' + '{:<12}'.format(r2c2) + '|')
    print('|' + '{:>13}'.format('10-13') + '|'+ '{:^18}'.format(r3c1) + '|' + '{:<12}'.format(r3c2) + '|')
    print(horizonLine)
    
def totalAndTopReader(listA,listB,listC,totalRead,final):
    '''
    this function is to prepare card number, first-last name of each participants of each age group
    
    Inputs:
        listA: in such age group, what card number it will contain
        listB: in such age group, what first name it will contain
        listC: in such age group, what last name it will contain
        totalRead: the length of the books list for the participants in this age group, i.e. the number of total books
        final: who rank first, read most books, it's a combination of first name(first 7 characters) and last name initial
    
    Return total book read and top reader's name
    '''
    
    bkList = []
    openDoc('booksRead.txt','#',bkList)    
    stats = []
    for l in bkList:
        for num in listA:
            if num in l:
                stats.append(num)
    totalRead = len(stats)          # summerize total books in the age group
    dic = {}                        # a dictionary that contains {cardnumber of a participant: how many times the cardnumber appears}
    for x in stats:
        if not x in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    cate = sorted(dic.items(), key=lambda d: d[1], reverse= True) # reverse and sorted, the first dic value may be the largest number(some times tied)
    listD = []
    for i in cate:
        listD.append(list(i))
    if len(listD) > 1:                         # there are more than 1 participants in this age group     
        if listD[0][1] == listD[1][1]:         # the number of books read of participants in certain age group are same
            final = 'Tied!'
        else:
            if len(listB[listA.index(listD[0][0])]) > nameMax:
                final = listB[listA.index(listD[0][0])][:7].upper() + '*' + ' ' + listC[listA.index(listD[0][0])][0].upper()  # final is the top reader printed in the format as before
            else:
                final = listB[listA.index(listD[0][0])].upper() + ' ' + listC[listA.index(listD[0][0])][0].upper()
    elif len(listD) == 1:                      # there is only one participant in this age group
        if len(listB[listA.index(listD[0][0])]) > nameMax:
            final = listB[listA.index(listD[0][0])][:7].upper() + '*' + ' ' + listC[listA.index(listD[0][0])][0].upper()
        else:
            final = listB[listA.index(listD[0][0])].upper() + ' ' + listC[listA.index(listD[0][0])][0].upper()
    else:
        final = 'N/A'                          # no participants read books in certain age group
    return totalRead, final

def openDoc(fileName,separator,yList):
    '''
    the function is going to open a certain file
    
    Inputs:
        fileName: in the same folder, the file will be opened
        separator: what symbol that separate the item of each line, in this program is '#' or ',' .etc.
        yList: a new clear list with no separators, no spaces, no empty list
        
    Return: yList
    '''
    
    xList = []
    for line in open(fileName):
        separateLine = line.split(separator)
        xList.append(separateLine)
    for i in xList:
        jList = []
        for j in i:
            n = j.strip()
            jList.append(n)
        if jList != ['']:           #to prevent an empty line that only contain 'Enter'
            yList.append(jList)
    return yList

def createList(aList,pos,bList):
    '''
    prepare the list for future usage
    
    Inputs:
        aList: the overall list, such as participants information
        pos: position of certain information such as first name is at [0] position
        bList: empty list, for future usage, only contains one information
        
    return: bList: a list that only contains one ID information
    '''
    
    for i in aList:
        iD = i[pos]
        bList.append(iD)
    return bList
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
main()

                