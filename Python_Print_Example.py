print("Hello.  What is your name?")
myName = input()
print('It\'s good to meet you ' + myName + '!')
print('There are this many characters in your name:')
print(len(myName))
print('Cool huh?  So how old are you?')
myAge=input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')
if int(myAge) > 25:
    print('You\'re old! HAHAHAH!')
else:
    print('You\'re still young; but you will be old in ' + str(int(40) - int(myAge)) + ' years.')