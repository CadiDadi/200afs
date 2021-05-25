# if & else statements 
a = 130
b = 130
if b < a:
    print("b is less than a")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are the same value")

DrivingSpeed = 75
if DrivingSpeed > 75:
    print("you get a ticket")
elif DrivingSpeed < 75:
    print("you do not get a ticket")
else:
    print("you are driving the speed limit")

# nested conditions
# https://www.techbeamers.com/python-tutorial-step-by-step/

# while loops
i = 100
while i < 102:
    print(i)
    i=i+1  # necessary or continues to run

# do while loops

# for loops
StudentNames1 = ["StudentA", "StudentB", "StudentC"]
for x in StudentNames1: 
    print(x) # prints items in a string
print(StudentNames1) # prints items individually

# lists - ordered, allows duplicates, allows different data types
StudentNames2 = ["StudentDD", "StudentEE", "StudentFF", "xxx"]
print(StudentNames2)
print(len(StudentNames2)) # len - how many items in list
print(StudentNames2[1]) # 0 indexing

# strings - split (string.split) & join (string.join)
mary = 'Mary had a little lamb'
    
# tuples
