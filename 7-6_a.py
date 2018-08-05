prompt = "What pizza topping do you want?\n"
prompt += "Enter 'quit' when you are finished.\n>> "
pizza_topping = ''

while 1:
    pizza_topping = input(prompt) 
    if pizza_topping == 'quit':
        break
    print(pizza_topping + " added.")
