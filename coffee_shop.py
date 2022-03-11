################################################
################# COFFEE SHOP ##################
##### Matt Heerspink ###########################
##### 03/11/2022 ###############################
################################################

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
message = ''

order = {}
orders = []
totals = []


def start_price_list():
    ##### start the price list and display results ###########################
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////')
    print('\n--------------------PRICE LIST--------------------\n')
    for i in range(len(x)):
        print(f'{y[i]}: {x[i]}')
    print('\n--------------------ORDER COFFEE-------------------\n')
    print('\n   ||||||||||||| COFFEE SHOP |||||||||||||||||')

    return order_coffee()


def order_coffee():
    ### order coffee - loop choices and prices ##########
    for i in range(len(x)):
        next_choice = x[i]
        choices = [key for key in next_choice.keys()]
        price = [value for value in next_choice.values()]
        ## display multiple choices and prices ##########
        while True:
            print(f'\nChoose a {y[i]}...\n')
            ## display choice and price lists ###########
            for j in range(len(next_choice)):
                print(f'{j+1} - {choices[j]} --> ${float(price[j])}0')
            print(f'{len(next_choice) + 1} - quit\n')
            ## handle input exceptions ##################
            try:
                s_input = int(input())
                if s_input == len(next_choice) + 1:
                    message = f'\nYou chose: {s_input} - Quit: Goodbye!'

                    return print(message)
                else:
                    ## store orders form input ##########
                    if s_input != 0:
                        message = f'{s_input} - {choices[s_input - 1]}'
                        user_choice = {
                            f'{choices[s_input - 1]}': price[s_input - 1]}
                        order.update(user_choice)
                        totals.append(price[s_input - 1])
                        ## display confirmation ######## 
                        print(
                            f'\nYou chose: {message}\n${float(price[s_input - 1])}0 added to order_total')
                        break
            except:
                print('\nPlease enter a valid choice...')
                continue
            if s_input == 0:
                print(f'\nEnter a value between 1 and 4')
                continue
            break

    return calculate_total()


def calculate_total():
    coffeez = 'COFFEE'
    if len(orders) != 0:
        coffeez = 'COFFEES'
    ## calculate orders ##
    orders.append([order])
    coffee_total = float(sum(totals))
    tip_amount = round(coffee_total * tip, 2)
    total = round(coffee_total + tip_amount, 2)
    ## display confirmation messages ###############################################
    order_summary = f'Coffee: ${coffee_total}0\nTip: ${tip_amount}\n\nTotal: ${total}'
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////')
    print(f'\n------------YOU ORDERED {len(orders)} {coffeez}----------------')
    print(f'\nCoffees Ordered: {len(orders)}\n')
    print(f'{order_summary}\n')
    print('-------------ORDER ANOTHER COFFEE?---------------')
    print('\n   ||||||||||||| COFFEE SHOP |||||||||||||||||')

    return order_coffee()


start_price_list()
