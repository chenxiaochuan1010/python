## Slicing a list
- To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0,1,2.
```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```
- If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```
- Similar syntax if you omit the second index:
```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
```
*Advantage: you don't need to know the length of the list.*

- If you need a slice of list for last three of a list, do like following:
```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```
## Copying a list using a slice
```
friend_foods = my_foods[:] -> 1
friend_foods = my_foods -> 2
```
**Case 1 does not equal to Case 2.**

	Case 1: Both lists are independent, only copied items at this moment are the same. Any item added to one of these lists only, then the two lists are different.
	
	Case 2: Both lists are identical **all the time**!
## Tuple
An immutable list is called a *tuple*.

## PEP8
- PEP8 recommends that you use four spaces per indentation level. TABs and SPACEs must not be mixed used otherwise they are very difficult to diagnose.

##Checking That a List Is NOT Empty
```
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding %s." % requested_topping)
else:
    print("Are you sure you want a plain pizza?")
```
As shown in above example, when the name of a list is used in an **if** statement, Python returns **True** if the list contains at least one item; an empty list evaluates to **False**.

# Dictionaries
*A dictionary in Python is a collection of key-value pairs.*
- In Python, a dictionary is wrapped in braces,{}, with a series of key-value pairs inside the braces, e.g.
```
alien_0 = {'color': 'green', 'points': 5}
```
- You can have unlimited number of key-value pairs in a dictionary.
- Dictionaries are dynamic structures. You can add new key-value pairs at any time.
- Python does NOT care the order of the key-value pairs!

## A Dictionary of Similar Objects
Herewith an example:
```
favorite_languages = {
        'jen':'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
```
**Note: the last colma could be omitted.**

# Looping Through a Dictionary
## Looping Through All Key-Value Pairs
```
for key, value in user_0.items()::
	print("\nKey: " + key)
	print("Value: " + value)
```
The variable *key* and *value* can also be named with other names as you like, e.g.
```
for k,v in user_0.items()
```

## Looping through All the keys in a Dictionary
See in this example:
```
for name in favorite_numbers.keys():
    print(name.title())
```
**Looping through the keys is default!**
You can also write above code like this:
```
for name in favorite_languages:
```

## Looping Through a Dictionary's Keys in Order
*sorted()* function must be used.

## Looping Through All Values in a Dictionary
By using *values()* method, you can get a list of values without any keys. Repeats might exist.
In order to get rid of repeats, *set()* function must be used.

# Nesting
- a list of dictionaries

# Input() function
- If a prompt is too long, save it in a variable.
```
prompt = "If you tell us who you are, we can personalize the mesages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, %s!" % name.title())
```
- Return value of *input()* function is a string!
- When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.
- If you're using Python 2.7, use *raw_input()* instead of *input()*.

# While Loops
A *while* loop runs as long as, or *while*, a certain condition is true.

## Using a Flag
- If many possible events might occur to stop the program, trying to test all these conditions in one *while* statement becomes complicated and difficult.
- We can write our programs so they run while the *flag* is set to *True* and stop running when any of several events sets the value of the *flag* to False. 
``` 
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```
## Using break to Exit a loop
- This is another way to exit a loop.
- You can use the *break* statement in any of Python's loops.

## Using continue in a Loop
- You can use the *continue* statement to return to the beginning of the loop, based on the result of a conditional test.
- In case of an infinite loop, press *CTRL+C* to exit the loop. 

## Using a while loop with Lists and Dictionaries
- You shouldn't modify a list inside a *for* loop because Python will have trouble keeping track of the items in the list.
- To modify a list as you work through it, use a *while* loop.
```
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)

    print("Verifiying user: %s" % current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(unconfirmed_users)
print(confirmed_users)
```
- The *while* loop runs as long as the list *unconfirmed_users* is not empty.

### *remove()*, *del()*, *pop()*
- *remove()* and *pop()* are methods; *del()* is a function
- *remove()* takes values as inputs; *pop()* takes index as inputs

### Removing All Instances of Specific Values from a List
```
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```
- After printing the list, Python enters the while loop because it finds the value 'cat' in the list at least once. 
- Once inside the loop, Python removes the first instance of 'cat', returns to the while line, and then reenters the loop when it finds that 'cat' is still in the list. 