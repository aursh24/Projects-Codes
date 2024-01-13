while True:
    n=int(input('Enter a year'))
    if n%100==0:
        if n%400==0:
            print('Its a century leap year')
        else:
            print("Not a century leap Year")
    elif n%4==0:
            print('leap year')
    else:
        print('Not a leap Year')

    print('Do you want to check for more years? Press Y/N ')
    ch=input()
    if ch=='N' or ch=='n':
        break
    else:
        continue
