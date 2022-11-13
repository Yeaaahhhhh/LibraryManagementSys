# Author: Dexter Dai
# Collaborators/references:
# The program is to help librarians to enter the book read by each participants
# generate a report for a given participant that summarizes how many books they have read and
# what level they are currently on
# see a summary of the club activity so far

def welBanner():
    starLine = '*' * 36
    welcome = "WELCOME TO EPL'S SUMMER READING CLUB"
    print(starLine)
    print(welcome)
    print(starLine)
    clubStart()
    
def clubStart():
    global enterDate
    enterDate = input("Please enter the club's start date (YYYYMMDD):")
    invalidEnter = 'Invalid date entered'
    normalMonth = 31 + 1
    otherMonth = 30 + 1
    leapMonth = 29 + 1
    nonLeap = 28 + 1
    for i in enterDate:
        if i not in ['1','2','3','4','5','6','7','8','9','0']:
            print(invalidEnter, end='. ')
            enterDate = clubStart()
            return enterDate
    first9Date = ['01','02','03','04','05','06','07','08','09']
    if enterDate != '' and len(enterDate) == 8:
        if int(enterDate[:4]) in range(1000,10000):
            if enterDate[4:6] in ['01','03','05','07','08','10','12']:
                if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,normalMonth):
                    return enterDate
                else:
                    print(invalidEnter, end='. ')
                    enterDate = clubStart()
                    return enterDate
            elif enterDate[4:6] in ['04','06','09','11']:
                if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,otherMonth):
                    return enterDate
                else:
                    print(invalidEnter, end='. ')
                    enterDate = clubStart()
                    return enterDate                
            elif enterDate[4:6] == '02':
                if int(enterDate[0:4]) % 4 == 0:
                    if int(enterDate[0:4]) % 100 == 0:
                        if int(enterDate[0:4]) % 400 == 0:
                            if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,leapMonth):
                                return enterDate
                            else:
                                print(invalidEnter, end='. ')
                                enterDate = clubStart()
                                return enterDate                             
                        else:
                            if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,nonLeap):
                                return enterDate
                            else:
                                print(invalidEnter, end='. ')
                                enterDate = clubStart()
                                return enterDate
                    else:
                        if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,leapMonth):
                            return enterDate
                        else:
                            print(invalidEnter, end='. ')
                            enterDate = clubStart()
                            return enterDate
                else:
                    if enterDate[6:8] in first9Date or int(enterDate[6:8]) in range(10,nonLeap):
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
        print(invalidEnter, end='. ')
        enterDate = clubStart()
        return enterDate    

def clubTheme():
    themes = []
    clubsDoc = 'clubLevels.txt'
    for line in open(clubsDoc):
        splitLine1 = line.split(':')
        if splitLine1[0] not in themes:
            themes.append(splitLine1[0])
    themes = sorted(themes)
    print('\nThemes to select from:')
    for name in themes:
        print('-',name)
    selectTheme(themes)

def selectTheme(themes):
    global pickTheme
    pickTheme = input('Please pick a theme from the list above:')
    if pickTheme not in themes:
        print('Invalid entry.', end=' ')
        selectTheme(themes)
    else:
        menuOpt(themes)

def menuOpt(themes):
    ques = 'What would you like to do?'
    choice1 = '1. Record a book that has been read.'
    choice2 = '2. Generate a participant report.'
    choice3 = '3. Summarize club activity.'
    choice4 = '4. Quit'
    print('\n' + ques,'\n'+choice1,'\n'+choice2,'\n'+choice3,'\n'+choice4)
    selectMenu(themes)
    
def selectMenu(themes):
    pickOne = input('>')
    if pickOne not in ['1','2','3','4']:
        print('Sorry, invalid entry. Please enter a choice from 1 to 4.')
        selectMenu(themes)
    else:
        if pickOne == '1':
            record(themes)
            menuOpt(themes)
            return
        elif pickOne == '2':
            report(themes)
            menuOpt(themes)
            return
        elif pickOne == '3':
            summerize()
            menuOpt(themes)
            return
        elif pickOne == '4':
            print('Goodbye')
        
