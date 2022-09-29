'''python SQLike'''
print(f'...Initializing {__name__}')
__all__=['cdb',
         'use',
         'deldb',
         'ct',
         'ins',
         'st',
         'delt'
         ]
print('''
Commands:-
    cdb  : create database
    use  : use database
    deldb: delete database
    ct   : create table
    ins  : insert into table
    st   : select table
    delt : delete table
''')
import os,csv
crd='..\\..\\'
def cdb(name):
    d=(crd+name)
    os.mkdir(d)
    
def use(name):
    global crd
    if os.path.exists(crd+name):
        crd+=name+'\\'
    else:
        return '...db not found!'

def deldb(name):
    crd='C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\'
    try:
        if os.path.exists(crd+name):
            os.rmdir(crd+name)
        else:
            return '...db not found,cannot be deleted!'
    except OSError:
        return '...db is not empty!'
    
def ct(name,*header):
    try:
        f=open(crd+name+'.txt','w')
        f.write(','.join(header)+'\n')
    except:
        print('...create table operation failed!')
    finally:
        f.close()

def ins(name,*values):
    try:
        if os.path.exists(crd+name+'.txt'):
            f=open(crd+name+'.txt','a')
            f.write(','.join(values)+'\n')
    except:
        print('...insert table operation failed!')
    finally:
        f.close()

def st(name):
    try:
        fo=open(crd+name+'.txt','r')
        f=csv.reader(fo)
        ref=list(f).copy()
        header=ref[0]
        centvalue=[]
        counter=0
        for i in range(len(header)):
                centvalue.append(0)
                for j in range(len(ref)):
                        if centvalue[counter]<len(ref[j][i]):
                                centvalue[counter]=len(ref[j][i])+2
                counter+=1
        counter=0
        borderlen=sum(centvalue)+len(header)+1
        print('-'*borderlen)
        for h in header:
                print(f'|{h.center(centvalue[counter]," ").capitalize()}',end='')
                counter+=1
        print('|')
        print('='*borderlen)
        l=0
        for r in ref:
                counter=0
                if l==0:
                        l+=1
                        continue
                for c in r:
                        if c == '':
                                print(f'|{"Null".center(centvalue[counter]," ")}',end='')
                        else:
                                print(f'|{c.center(centvalue[counter]," ")}',end='')
                        counter+=1
                print('|')
                print('-'*borderlen)
                l+=1
        print(f'Operation ok! ...{l} row(s) processed.')
    except:
            print(f'...select operation Failed!')
    finally:
        fo.close()

def delt(name):
    if os.path.exists(crd+name+'.txt'):
        os.remove(crd+name+'.txt')
    else:
        return '...table not found,cannot be deleted!'
