#Some inbuilt functions

# dir() function
# These all statements will print the inbuit functions present in python
print(dir(""))
print(dir([]))
print(dir(()))
print(dir({}))

#String functions

statement = "Luffy is going to be the pirate king"
print(statement.capitalize()) #capitalize the statement
print(statement.upper())#every letter becomes uppercase
print(statement.islower()) #checks if every letter is in lowercase
print(statement.isupper()) #checks if every letter is in uppercase
print(statement.find("is")) #finds and returns the index of the string in the given string
print(statement.find("Sukuna")) #It will return -1 as "Sukuna" is not present in the statement
print(statement[0:5]) #prints the substring from index 0 to 4

fact = ["Sukuna", "is", "incredibly", "strong"]
print(" ".join(fact)) # joins the substrings with the given regex
fact.append("and scary") #appends the substring into the list
print(fact)
fact.insert(1,"Ryomen") #inserts the given string at  
print(fact)
fact.pop()
print(fact)

dict = {"Name":"Gojo Satoru","Skill":"Sorcerrer"}
print(dict.keys()) #prints all the keys in the dict
print(dict.values()) #prints all the values in the dict