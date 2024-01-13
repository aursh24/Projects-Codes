import pickle as p
def disease():
    f=open('sn.data','wb')
    choice = 'Yes'
    while choice == 'Yes':
        d={}
        n = 'in record'
        while n == 'in record' :
            Id = int(input('Enter Id'))
            name = input('Enter name of Paitient')
            disease = input('Enter name of disease')
            d[Id]='name','disease'
            p.dump(d,f)
            print('Do you want to append more records?')
            choice = input('Yes or No')
            if choice == 'Yes':
                d.update({Id:(name,disease)})
            else:
                break
    
disease()
