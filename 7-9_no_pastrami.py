sandwich_orders = ['ham','bologna','pastrami',
    'pastrami','pastrami','tuna','chicken']
finished_sandwiches = []

print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
