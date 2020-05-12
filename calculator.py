# calculator
T=1
while T<=100:
    try: a=float(input("Enter Your 1st number: "))
    except: print('\n\t\tSorry it is wrong, Enter a Number\n')
    try: b=input("choise Your mark(+,-,*,/): ")
    except: print('Chosse one')
    try: c=float(input('Enter Your 2nd number: '))
    except: print('\n\t\tSorry it is wrong, Enter a Number\n')
    if b=='+':
        print(a,b,c,'=',a+c)
        break
    elif b=='-':
        print(a,b,c,'=',a-c)
        break
    elif b=='/':
        print(a,b,c,'=',a/c)
        break
    elif b=='*':
        print(a,b,c,'=',a*c)
        break
    else:
        print('Try again')
T=T+1