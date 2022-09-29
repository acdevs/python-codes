#dictionary module for finding words meaning.
import mysql.connector as m
db=m.connect(host='localhost',user='Admin',password='',database='test')
if not db.is_connected():
    print('Database Connectivity Failed!')
else:
    #code block goes here
    while True:
        word=input('Find Meaning [enter for exit]: ')
        if not word:
            break
        c=db.cursor()
        sql=f'select * from entries where word="{word}"'
        c.execute(sql)
        entry=c.fetchall()
        if not entry:
            print('Oops ! Can\'t find.')
        else:
            for i in entry:
                print(f'Word Type: {i[1]}')
                print(f'Meaning  : {i[2]}')
                print('-------------------------------------------------------------------------')
