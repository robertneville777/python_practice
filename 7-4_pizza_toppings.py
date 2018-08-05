prompt = "What pizza topping do you want?\n"
prompt += "Enter 'quit' when you are finished.\n>> "
pizza_topping = ''

while pizza_topping != 'quit':
    pizza_topping = input(prompt) 
    print(pizza_topping + " added.")
