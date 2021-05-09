# Step 3:

# In your Week 3 folder, create a folder called ‘join & split’ for this assignment.
# Create a join&split.py file
# In the tuple.py file, write a program according to following specifications
# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with csv']
# print(friends_list)
# From the above fill a list(friend_list) properly with the csv of all the friends. One per “slot”
# You may need to enter same command several times
# Use print() statements to work your way through the exercise.

friend_list = []
csv = ["Eric", "John", "Michael", "Terry", "Graham", "TerryG", "Brian"]
friend_list.append(csv[0])
friend_list.append(csv[1])
friend_list.append(csv[2])
friend_list.append(csv[3])
friend_list.append(csv[4])
friend_list.append(csv[5])
friend_list.append(csv[6])
print(friend_list)