def record(themes):
    memberDoc = 'participants.txt'
    bkRead = 'booksRead.txt'
    numList = []
    for line in open(memberDoc):
        splitLine2 = line.split(',')
        splitLine2[-1] = splitLine2[-1].strip()
        numList.append(splitLine2[2])
    newList = []
    for num in numList:
        newList.append(num.replace(' ',''))
    cardNum = input('Card number: ')
    if cardNum in newList:
        bookTitle = input('Book title: ')
        branch = input('Library branch: ')
        newRecord = open(bkRead,'a')
        newRecord.writelines('\n'+branch+'#'+cardNum+'#'+bookTitle +'\n')
        print('Record added successfully.')
    else:
        print('Invalid card number, please re-enter')
        record(themes)
def report(themes):
    
    noBook = 'None yet...'
    bookDoc = open('booksRead.txt')
    bkList = []
    for line in bookDoc:
        seperateLine1 = line.split('#')
        bkList.append(seperateLine1)
    newList = []
    for i in bkList:
        iList = []
        for j in i:
            m = j.strip()
            iList.append(m)
        newList.append(iList)
    
    bkList = newList
    levelDoc = open('clubLevels.txt')
    lvlList = []
    for line in levelDoc:
        seperateLine2 = line.split(':')
        lvlList.append(seperateLine2)
    levelList = []
    for i in lvlList:
        jList = []
        for j in i:
            n = j.strip()
            jList.append(n)
        levelList.append(jList)

    cardNumber = input('Library Card Number: ')
    memberDoc = 'participants.txt'
    file = open(memberDoc)
    div = '-------------------------'
    name = []
    for line in file:
        splitline = line.split(',')
        name.append(splitline)

    fNameList = []
    for f in name:
        first = f[0]
        fNameList.append(first)

    lNameList = []
    for l in name:
        last = l[1].strip()
        lNameList.append(last)

    cardnum = []
    for n in name:
        num = n[2].strip()
        cardnum.append(num)
    birth = []
    for b in name:
        i = b[3].strip()
        birth.append(i)
    birthday = []
    for i in birth:
        if ' ' in i:
            i = birth[birth.index(i)].replace(' ','')
        birthday.append(i)
    numBirth = []
    for item in birthday:
        if item[:3] == 'Jan':
            bir = item.replace(item[:3],'11')    # for calculating age, it cannot be calculated from eg.09 - 01, so change 0 to 1, i.e. 19 - 11
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
            listNum.insert(2,'0')
            num = ''.join(listNum)
        changeBirth.append(num)
    finalBirth = list(map(int, changeBirth))
    calBirth = []
    for i in finalBirth:
        i = i + 100000
        calBirth.append(i)
        year = (enterDate[:4])
        month1 = (enterDate[4:6])
        month2 = int(month1) + 10
        date1 = (enterDate[6:8])
        date2 = int(date1) + 10
    
    calBirth = list(map(str, calBirth))
    if cardNumber in cardnum:
        if len(fNameList[cardnum.index(cardNumber)]) > 8:
            print('\n'+'Report for: ' + '{:>10}'.format(fNameList[cardnum.index(cardNumber)][:7].upper()) + '*' + ' ' + lNameList[cardnum.index(cardNumber)][0].upper())
            if int(year) - int(calBirth[cardnum.index(cardNumber)][4:]) > 0:
                if month2 - int(calBirth[cardnum.index(cardNumber)][:2]) > 0:
                    age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:])
                    print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                    print('Books read:')
                    totalBook = 0
                    for i in bkList:
                        if cardNumber in i:
                            if len(i[2]) > 23:
                                print('-' + i[2][:23] + '*')
                                totalBook += 1
                            else:
                                print('-' + i[2])
                                totalBook += 1
                    preList = []
                    for i in levelList:
                        if pickTheme in i:
                            preList.append(i)
                    for i in range(len(preList) - 1):
                        if totalBook in range(0,int(preList[0][2]) + 1):
                            level = preList[0][1]
                        elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                            level = preList[i+1][1]
                        elif totalBook >= int(preList[-1][2]):
                            level = preList[-1][1]
                    level = level.upper()
                            
                    if totalBook == 0:
                        print(noBook)
                        print('Level:' + '{:>19}'.format(level))
                        print(div)
                    else:
                        print(div)
                        print('Total books read:'+str(totalBook).rjust(8))
                        print('Level:' + '{:>19}'.format(level))
                        print(div)
                elif month2 - int(calBirth[cardnum.index(cardNumber)][2:4]) == 0:
                    if date2 - int(calBirth[cardnum.index(cardNumber)][2:4]) > 0:
                        age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:])
                        print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                        print('Books read:')
                        totalBook = 0
                        for i in bkList:
                            if cardNumber in i:
                                if len(i[2]) > 23:
                                    print('-' + i[2][:23] + '*')
                                    totalBook += 1
                                else:
                                    print('-' + i[2])
                                    totalBook += 1
                        preList = []
                        for i in levelList:
                            if pickTheme in i:
                                preList.append(i)
                        for i in range(len(preList) - 1):
                            if totalBook in range(0,int(preList[0][2]) + 1):
                                level = preList[0][1]
                            elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                                level = preList[i+1][1]
                            elif totalBook >= int(preList[-1][2]):
                                level = preList[-1][1]                                
                        level = level.upper()                 
                        if totalBook == 0:
                            print(noBook)
                            print('Level:' + '{:>19}'.format(level))
                            print(div)
                        else:
                            print(div)
                            print('Total books read:'+str(totalBook).rjust(8))
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                                 
                    elif date2 - int(calBirth[cardnum.index(cardNumber)][2:4]) == 0:
                        age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:])
                        print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                        print('Books read:')
                        totalBook = 0
                        for i in bkList:
                            if cardNumber in i:
                                if len(i[2]) > 23:
                                    print('-' + i[2][:23] + '*')
                                    totalBook += 1
                                else:
                                    print('-' + i[2])
                                    totalBook += 1
                        preList = []
                        for i in levelList:
                            if pickTheme in i:
                                preList.append(i)
                        for i in range(len(preList) - 1):
                            if totalBook in range(0,int(preList[0][2]) + 1):
                                level = preList[0][1]
                            elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                                level = preList[i+1][1]
                            elif totalBook >= int(preList[-1][2]):
                                level = preList[-1][1]                            
                        level = level.upper()                      
                        if totalBook == 0:
                            print(noBook)
                            print('Level:' + '{:>19}'.format(level))
                            print(div)
                        else:
                            print(div)
                            print('Total books read:'+str(totalBook).rjust(8))
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                        
                    else:
                        age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:]) - 1
                        print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                        print('Books read:')
                        totalBook = 0
                        for i in bkList:
                            if cardNumber in i:
                                if len(i[2]) > 23:
                                    print('-' + i[2][:23] + '*')
                                    totalBook += 1
                                else:
                                    print('-' + i[2])
                                    totalBook += 1
                        preList = []
                        for i in levelList:
                            if pickTheme in i:
                                preList.append(i)
                        for i in range(len(preList) - 1):
                            if totalBook in range(0,int(preList[0][2]) + 1):
                                level = preList[0][1]
                            elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                                level = preList[i+1][1]
                            elif totalBook >= int(preList[-1][2]):
                                level = preList[-1][1]                            
                        level = level.upper()
                        if totalBook == 0:
                            print(noBook)
                            print('Level:' + '{:>19}'.format(level))
                            print(div)
                        else:
                            print(div)
                            print('Total books read:'+str(totalBook).rjust(8))
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                        
                else:
                    age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:]) - 1
                    print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                    print('Books read:')
                    totalBook = 0
                    for i in bkList:
                        if cardNumber in i:
                            if len(i[2]) > 23:
                                print('-' + i[2][:23] + '*')
                                totalBook += 1
                            else:
                                print('-' + i[2])
                                totalBook += 1
                    preList = []
                    for i in levelList:
                        if pickTheme in i:
                            preList.append(i)
                    for i in range(len(preList) - 1):
                        if totalBook in range(0,int(preList[0][2]) + 1):
                            level = preList[0][1]
                        elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                            level = preList[i+1][1]
                        elif totalBook >= int(preList[-1][2]):
                            level = preList[-1][1]                            
                    level = level.upper()                
                    if totalBook == 0:
                        print(noBook)
                        print('Level:' + '{:>19}'.format(level))
                        print(div)
                    else:
                        print(div)
                        print('Total books read:'+str(totalBook).rjust(8))
                        print('Level:' + '{:>19}'.format(level))
                        print(div)                    
            else:
                age = 0
                print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                print('Books read:')
                totalBook = 0
                for i in bkList:
                    if cardNumber in i:
                        if len(i[2]) > 23:
                            print('-' + i[2][:23] + '*')
                            totalBook += 1
                        else:
                            print('-' + i[2])
                            totalBook += 1
                    preList = []
                for i in levelList:
                    if pickTheme in i:
                        preList.append(i)
                for i in range(len(preList) - 1):
                    if totalBook in range(0,int(preList[0][2]) + 1):
                        level = preList[0][1]
                    elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                        level = preList[i+1][1]
                    elif totalBook >= int(preList[-1][2]):
                        level = preList[-1][1]                    
                level = level.upper()                          
                if totalBook == 0:
                    print(noBook)
                    print('Level:' + '{:>19}'.format(level))
                    print(div)
                else:
                    print(div)
                    print('Total books read:'+str(totalBook).rjust(8))
                    print('Level:' + '{:>19}'.format(level))
                    print(div)                
        else:
            print('\n'+'Report for: ' + '{:>11}'.format(fNameList[cardnum.index(cardNumber)][:7].upper()) + ' ' + lNameList[cardnum.index(cardNumber)][0].upper())
            if int(year) - int(calBirth[cardnum.index(cardNumber)][4:]) > 0:
                if month2 - int(calBirth[cardnum.index(cardNumber)][:2]) > 0:
                    age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:])
                    print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                    print('Books read:')
                    totalBook = 0
                    for i in bkList:
                        if cardNumber in i:
                            if len(i[2]) > 23:
                                print('-' + i[2][:23] + '*')
                                totalBook += 1
                            else:
                                print('-' + i[2])
                                totalBook += 1
                    preList = []
                    for i in levelList:
                        if pickTheme in i:
                            preList.append(i)
                    for i in range(len(preList) - 1):
                        if totalBook in range(0,int(preList[0][2]) + 1):
                            level = preList[0][1]
                        elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                            level = preList[i+1][1]
                        elif totalBook >= int(preList[-1][2]):
                            level = preList[-1][1]                            
                    level = level.upper()          
                    if totalBook == 0:
                        print(noBook)
                        print('Level:' + '{:>19}'.format(level))
                        print(div)
                    else:
                        print(div)
                        print('Total books read:'+str(totalBook).rjust(8))
                        
                        print('Level:' + '{:>19}'.format(level))
                        print(div)                    
                elif month2 - int(calBirth[cardnum.index(cardNumber)][2:4]) == 0:
                    if date2 - int(calBirth[cardnum.index(cardNumber)][2:4]) > 0:
                        age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:])
                        print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                        print('Books read:')
                        totalBook = 0
                        for i in bkList:
                            if cardNumber in i:
                                if len(i[2]) > 23:
                                    print('-' + i[2][:23] + '*')
                                    totalBook += 1
                                else:
                                    print('-' + i[2])
                                    totalBook += 1
                        preList = []
                        for i in levelList:
                            if pickTheme in i:
                                preList.append(i)
                        for i in range(len(preList) - 1):
                            if totalBook in range(0,int(preList[0][2]) + 1):
                                level = preList[0][1]
                            elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                                level = preList[i+1][1]
                            elif totalBook >= int(preList[-1][2]):
                                level = preList[-1][1]                                
                        level = level.upper()                      
                        if totalBook == 0:
                            print(noBook)
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                        
                        else:
                            print(div)
                            print('Total books read:'+str(totalBook).rjust(8))
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                        
                    elif date2 - int(calBirth[cardnum.index(cardNumber)][2:4]) == 0:
                        age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:])
                        print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                        print('Books read:')
                        totalBook = 0
                        for i in bkList:
                            if cardNumber in i:
                                if len(i[2]) > 23:
                                    print('-' + i[2][:23] + '*')
                                    totalBook += 1
                                else:
                                    print('-' + i[2])
                                    totalBook += 1
                        preList = []
                        for i in levelList:
                            if pickTheme in i:
                                preList.append(i)
                        for i in range(len(preList) - 1):
                            if totalBook in range(0,int(preList[0][2]) + 1):
                                level = preList[0][1]
                            elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                                level = preList[i+1][1]
                            elif totalBook >= int(preList[-1][2]):
                                level = preList[-1][1]                                
                        level = level.upper()                      
                        if totalBook == 0:
                            print(noBook)
                            print('Level:' + '{:>19}'.format(level))
                            print(div)
                        else:
                            print(div)
                            print('Total books read:'+str(totalBook).rjust(8))
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                            
                    else:
                        age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:]) - 1
                        print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                        print('Books read:')
                        totalBook = 0
                        for i in bkList:
                            if cardNumber in i:
                                if len(i[2]) > 23:
                                    print('-' + i[2][:23] + '*')
                                    totalBook += 1
                                else:
                                    print('-' + i[2])
                                    totalBook += 1
                        preList = []
                        for i in levelList:
                            if pickTheme in i:
                                preList.append(i)
                        for i in range(len(preList) - 1):
                            if totalBook in range(0,int(preList[0][2]) + 1):
                                level = preList[0][1]
                            elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                                level = preList[i+1][1]
                            elif totalBook >= int(preList[-1][2]):
                                level = preList[-1][1]                                
                        level = level.upper()                  
                        if totalBook == 0:
                            print(noBook)
                            print('Level:' + '{:>19}'.format(level))
                            print(div)
                        else:
                            print(div)
                            print('Total books read:'+str(totalBook).rjust(8))
                            print('Level:' + '{:>19}'.format(level))
                            print(div)                        
                else:
                    age = int(year) - int(calBirth[cardnum.index(cardNumber)][4:]) - 1
                    print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                    print('Books read:')
                    totalBook = 0
                    for i in bkList:
                        if cardNumber in i:
                            if len(i[2]) > 23:
                                print('-' + i[2][:23] + '*')
                                totalBook += 1
                            else:
                                print('-' + i[2])
                                totalBook += 1
                    preList = []
                    for i in levelList:
                        if pickTheme in i:
                            preList.append(i)
                    for i in range(len(preList) - 1):
                        if totalBook in range(0,int(preList[0][2]) + 1):
                            level = preList[0][1]
                        elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                            level = preList[i+1][1]
                        elif totalBook >= int(preList[-1][2]):
                            level = preList[-1][1]                            
                    level = level.upper()                    
                    if totalBook == 0:
                        print(noBook)
                        print('Level:' + '{:>19}'.format(level))
                        print(div)
                    else:
                        print(div)
                        print('Total books read:'+str(totalBook).rjust(8))
                        print('Level:' + '{:>19}'.format(level))
                        print(div)                    
            else:
                age = 0
                print('Age on ' + year + ' ' + month1 + ' ' + date1 + ':' + '{:>7}'.format(str(age)) + '\n' + div)
                print('Books read:')
                totalBook = 0
                for i in bkList:
                    if cardNumber in i:
                        if len(i[2]) > 23:
                            print('-' + i[2][:23] + '*')
                            totalBook += 1
                        else:
                            print('-' + i[2])
                            totalBook += 1
                preList = []
                for i in levelList:
                    if pickTheme in i:
                        preList.append(i)
                for i in range(len(preList) - 1):
                    if totalBook in range(0,int(preList[0][2]) + 1):
                        level = preList[0][1]
                    elif totalBook in range(int(preList[i][2]),int(preList[i+1][2])):
                        level = preList[i+1][1]
                    elif totalBook > int(preList[-1][2]):
                        level = preList[-1][1]                        
                level = level.upper()                            
                if totalBook == 0:
                    print(noBook)
                    print('Level:' + '{:>19}'.format(level))
                    print(div)
                else:
                    print(div)
                    print('Total books read:'+str(totalBook).rjust(8))
                    print('Level:' + '{:>19}'.format(level))
                    print(div)
        print(preList)
    else:
        print('Invalid library card number.')
        menuOpt(themes)
        

