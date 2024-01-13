import pickle as p
def display():
    f=open('sn.dat','rb')
    s=0
    try:
        while True:
            a = p.load(f)
            if disease[Id] == 'covid':
                s=s+1
                print(a,a[1])
    except EOFError:
        print('Total No of covid paitent: ',s)

display()
