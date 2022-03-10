# Coffee Shop
coffee_sizes = {
    'small': 2,
    'medium': 3,
    'large': 4
}

coffees = {
    'brewed': 0,
    'expresso': .5,
    'cold_brew': 1
}

flavoring = {
    'none': 0,
    'hazelnut': .5,
    'vanilla': .5,
    'caramel': .5
}

x = [coffee_sizes, coffees, flavoring]
y = ['size', 'coffee', 'flavor']

tip = .15

order = {}
message = ''


def start_price_list():
    print('Price List:')
    for i in range(len(x)):
        print(f'{y[i]}: {x[i]}')

    return order_coffee()


def order_coffee():
    for i in range(len(x)):
        next_choice = x[i]
        choices = [key for key in next_choice.keys()]
        price = [value for value in next_choice.values()]

        while len(order) < len(order) + 1:
            print(f'\nChoose a {y[i]}...\n')

            for j in range(len(next_choice)):
                print(f'{j+1} - {choices[j]}')
            print(f'{len(next_choice) + 1} - quit\n')

            try:
                s_input = int(input())
                if s_input == len(next_choice) + 1:
                    message = f'\nYou chose: {s_input} - Quit: Goodbye!'

                    return print(message)
                else:
                    if s_input != 0:
                        message = f'{s_input} - {choices[s_input - 1]}'
                        user_choice = {
                            f'{choices[s_input - 1]}': price[s_input - 1]}
                        order.update(user_choice)
                        print(
                            f'\nYou chose: {message}\n${price[s_input - 1]} added to order_total')
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
    total = float(sum(order.values()))
    tip_amount = total * tip

    return print(f'Coffee: ${total}\nTip: ${tip_amount}\n\nTotal: ${round(total + tip_amount, 2)}')


start_price_list()