def summerize():
    horizonLine = '+' + '=' * 13 + '+' + '=' * 18 + '+' + '=' * 12 + '+'
    category = '|  Age Group  | Total Books Read | Top Reader |'
    centralLine = '+' + '-' * 13 + '+' + '-' * 18 + '+' + '-' * 12 + '+'
    bookDoc = open('booksRead.txt')
    bkList = []
    for line in bookDoc:
        seperateLine1 = line.split('#')
        bkList.append(seperateLine1)
    newList = []
    for i in bkList:
        iList = []
        for j in i:
            m = j.strip()
            iList.append(m)
        newList.append(iList)
    
    bkList = newList
    
    memberDoc = 'participants.txt'
    file = open(memberDoc)
    name = []
    for line in file:
        splitline = line.split(',')
        name.append(splitline)

    fNameList = []
    for f in name:
        first = f[0]
        fNameList.append(first)

    lNameList = []
    for l in name:
        last = l[1].strip()
        lNameList.append(last)

    cardnum = []
    for n in name:
        num = n[2].strip()
        cardnum.append(num)
    birth = []
    for b in name:
        i = b[3].strip()
        birth.append(i)
    birthday = []
    for i in birth:
        if ' ' in i:
            i = birth[birth.index(i)].replace(' ','')
        birthday.append(i)
    numBirth = []
    for item in birthday:
        if item[:3] == 'Jan':
            bir = item.replace(item[:3],'11')    # for calculating age, it cannot be calculated from eg.09 - 01, so change 0 to 1, i.e. 19 - 11
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
            listNum.insert(2,'0')
            num = ''.join(listNum)
        changeBirth.append(num)
    finalBirth = list(map(int, changeBirth))
    calBirth = []
    for i in finalBirth:
        i = i + 100000
        calBirth.append(i)
        year = (enterDate[:4])
        month1 = (enterDate[4:6])
        month2 = int(month1) + 10
        date1 = (enterDate[6:8])
        date2 = int(date1) + 10
    ageList = []
    
    for i in range(len(calBirth)):
        if int(year) - int(str(calBirth[i])[4:]) > 0:
            if month2 - int(str(calBirth[i])[:2]) > 0:
                age = int(year) - int(str(calBirth[i])[4:])
                ageList.append(age)
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
    fiveUnderL = [] # 5 under last name
    fiveUnderC = [] # 5 under card number
    sixToNineF = []
    sixToNineL = []
    sixToNineC = []
    tenTo14F = []
    tenTo14L = []
    tenTo14C = []
    for i in range(len(ageList)):
        if ageList[i] in range(0,6):
            fiveUnderC.append(cardnum[i])
            fiveUnderF.append(fNameList[i])
            fiveUnderL.append(lNameList[i])
            statsList1 = []
            for l in bkList:
                for num in fiveUnderC:
                    if num in l:
                        statsList1.append(num)
            totalRead1 = len(statsList1)
            dic1 = {}
            for x in statsList1:
                if not x in dic1:
                    dic1[x] = 1
                else:
                    dic1[x] += 1
            cate1 = sorted(dic1.items(), key=lambda d: d[1], reverse= True)
            aList1 = []
            for i in cate1:
                aList1.append(list(i))
            if len(aList1) > 1:            
                if aList1[0][1] == aList1[1][1]:
                    final1 = 'Tied!'
                else:
                    if len(fiveUnderF[cardnum.index(aList1[0][0])]) > 8:
                        final1 = fiveUnderF[fiveUnderC.index(aList1[0][0])][:7].upper() + '*' + ' ' + fiveUnderL[fiveUnderC.index(aList1[0][0])][0].upper()
                    else:
                        final1 = fiveUnderF[fiveUnderC.index(aList1[0][0])].upper() + ' ' + fiveUnderL[fiveUnderC.index(aList1[0][0])][0].upper()
            elif len(aList1) == 1:
                if len(fiveUnderF[cardnum.index(aList1[0][0])]) > 8:
                    final1 = fiveUnderF[fiveUnderC.index(aList1[0][0])][:7].upper() + '*' + ' ' + fiveUnderL[fiveUnderC.index(aList1[0][0])][0].upper()
                else:
                    final1 = fiveUnderF[fiveUnderC.index(aList1[0][0])].upper() + ' ' + fiveUnderL[fiveUnderC.index(aList1[0][0])][0].upper()        
            else:
                final1 = 'N/A'               
            
            
        elif ageList[i] in range(6,10):
            sixToNineC.append(cardnum[i])
            sixToNineF.append(fNameList[i])
            sixToNineL.append(lNameList[i])
            statsList2 = []
            for l in bkList:
                for num in sixToNineC:
                    if num in l:
                        statsList2.append(num)
            totalRead2 = len(statsList2)
            dic2 = {}
            for x in statsList2:
                if not x in dic2:
                    dic2[x] = 1
                else:
                    dic2[x] += 1
            cate = sorted(dic2.items(), key=lambda d: d[1], reverse= True)
            aList2 = []
            for i in cate:
                aList2.append(list(i))
            if len(aList2) > 1:    
                if aList2[0][1] == aList2[1][1]:
                    final2 = 'Tied!'
                else:
                    if len(sixToNineF[sixToNineC.index(aList2[0][0])]) > 8:
                        final2 = sixToNineF[sixToNineC.index(aList2[0][0])][:7].upper() + '*' + ' ' + sixToNineL[sixToNineC.index(aList2[0][0])][0].upper()
                    else:
                        final2 = sixToNineF[sixToNineC.index(aList2[0][0])].upper() + ' ' + sixToNineL[sixToNineC.index(aList2[0][0])][0].upper()
            elif len(aList2) == 1:
                if len(sixToNineF[sixToNineC.index(aList2[0][0])]) > 8:
                    final2 = sixToNineF[sixToNineC.index(aList2[0][0])][:7].upper() + '*' + ' ' + sixToNineL[sixToNineC.index(aList2[0][0])][0].upper()
                else:
                    final2 = sixToNineF[sixToNineC.index(aList2[0][0])].upper() + ' ' + sixToNineL[sixToNineC.index(aList2[0][0])][0].upper()        
            else:
                final2 = 'N/A'
                
        elif ageList[i] in range(10,14):
            tenTo14C.append(cardnum[i])
            tenTo14F.append(fNameList[i])
            tenTo14L.append(lNameList[i])
            statsList3 = []
            for l in bkList:
                for num in tenTo14C:
                    if num in l:
                        statsList3.append(num)
            totalRead3 = len(statsList3)
            dic3 = {}
            for x in statsList3:
                if not x in dic3:
                    dic3[x] = 1
                else:
                    dic3[x] += 1
            cate = sorted(dic3.items(), key=lambda d: d[1], reverse= True)
            aList3 = []
            for i in cate:
                aList3.append(list(i))
            if len(aList3) > 1:    
                if aList3[0][1] == aList3[1][1]:
                    final3 = 'Tied!'
                else:
                    if len(tenTo14F[tenTo14C.index(aList3[0][0])]) > 8:
                        final3 = tenTo14F[tenTo14C.index(aList3[0][0])][:7].upper() + '*' + ' ' + tenTo14F[tenTo14C.index(aList3[0][0])][0].upper()
                    else:
                        final3 = tenTo14F[tenTo14C.index(aList3[0][0])].upper() + ' ' + tenTo14F[tenTo14C.index(aList3[0][0])][0].upper()
            elif len(aList3) == 1:
                if len(tenTo14F[tenTo14C.index(aList3[0][0])]) > 8:
                    final3 = tenTo14F[tenTo14C.index(aList3[0][0])][:7].upper() + '*' + ' ' + tenTo14F[tenTo14C.index(aList3[0][0])][0].upper()
                else:
                    final3 = tenTo14F[tenTo14C.index(aList3[0][0])].upper() + ' ' + tenTo14F[tenTo14C.index(aList3[0][0])][0].upper()        
            else:
                final3 = 'N/A'    
    print(horizonLine)
    print(category)
    print(centralLine)
    print('|' + '{:>13}'.format('5 and under') + '|'+ '{:^18}'.format(totalRead1) + '|' + '{:<12}'.format(final1) + '|')
    print('|' + '{:>13}'.format('6-9') + '|'+ '{:^18}'.format(totalRead2) + '|' + '{:<12}'.format(final2) + '|')
    print('|' + '{:>13}'.format('10-13') + '|'+ '{:^18}'.format(totalRead3) + '|' + '{:<12}'.format(final3) + '|')
    print(horizonLine)
def main():
    welBanner()

    clubTheme()
main()

                