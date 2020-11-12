gender=input('enter your gender:(male or female)=')
age=int(input('enter your age'))
if age>=18:
    if gender=='male':
        print('u can buy beer')
    elif gender=='female':
        print('u can buy beer girl')
else:
    print('go home')