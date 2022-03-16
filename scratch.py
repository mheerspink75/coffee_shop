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

sc = [{}, [], []]
message = ''
tip = .15


def start_price_list():
    ##### start the price list and display results #################################
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////')
    print('\n------------------- PRICE LIST -------------------\n')
    for choice, price in coffees.items():
        print(f'   {choice.upper()}:')
        for key in price:
            print(f'                {key.upper()} - ${float(price[key])}0')
    print('\n------------------- ORDER COFFEE ------------------\n')
    print('\n |||||||||||||||| COFFEE SHOP ||||||||||||||||||||\n')

    return choose_coffee()


def choose_coffee():
    ###### loop through coffee and display results #################################
    for choice, price in coffees.items():
        print(
            f'\n------------------- CHOOSE {choice.upper()} ------------------\n')
        print(f'    Choose a {choice}...\n')

        for choices, key in enumerate(price):
            print(
                f'        {choices + 1} - {key.upper()} --> ${float(price[key])}0')

        print(f'        {len(price) + 1} - Quit!')
        print(
            f'\n------------------- CHOOSE {choice.upper()} ------------------\n')

        while True:
            try:
                #### get user input and handle exceptions ##########################
                user_input = int(input())

                if user_input == len(price) + 1:
                    message = f'\nYou chose: {user_input} - Quit: Goodbye!'

                    return print(message)

                #### update temporary data from user input #####################
                user_choice = [i for i in price.keys()]
                user_price = [i for i in price.values()]

                if user_input > 0 and user_input < len(price) + 2:
                    message = f'{user_input} - {user_choice[user_input - 1]}'
                    sc[0].update({user_choice[user_input - 1]
                                 : user_price[user_input - 1]})
                    sc[1].append(user_price[user_input - 1])

                    print(
                        f'\nYou chose: {message.upper()}\n--> ${float(user_price[user_input - 1])}0 added to '
                        f'ORDER TOTAL')

            except:
                print('\nPlease enter a valid choice...')
                continue
            if user_input <= 0 or user_input > len(price) + 1:
                print(f'\nEnter a value between 1 and 4')
                continue
            break

    return store_orders()


def store_orders():
    #### format single orders ##################################
    x = [i for i in sc[0].keys()]
    y = [i for i in sc[0].values()]

    s_order = {
        'id': f'{len(sc[2])}',
        'size': f'{x[0]}',
        'coffee': f'{x[1]}',
        'flavoring': f'{x[2]}',
        '_charges': f'{y}',
        '_coffee': f'${float(sum(y))}0',
        '_tip': f'${round(sum(y) * tip, 2)}',
        '_total': f'${round((sum(y) * tip) + sum(y), 2)}'
    }

    #### store formatted orders in sc[1] ########################
    sc[2].append(s_order)

    #### clear user input choices sc[0] #########################
    sc[0].clear()

    return calculate_price()


def calculate_price():
    c = 'COFFEE'
    if len(sc[1]) > 1:
        c = 'COFFEES'

    #### sum price data stored stored in sc[1] ########################
    coffee_total = sum(sc[1])
    tip_total = coffee_total * tip
    order_total = round(coffee_total + tip_total, 2)

    print('\n|||||||||||| COFFEE SHOP ORDERS |||||||||||||||\n')
    print(f'\n----------- YOU ORDERED {len(sc[2])} {c} ---------------')

    #### display formatted orders stored in sc[2] #####################
    for i in range(len(sc[2])):
        print(f'\n      ORDER {i + 1}:\n')
        for key, value in sc[2][i].items():
            print(f'            {key}: {value}')

    print(f'\nCOFFEE: ${float(coffee_total)}0')
    print(f'TIP: ${float(round(tip_total, 2))}\n')
    print(f'ORDER TOTAL: ${order_total}\n')

    return more_coffee()


def more_coffee():
    while True:
        try:
            #### display options and handle exceptions #########
            print('------------ ORDER ANOTHER COFFEE? --------------')
            user_input = int(input('Order more coffee...\n1 - YES\n2 - NO\n'))
            if user_input == 2:
                return print('Quit - Goodbye!')
            if user_input == 1:
                return start_price_list()
        except:
            print('\nPlease enter a valid choice...')
            continue
        if user_input < 0 or user_input != 2 or user_input != 1:
            print(f'\nEnter a value between 1 and 2')
            continue


start_price_list()
