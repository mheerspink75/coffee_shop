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

sc = [[], [], [], []]
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
        user_choice = [i for i in price.keys()]
        user_price = [i for i in price.values()]
        print(f'\n------------------- CHOOSE {choice.upper()} ------------------\n')
        print(f'    Choose a {choice}...\n')
        for choices, key in enumerate(price):
            print(f'        {choices + 1} - {key.upper()} --> ${float(price[key])}0')
        print(f'        {len(price) + 1} - Quit!')
        print(f'\n------------------- CHOOSE {choice.upper()} ------------------\n')

        while True:
            try:
                #### get user input and handle exceptions ##########################
                user_input = int(input())

                if user_input == len(price) + 1:
                    message = f'\nYou chose: {user_input} - Quit: Goodbye!'

                    return print(message)
                else:
                    #### update temporary data from user input #####################
                    if user_input != 0:
                        message = f'{user_input} - {user_choice[user_input - 1]}'
                        sc[0].append(user_choice[user_input - 1])
                        sc[1].append(user_price[user_input - 1])
                        sc[2].append(user_price[user_input - 1])
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
    #### format single orders ##################################
    s_order = {
        'id': f'{len(sc[3])}',
        'size': f'{sc[0][0]}',
        'coffee': f'{sc[0][1]}',
        'flavoring': f'{sc[0][2]}',
        '_charges': f'{sc[1]}',
        '_coffee': f'${float(sum(sc[1]))}0',
        '_tip': f'${round(sum(sc[1]) * tip, 2)}',
        '_total': f'${round((sum(sc[1]) * tip) + sum(sc[1]), 2)}'
    }

    #### store formatted orders in sc[3] ########################
    sc[3].append(s_order)

    #### user input choices from sc[0] and sc[1] ################
    for i in range(len(sc[0])):
        sc[0].pop()
        sc[1].pop()

    return calculate_price()


def calculate_price():
    c = 'COFFEE'
    if len(sc[3]) > 1:
        c = 'COFFEES'

    #### sum price data stored stored in sc[2] ########################
    coffee_total = sum(sc[2])
    tip_total = coffee_total * tip
    order_total = round(coffee_total + tip_total, 2)

    print('\n|||||||||||| COFFEE SHOP ORDERS |||||||||||||||\n')
    print(f'\n----------- YOU ORDERED {len(sc[3])} {c} ---------------')

    #### display formatted orders stored in sc[3] #####################
    for i in range(len(sc[3])):
        print(f'\n      ORDER {i + 1}:\n')
        for key, value in sc[3][i].items():
            print(f'            {key}: {value}')

    print(f'\nCOFFEE: ${float(coffee_total)}0')
    print(f'TIP: ${float(round(tip_total, 2))}\n')
    print(f'ORDER TOTAL: ${order_total}\n')

    while True:
        try:
            #### display options and hand handle exceptions #########
            print('------------ ORDER ANOTHER COFFEE? --------------')
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
