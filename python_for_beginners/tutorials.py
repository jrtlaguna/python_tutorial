from datetime import datetime, timedelta

def using_print():
    print('Hello world')


def comment():
    # These are comments
    print("There are comments above me.")


def strings_and_format():

    user_first = input('What is your first name? ')
    user_last = input('What is your last name? ')

    # first_name = 'Christopher'
    # last_name = 'Harrison'
    # print(first_name.capitalize + ' ' + last_name.capitalize)

    # print('Your name is ' + user_first.capitalize() + ' ' + user_last.capitalize())
    print('Your name is {} {}.'.format(user_first.capitalize(), user_last.capitalize()))

def numbers():

    num1 = input("Enter a number: ")
    num2 = input("Enter a second number: ")
    
    print("Their product is " + str(int(num1)*int(num2)))


def date_demo():
    today = datetime.now()
    one_day = timedelta(days=1)
    yesterday = today - one_day

    print('Yesterday was ' + datetime.strftime(yesterday, '%D'))

def error_handling():

    x = 23
    y = 0

    try:
        print(x/y)
    except ZeroDivisionError as e:
        print('Not allowed to divide by 0')
        print(e)
    else:
        print('Something went wrong')
    finally:
        print("Move on...")
    
def conditional():

    price = float(input('how much did you pay? '))

    if price >= 100:
        tax = 0.7

    else:
        tax = 0
    print('Tax rate is: ' + str(tax))

    if price > 90 and tax != 0.7:
        print('Multiple condiitons')


def collections_and_loops():

    people = []

    susan = {}
    susan['first'] = 'Susan'
    susan['last'] = 'Ibach'

    christopher = {}
    christopher['first'] = 'Christopher'
    christopher['last'] = 'Columbus'

    people.append(susan)
    people.append(christopher)


    for p in people:
        print(p)


def parameterized(name='John'):


    print(name)



    