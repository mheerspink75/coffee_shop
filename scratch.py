################################################
################# COFFEE SHOP ##################
##### Matt Heerspink ###########################
##### 03/11/2022 ###############################
################################################

coffees = {
    'size': {
        'small': 2,
        'medium': 3,
        'large': 4
    },
    'coffee': {
        'brewed': 0,
        'expresso': .5,
        'cold_brew': 1
    },
    'flavoring': {
        'none': 0,
        'hazelnut': .5,
        'vanilla': .5,
        'caramel': .5
    }
}

message = ''
single_choices = []
single_charges = []
total_charges = []
orders = []
tip = .15


def start_price_list():
    ##### start the price list and display results ###########################
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////')
    print('\n--------------------PRICE LIST--------------------\n')
    for choice, price in coffees.items():
        print(f'   {choice.upper()}:')
        for key in price:
            print(f'                {key.upper()} - ${float(price[key])}0')
    print('\n--------------------ORDER COFFEE-------------------\n')
    print('\n |||||||||||||||| COFFEE SHOP ||||||||||||||||||||\n')
    return choose_coffee()


def choose_coffee():
    for choice, price in coffees.items():
        user_choice = [i for i in price.keys()]
        user_price = [i for i in price.values()]
        print(f'\n--------------------Choose {choice.upper()}-------------------\n')
        print(f'    Choose a {choice}...\n')
        for choices, key in enumerate(price):
            print(f'        {choices + 1} - {key.upper()} --> ${float(price[key])}0')
        print(f'        {len(price) + 1} - Quit!')

        while True:
            try:
                user_input = int(input())

                if user_input == len(price) + 1:
                    message = f'\nYou chose: {user_input} - Quit: Goodbye!'

                    return print(message)
                else:
                    if user_input != 0:
                        message = f'{user_input} - {user_choice[user_input - 1]}'
                        single_choices.append(user_choice[user_input - 1])
                        single_charges.append(user_price[user_input - 1])
                        total_charges.append(user_price[user_input - 1])
                        print(
                            f'\nYou chose: {message.upper()}\n--> ${float(user_price[user_input - 1])}0 added to '
                            f'ORDER TOTAL')
            except:
                print('\nPlease enter a valid choice...')
                continue
            if user_input == 0:
                print(f'\nEnter a value between 1 and 4')
                continue
            break

    return store_orders()


def store_orders():
    s_order = {
        'id': f'{len(orders)}',
        'size': f'{single_choices[0]}',
        'coffee': f'{single_choices[1]}',
        'flavoring': f'{single_choices[2]}',
        'charges': f'{single_charges}',
        'total': f'{float(sum(single_charges))}'
    }

    orders.append(s_order)

    for i in range(len(single_charges)):
        single_choices.pop()
        single_charges.pop()

    return calculate_price()


def calculate_price():
    coffeez = 'COFFEE'
    if len(orders) != 0:
        coffeez = 'COFFEES'

    coffee_total = sum(total_charges)
    tip_total = coffee_total * tip
    order_total = round(coffee_total + tip_total, 2)

    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////')
    print(f'\n----------- YOU ORDERED {len(orders)} {coffeez} ---------------')

    for i in range(len(orders)):
        print(f'\n      ORDER {i + 1}:\n')
        for key, value in orders[i].items():
            print(f'            {key}: {value}')

    print(f'\nCOFFEE: ${float(coffee_total)}0')
    print(f'TIP: ${float(round(tip_total, 2))}\n')
    print(f'ORDER TOTAL: ${order_total}\n')
    print('------------ ORDER ANOTHER COFFEE? --------------')
    print('\n|||||||||||||||| COFFEE SHOP ||||||||||||||||||||\n')

    while True:
        try:
            user_input = int(input('Order more coffee...\n1 - YES\n2 - NO\n'))
            if user_input == 2:
                print('Quit - Goodbye!')
                break
            if user_input == 1:
                return start_price_list()
        except:
            print('\nPlease enter a valid choice...')
            continue
        if user_input == 0:
            print(f'\nEnter a value between 1 and 4')
            continue
        break

    return


start_price_list()
