prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    elif city == '':
        print("Input can't be blank. Please input again!")
    else:
        print("I'd love to go to %s!" % city.title())
