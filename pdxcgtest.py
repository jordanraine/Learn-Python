def is_yes(answer):
    if ( answer.lower().find('y') == 0 or answer.lower().find('ok') == 0 ):
        return True;
    else:
        return False;
def times(a, b):
    return a * b
def print_times(a, b):
    print times(a, b)

def divide(a, b):
    return a / b
def print_divide(a, b):
    print divide(a, b)


def add(a, b):
    return a + b
def print_add(a, b):
    print add(a, b)
print "Hello World. Would you like to see my test?"
answer = raw_input()
if ( not is_yes(answer) ):
    print "Maybe next time\n"
    quit();

fruits = ['Apples', 'Bananas', 'Oranges'] 
        
print "Awesome, do you like fruit?"
answer = raw_input()
if (is_yes(answer)):
     print "Excellent! Here is a list of fruits that hopefully satisfy you."

else:
    print "thats too bad. It's really good for you"

for fruit in fruits:
    print " %s " % fruit   
print "are you ready to try out some math?\n"
answer = raw_input()
if (is_yes(answer)):
    print "is it true that 5 + 5 = 10\n"
else:
    print "Maybe next time?"
    quit();
answer = raw_input()
if ( add(5, 5)):

    print "That is correct 5 + 5 does = "
    print_add(5, 5)
else:
    print "That is not correct 5 + 5 = " ,
    print_add(5, 5)

print "\nWhat is 15 * 10?"
answer = raw_input()
if ( times(15, 10)):
    print "Hey! You are pretty good at this! it was definitely was\n"
    print_times(15, 10)
else:
    print "you failz! The correct answer is "
    print_times(15, 10)

print "What is 6 / 3?"
answer=raw_input()
if ( divide(6, 3)):
    print "Yep! The answer was correct with\n"
    print_divide(6, 3)
else:
    print "That is incorrect, the correct answer is "
    print_divide(6, 3)

