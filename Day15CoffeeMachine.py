from Day15CoffeeData import resources, MENU, logo

coffeeMenu = MENU
coffeeResources = resources
emoji = '☕'
money = 0
resource_water = resources['water']
resource_milk = resources['milk']
resource_coffee = resources['coffee']


def coffeemachine():
    global money, resource_coffee, resource_milk, resource_water
    user_input = str(input('What would you like? (espresso/latte/cappuccino): ')).lower()
    if user_input == 'report':
        print(f'Water: {resource_water}ml\nMilk: {resource_milk}ml\nCoffee: {resource_coffee}g\nMoney: ${money}')
        coffeemachine()
    elif user_input == 'off':
        quit()
    elif user_input == 'latte' or user_input == 'espresso' or user_input == 'cappuccino':
        drink_water = coffeeMenu[user_input]['ingredients']['water']
        drink_milk = coffeeMenu[user_input]['ingredients']['milk']
        drink_coffee = coffeeMenu[user_input]['ingredients']['coffee']
        if resource_milk < drink_milk:
            print('Sorry there is not enough milk.')
            coffeemachine()
        if resource_water < drink_water:
            print('Sorry there is not enough water.')
            coffeemachine()
        if resource_coffee < drink_coffee:
            print('Sorry there is not enough coffee.')
            coffeemachine()
        print('Please insert coins')
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickles = int(input('how many nickles?: '))
        pennies = int(input('how many pennies?: '))
        total = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
        if coffeeMenu[user_input]['cost'] > total:
            print('Sorry that\'s not enough money. Money refunded.')
        else:
            change = round(total - coffeeMenu[user_input]['cost'], 2)
            print(f'Here is ${change} in change.')
            print(f'Here is your {user_input} {emoji}. Enjoy!')
            total = round(total - change, 2)
            money += total
            resource_water = resource_water - drink_water
            resource_coffee = resource_coffee - drink_coffee
            resource_milk = resource_milk - drink_milk
        coffeemachine()
    else:
        print('Invalid Response, Please try again!')
        coffeemachine()




print('Welcome to Toye\'s Coffee Machine')
print(logo)
coffeemachine()

