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


# Price List
def start_price_list():
    print('Price List:')
    for i in range(len(x)):
        print(f'{y[i]}: {x[i]}')
    return choose_coffee()

# Choose Coffee
def choose_coffee():
    message = ''

    while len(order) < len(x):
        # Get the coffee size
        if len(order) == 0:
            next_choice = x[0]
            choices = [key for key in next_choice.keys()]
            price = [value for value in next_choice.values()]

            # Input Question
            print(f'\nChoose a {y[0]}...\n')
            for i in range(len(x[0])):
                print(f'{i+1} - {choices[i]}')
            print(f'{len(x[0]) + 1} - quit\n')

            # Exception Handling
            try:
                s_input = int(input())
                if s_input == len(next_choice) + 1:
                    message = f'\nYou chose: {s_input} - Quit: Goodbye!'
                    return print(message)
                else:
                    message = f'{s_input} - {choices[s_input - 1]}'
                    user_choice = {
                        f'{choices[s_input - 1]}': price[s_input - 1]}
                    order.update(user_choice)
                    print(
                        f'\nYou chose: {message}\n${round(float(price[s_input - 1]), 2)} added to order_total')
            except:
                print('\nPlease enter a valid choice...')
                continue
            if s_input < 1 or s_input > len(x[0]) + 1:
                print('\nEnter a value between 1 and 4')
                continue

            # Get the coffee type
            if len(order) == 1:
                next_choice = x[1]
                choices = [key for key in next_choice.keys()]
                price = [value for value in next_choice.values()]

                # Input Question
                print(f'\nChoose a {y[1]}...\n')
                for j in range(len(x[1])):
                    print(f'{j+1} - {choices[j]}')
                print(f'{len(x[1]) + 1} - quit\n')

                # Exception Handling
                try:
                    s_input = int(input())
                    if s_input == len(next_choice) + 1:
                        message = f'You chose: {s_input} - Quit: Goodbye!'
                        return print(message)
                    else:
                        message = f'{s_input} - {choices[s_input - 1]}'
                        user_choice = {
                            f'{choices[s_input - 1]}': price[s_input - 1]}
                        order.update(user_choice)
                        print(
                            f'\nYou chose: {message}\n${round(float(price[s_input - 1]), 2)} added to order_total\n')
                except:
                    print('Please enter a valid choice...')
                    continue
                if s_input < 1 or s_input > len(x[1]) + 1:
                    print('Enter a value between 1 and 4')
                    continue

            # Get the flavor
            if len(order) == 2:
                next_choice = x[2]
                choices = [key for key in next_choice.keys()]
                price = [value for value in next_choice.values()]

                # Input Question
                print(f'\nChoose a {y[2]}...\n')
                for k in range(len(x[2])):
                    print(f'{k+1} - {choices[k]}')
                print(f'{len(x[2]) + 1} - quit\n')

                # Exception Handling
                try:
                    s_input = int(input())
                    if s_input == len(next_choice) + 1:
                        message = f'You chose: {s_input} - Quit: Goodbye!'
                        return print(message)
                    else:
                        message = f'{s_input} - {choices[s_input - 1]}'
                        user_choice = {
                            f'{choices[s_input - 1]}': price[s_input - 1]}
                        order.update(user_choice)
                        print(
                            f'\nYou chose: {message}\n${round(float(price[s_input - 1]), 2)} added to order_total\n')
                except:
                    print('Please enter a valid choice...')
                    continue
                if s_input < 1 or s_input > len(x[1]) + 1:
                    print('Enter a value between 1 and 4')
                    continue
        break

    return calculate_total()


def calculate_total():
    print(f'Coffee Order: {order}\n')
    total = round(float(sum(order.values())), 2)
    tip_amount = round(float(total * tip), 2)
    return print(f'Coffee: ${total}\nTip: ${tip_amount}\n\nTotal: ${round(total + tip_amount, 2)}')


start_price_list()
