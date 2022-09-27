import turtle  #imports turtle
import DClogos1  #imports function/module library

print('''What do you want printed out, the Green arrow logo, or the Flash logo?.
Type in below if you want arrow or flash:''')  #intro/info


def retry(): #asks user what logo they want and if the answer is invaild
    answer = input('answer here: ')   #will continue to ask
    if answer == 'arrow':
        DClogos1.GreenArrow1()
    elif answer == 'flash':
        DClogos1.Flash1()
    else:
        print('invalid answer')
        print('do you want to try again?')
        answer2 = input('')
        if answer2 == 'yes' or answer2 == 'y':
            retry()



retry()  #runs the function above
        

