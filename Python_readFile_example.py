passwordFile = open('SecretPWFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That\'s the kinda thing an idiot would have on his luggage!')
else:
    print('Access denied')