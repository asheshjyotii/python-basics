'''
1. Write a script that converts the following strings to lowercase: "An-
imals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase
string on a separate line.
'''
string = ["Animals", "Badger", "Honey Bee", "Honeybadger"]
print("Lower")
for x in string :
    x = x.lower() # since string are immutable therefore reassigning
    print(x+"\n")

'''
2. Repeat Exercise 1, but convert each string to uppercase instead of
lowercase.
'''

string = ["Animals", "Badger", "Honey Bee", "Honeybadger"]
print("Upper")
for x in string :
    x = x.upper()
    print(x+"\n")

'''
3. Write a script that removes whitespace from the following strings:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
Print out the strings with the whitespace removed.
'''

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print("removing whitespace...")
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

'''
4. Write a script that prints out the result of .startswith("be") on each
of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
'''

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print("The strings starting with 'be' are")
print(string1+"->",string1.startswith("be"))
print(string2+"->",string2.startswith("be"))
print(string3+"->",string3.startswith("be"))
print(string4+"->",string4.startswith("be"))

'''
5. Using the same four strings from Exercise 4, write a script that
uses string methods to alter each string so that .startswith("be")
returns True for all of them
'''
print("checking the spelling without case sensitive")
string = ["Becomes", "becomes" ,"BEAR"," bEautiful"]
for index, elements in enumerate(iterable=string,start=1):
    x = x.strip()
    x = x.lower()
    if x.startswith("be"):
        print(f"string{index} - > True")
    else:
        print(f"string{index} - > False")

# Methods : Starts with and ends with
string1 = "Anil"
print(string1.startswith("An")) # True
print(string1.endswith("il")) # True

# Methods : find()
string1 = "Do you want burgers?"
print(string1.find("burger")) # 12
print(string1[12:]) # burgers?

# Methods : replace ()
string1 = "This is USA, the world superpower, Im proud to be a citizen of USA"
print(string1.replace("USA","INDIA"))