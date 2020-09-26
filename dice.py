from random import randint

while True:
    def action(x):
        user=input('press enter to roll dice')
        num=randint(1,6)
        print('user{}:'.format(x),num)
        return num
    number=action(1)
    number2=action(2)
    if number>number2:
        print('user 1 is winner')
    elif number2==number:
        print('no winner')
    else:
        print('user2 is winner')
    q=input('press q to quit')
    if q=='q':
        break
print('thanks for playing')
