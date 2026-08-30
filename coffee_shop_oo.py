################################################
################# COFFEE SHOP ##################
##### Matt Heerspink ###########################
##### 08/29/2026 ###############################
#### REFACTORED - Object Oriented Style ########
################################################

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class CoffeeSize(Enum):
    SMALL = 2.0
    MEDIUM = 3.0
    LARGE = 4.0


class CoffeeType(Enum):
    BREWED = 0.0
    ESPRESSO = 0.5
    COLD_BREW = 1.0


class Flavoring(Enum):
    NONE = (0.0, 0)
    HAZELNUT = (0.5, 1)
    VANILLA = (0.5, 2)
    CARAMEL = (0.5, 3)
    
    @property
    def price(self):
        return self.value[0]


@dataclass
class Order:
    """Represents a single coffee order"""
    order_id: int
    size: CoffeeSize
    coffee_type: CoffeeType
    flavoring: Flavoring
    tip_rate: float = 0.15
    
    @property
    def subtotal(self) -> float:
        return self.size.value + self.coffee_type.value + self.flavoring.price
    
    @property
    def tip_amount(self) -> float:
        return round(self.subtotal * self.tip_rate, 2)
    
    @property
    def total(self) -> float:
        return round(self.subtotal + self.tip_amount, 2)
    
    def display(self) -> str:
        """Format order for display"""
        return f"""
      ORDER {self.order_id}:
            size: {self.size.name.lower()}
            coffee: {self.coffee_type.name.lower()}
            flavoring: {self.flavoring.name.lower()}
            _coffee: ${self.subtotal:.2f}
            _tip: ${self.tip_amount:.2f}
            _total: ${self.total:.2f}"""


class Menu:
    """Manages coffee shop menu"""
    
    def __init__(self):
        self.sizes = {
            1: CoffeeSize.SMALL,
            2: CoffeeSize.MEDIUM,
            3: CoffeeSize.LARGE
        }
        self.coffees = {
            1: CoffeeType.BREWED,
            2: CoffeeType.ESPRESSO,
            3: CoffeeType.COLD_BREW
        }
        self.flavorings = {
            1: Flavoring.NONE,
            2: Flavoring.HAZELNUT,
            3: Flavoring.VANILLA,
            4: Flavoring.CARAMEL
        }
    
    def display_price_list(self):
        """Display the complete price list"""
        print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////')
        print('\n------------------- PRICE LIST -------------------\n')
        
        print('   SIZES:')
        for idx, size in self.sizes.items():
            print(f'                {size.name.upper()} - ${size.value:.2f}')
        
        print('\n   COFFEE:')
        for idx, coffee in self.coffees.items():
            print(f'                {coffee.name.upper()} - ${coffee.value:.2f}')
        
        print('\n   FLAVORING:')
        for idx, flavoring in self.flavorings.items():
            print(f'                {flavoring.name.upper()} - ${flavoring.price:.2f}')
        
        print('\n------------------- ORDER COFFEE ------------------\n')
        print('\n |||||||||||||||| COFFEE SHOP ||||||||||||||||||||\n')
    
    def get_user_choice(self, category: str, options: Dict) -> int:
        """Get valid user choice for a category"""
        category_name = category.upper()
        print(f'\n------------------- CHOOSE {category_name} ------------------\n')
        print(f'    Choose a {category}...\n')
        
        for idx, option in options.items():
            if hasattr(option, 'price'):
                value = option.price
            else:
                value = option.value
            print(f'        {idx} - {option.name.upper()} --> ${value:.2f}')
        
        quit_option = len(options) + 1
        print(f'        {quit_option} - Quit!')
        print(f'\n------------------- CHOOSE {category_name} ------------------\n')
        
        while True:
            try:
                user_input = int(input())
                
                if user_input == quit_option:
                    return None
                
                if user_input in options:
                    return user_input
                else:
                    print(f'\nEnter a value between 1 and {quit_option}')
                    continue
            except ValueError:
                print('\nPlease enter a valid choice...')
                continue


class CoffeeShop:
    """Main coffee shop application"""
    
    def __init__(self, tip_rate: float = 0.15):
        self.menu = Menu()
        self.orders: List[Order] = []
        self.tip_rate = tip_rate
        self.order_counter = 0
    
    def run(self):
        """Start the coffee shop application"""
        self.menu.display_price_list()
        self._order_loop()
    
    def _order_loop(self):
        """Iterative loop for taking orders"""
        while True:
            if not self._take_order():
                break
    
    def _take_order(self) -> bool:
        """Process a single order. Returns True if user wants to order again, False otherwise"""
        # Get size
        size_choice = self.menu.get_user_choice('size', self.menu.sizes)
        if size_choice is None:
            print('\nYou chose: Quit - Goodbye!')
            return False
        
        size = self.menu.sizes[size_choice]
        print(f'\nYou chose: {size_choice} - {size.name.upper()}\n--> ${size.value:.2f} added to ORDER TOTAL')
        
        # Get coffee type
        coffee_choice = self.menu.get_user_choice('coffee', self.menu.coffees)
        if coffee_choice is None:
            print('\nYou chose: Quit - Goodbye!')
            return False
        
        coffee = self.menu.coffees[coffee_choice]
        print(f'\nYou chose: {coffee_choice} - {coffee.name.upper()}\n--> ${coffee.value:.2f} added to ORDER TOTAL')
        
        # Get flavoring
        flavoring_choice = self.menu.get_user_choice('flavoring', self.menu.flavorings)
        if flavoring_choice is None:
            print('\nYou chose: Quit - Goodbye!')
            return False
        
        flavoring = self.menu.flavorings[flavoring_choice]
        print(f'\nYou chose: {flavoring_choice} - {flavoring.name.upper()}\n--> ${flavoring.price:.2f} added to ORDER TOTAL')
        
        # Create and store order
        self.order_counter += 1
        order = Order(
            order_id=self.order_counter,
            size=size,
            coffee_type=coffee,
            flavoring=flavoring,
            tip_rate=self.tip_rate
        )
        self.orders.append(order)
        
        # Display summary and ask for more
        self._display_orders_summary()
        return self._ask_for_more_coffee()
    
    def _display_orders_summary(self):
        """Display all orders and totals"""
        order_word = 'COFFEE' if len(self.orders) == 1 else 'COFFEES'
        
        print('\n|||||||||||| COFFEE SHOP ORDERS |||||||||||||||\n')
        print(f'\n----------- YOU ORDERED {len(self.orders)} {order_word} ---------------')
        
        for order in self.orders:
            print(order.display())
        
        # Calculate totals
        total_coffee = sum(order.subtotal for order in self.orders)
        total_tips = sum(order.tip_amount for order in self.orders)
        order_total = sum(order.total for order in self.orders)
        
        print(f'\nCOFFEE: ${total_coffee:.2f}')
        print(f'TIP: ${total_tips:.2f}\n')
        print(f'ORDER TOTAL: ${order_total:.2f}\n')
    
    def _ask_for_more_coffee(self) -> bool:
        """Ask if user wants to order more coffee. Returns True if YES, False if NO"""
        while True:
            try:
                print('------------ ORDER ANOTHER COFFEE? --------------')
                user_input = int(input('Order more coffee...\n1 - YES\n2 - NO\n'))
                
                if user_input == 2:
                    print('Quit - Goodbye!')
                    return False
                elif user_input == 1:
                    return True
                else:
                    print(f'\nEnter a value between 1 and 2')
                    continue
            except ValueError:
                print('\nPlease enter a valid choice...')
                continue


if __name__ == '__main__':
    shop = CoffeeShop(tip_rate=0.15)
    shop.run()
