# Coffee Shop
coffee_sizes = {
    'small': 2,
    'medium': 3,
    'large': 4
}

coffees = {
    'brewed': 0,
    'expresso': float(.5),
    'cold_brew': 1
}

flavoring = {
    'none': 0,
    'hazelnut': float(.5),
    'vanilla': float(.5),
    'caramel': float(.5)
}

x = [coffee_sizes, coffees, flavoring]
y = ['size', 'coffee', 'flavor']

tip = float(.15)

order = {}
message = ''


def start_price_list():
    print('Price List:')
    for i in range(len(x)):
        print(f'{y[i]}: {x[i]}')

    return order_coffee()


def order_coffee():
    for i in range(len(x)):
        while len(order) < len(order) + 1:
            next_choice = x[i]
            choices = [key for key in next_choice.keys()]
            price = [value for value in next_choice.values()]

            print(f'\nChoose a {y[i]}...\n')
            for j in range(len(x[i])):
                print(f'{j+1} - {choices[j]}')
            print(f'{len(x[i]) + 1} - quit\n')

            try:
                s_input = int(input())
                if s_input == len(next_choice) + 1:
                    message = f'\nYou chose: {s_input} - Quit: Goodbye!'
                    return print(message)
                else:
                    if s_input !=0:
                        message = f'{s_input} - {choices[s_input - 1]}'
                        user_choice = {
                            f'{choices[s_input - 1]}': price[s_input - 1]}
                        order.update(user_choice)
                        print(
                            f'\nYou chose: {message}\n${round(float(price[s_input - 1]), 2)} added to order_total')
            except:
                print('\nPlease enter a valid choice...')
                continue
            if s_input == 0:
                print(f'\nEnter a value between 1 and 4')
                continue
            break

    return calculate_total()


def calculate_total():
    print(f'\nCoffee Order: {order}\n')
    total = round(float(sum(order.values())), 2)
    tip_amount = round(float(total * tip), 2)

    return print(f'Coffee: ${total}\nTip: ${tip_amount}\n\nTotal: ${round(total + tip_amount, 2)}')


start_price_list()
