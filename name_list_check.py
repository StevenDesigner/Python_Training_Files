# Get the number of users to register
num_users = int(input("Enter the number of users to register: "))

# Initialize an empty array to store the names
names = []

# Get names from users and store them in the array
for i in range(num_users):
    name = input("Enter name {}: ".format(i+1))
    names.append(name)

# Check if a name is in the list
check_name = input("Enter a name to check if it's in the list: ")
found = False
for name in names:
    if name == check_name:
        found = True
        break

if found:
    print("{} is in the list.".format(check_name))
else:
    print("{} is not in the list.".format(check_name))
