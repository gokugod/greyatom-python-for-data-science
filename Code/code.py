# --------------
# Code starts here

# Create the lists
class1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio'] 
class2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class1+class2

# Append the list
new_class.append("Peter Warden")
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)



# Create the Dictionary
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}


# Slice the dict and stores  the all subjects marks in variable
a=courses["Math"]
b=courses["English"]
c=courses["History"]
d=courses["French"]
e=courses["Science"]



# Store the all the subject in one variable `Total`
total=a+b+c+d+e

# Print the total
print(total)
# Insert percentage formula
percantage=(345/500)*100

# Print the percentage
print(percantage)



# Create the Dictionary
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
print(mathematics)
max_marks_scored=max(mathematics,key=mathematics.get)
print(max_marks_scored)
# Given string
topper="Andrew Ng"


# Create variable first_name 
first_name,last_name=topper.split(" ")
# Create variable Last_name and store last two element in the list
Last_name=topper[7:9]
print(Last_name)
# Concatenate the string
full_name=Last_name + " " +first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


