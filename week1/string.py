from datetime import datetime
name = input('What is your name? ')
age = int(input('How old are you? '))
hundred = int((100-age) + datetime.now().year)
print ('You will turn 100 years old in %s.' % (hundred))

