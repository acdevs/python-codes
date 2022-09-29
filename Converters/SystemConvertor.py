def decq(x):
    h=list(bin(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Bin: ",n)
    h=list(hex(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Hex: ",n.capitalize())
    h=list(oct(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Oct: ",n)
def binq(x):
    x=eval('0b'+x)
    print("Dec: ",x)
    h=list(hex(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Hex: ",n.capitalize())
    h=list(oct(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Oct: ",n)
def octq(x):
    x=eval('0o'+x)
    h=list(bin(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Bin: ",n)
    h=list(hex(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Hex: ",n.capitalize())
    print("Dec: ",x)
def hexq(x):
    x=eval('0x'+x)
    h=list(bin(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Bin: ",n)
    h=list(oct(x))
    del h[0:2]
    n=''
    for i in h:
       n=n+i
    print("Oct: ",n)
    print("Dec: ",x)
user='y'
while user=='y':
    ask=input('Covert all: (b/d/o/h )\nEnter Number System(in which you want to enter digit): ')
    if ask=='d':
        x=int(input('Number: '))
        decq(x)
    elif ask=='b':
        x=input('Number: ')
        binq(x)
    elif ask=='o':
        x=input('Number: ')
        octq(x)
    elif ask=='h':
        x=input('Number: ')
        hexq(x)
    user=input('Convert again ? (y/n) ')
else:
    print('\tfinished!\nHow was the experience ?')
