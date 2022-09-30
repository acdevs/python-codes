from time import sleep 
import random as rd
print('::::::::::::WELCOME TO THE MATCH: ODDEVE:::::::::::::')
''':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #BEFORE YOU BEGIN,
        A NOTE FOR PLAYER
        1 ENTER THE RESPECTIVE VALUES IN PARENTHESIS/BRACKETS GIVEN NO OTHER VALUES ARE ALLOWED UNLESS STATED!
        2 DO NOT LEAVE THE PROMPT NULL...
        3 ENDLESS PLAY...
        4 BUG FREE...
        5 Skip match using SKIP()
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''
skip=0
def SKIP():
        skip=1
while True:
      
    if skip==1:
        continue
    while True:
            coice=input('ODD(o) OR EVE(e) :').lower()
            try:
                if coice not in ['o','e']:
                        raise TypeError   #just any error
                else:
                        break
            except:
                print(' ---INVALID ENTRY !--- ')
                continue
                
    print('TOSSING...',end='')
    while True:
            try:
                toss_u=int(input('throw [number] : '))
                break
            except:
                print(' ---ENTER VALID VALUE !--- ')
                continue
    toss_c=rd.choice([1,2,3,4,5,6,10])
    if (toss_u+toss_c)%2==0:
        r='e'
        show='EVE'
    else:
        r='o'
        show='ODD'
    print('YOU\tCOMP\n',toss_u,'\t',toss_c,' ...THAT\'S {}'.format(show))
    def check(v):
        if v<1 or v>10:
            return 1
    def bat_u():
        score_u=score_c=0
        print('COMP BOWLS YOU BAT: ')
        while True:
            try:
                xu=int(input(''))
            except:
                print('ERROR RETHROW')
                continue
            if check(xu):
                print('outOfBounds RETHROW')
                continue
            xc=rd.randint(1,10);print(xc,end='\n\n')
            if xu != xc:
                score_u+=xu
            else:
                for i in '                     !!!YOU OUT!!!                      ':
                        print(i,end='')
                        sleep(0)
                print('\nYOUR TOTAL SCORE:',score_u)
                break
        target=score_u+1
        print('COMP NEEDS {} SCORE TO WIN.'.format(target),'\nREADY TO BOWL...?')
        print('YOU BOWL COMP BATS: ')
        while True:
            try:
                yu=int(input(''))
            except:
                print('ERROR RETHROW')
                continue
            if check(yu):
                print('outOfBounds RETHROW')
                continue
            yc=rd.randint(1,10);print(yc,end='\n\n')
            if yu != yc:
                score_c+=yc
                if score_c >= target:
                    V=score_c-score_u
                    print('YOU LOST THE MATCH :( COMP WON BY {} SCORE(s).'.format(V))
                    break
            else:
                V=score_u-score_c
                for i in '              !!!YOU KNOCKED OUT COMP!!!               ':
                        print(i,end='')
                        sleep(0)
                print('\nCOMP TOTAL SCORE:',score_c)
                print('YOU WON BY {} SCORE(s):) '.format(V))
                break
    def bowl_u():
        score_u=score_c=0
        print('YOU BOWL COMP BATS: ')
        while True:
            try:
                xu=int(input(''))
            except:
                print('ERROR RETHROW')
                continue
            if check(xu):
                print('outOfBounds RETHROW')
                continue
            xc=rd.randint(1,10);print(xc,end='\n\n')
            if xu != xc:
                score_c+=xc
            else:
                for i in '                     !!!COMP OUT!!!                    ':
                        print(i,end='')
                        sleep(0)
                print('\nCOMP TOTAL SCORE:',score_c)
                break
        target=score_c+1
        print('YOU NEED {} SCORE TO WIN.'.format(target),'\nCOMP READY TO BOWL...')
        print('COMP BOWLS YOU BAT: ')
        while True:
            try:
                yu=int(input(''))
            except:
                print('ERROR RETHROW')
                continue
            if check(yu):
                print('outOfBounds RETHROW')
                continue
            yc=rd.randint(1,10);print(yc,end='\n\n')
            if yu != yc:
                score_u+=yu
                if score_u >= target:
                    V=score_u-score_c
                    for i in '                  YOU ACED THE MATCH :)                ':
                        print(i,end='')
                        sleep(0)
                    print('\nTOTAL SCORE:',score_u,'YOU WON BY {} SCORE(s).'.format(V))

                    break
            else:
                V=score_c-score_u
                for i in '                  YOU LOST THE MATCH :(                ':
                        print(i,end='')
                        sleep(0)
                print('\nTOTAL SCORE:',score_u)
                print('COMP WON BY {} SCORE(s) '.format(V))
                break        
    def ply_u():
        choice=input('CHOOSE Bat[t] or Bowl[b]: ')
        if choice=='t':
            bat_u()
        else:
            bowl_u()
    def ply_c():
        if rd.randint(1,2)==1:
            choice='t'
            p='BAT'
        else:
            choice='b'
            p='BOWL'
        print('COMP CHOSE TO {}: '.format(p))
        if choice=='b':
            bat_u()
        else:
            bowl_u()

    if coice==r:
        print('YOU WON THE TOSS.',end=' ')
        ply_u()
    else:
        print('YOU LOST THE TOSS.',end=' ')
        ply_c()
    print('\n::::::::::::::::::::::::NEW MATCH::::::::::::::::::::::::::\n')
'''
CODE BY @AC DEVELOPERS
copywrite 2020-2025
Thanks
'''
