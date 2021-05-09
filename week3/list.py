# Step 1:

# In your Week 3 folder, create a folder called ‘list’ for this assignment.
#  Create a list.py file
# The list.py file should take a list, say for example this one: 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# In the list.py file, write a program that prints out all the elements of the list that are less than 5.
  
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for a in a:
    if a < 5:
        print("{}".format(a))