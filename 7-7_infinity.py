prompt = "What pizza topping do you want?\n"
prompt += "Enter 'quit' when you are finished.\n>> "
pizza_topping = input(prompt) 

while pizza_topping != 'quit':
    print(pizza_topping + " added.")
