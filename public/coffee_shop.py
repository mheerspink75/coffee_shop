from dataclasses import dataclass
from typing import Dict, List
from enum import Enum
from pyodide.ffi import create_proxy
from js import document


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
        return f"""
      ORDER {self.order_id}:
            size: {self.size.name.lower()}
            coffee: {self.coffee_type.name.lower()}
            flavoring: {self.flavoring.name.lower()}
            _coffee: ${self.subtotal:.2f}
            _tip: ${self.tip_amount:.2f}
            _total: ${self.total:.2f}"""


class Menu:
    def __init__(self):
        self.sizes = {1: CoffeeSize.SMALL, 2: CoffeeSize.MEDIUM, 3: CoffeeSize.LARGE}
        self.coffees = {1: CoffeeType.BREWED, 2: CoffeeType.ESPRESSO, 3: CoffeeType.COLD_BREW}
        self.flavorings = {
            1: Flavoring.NONE,
            2: Flavoring.HAZELNUT,
            3: Flavoring.VANILLA,
            4: Flavoring.CARAMEL,
        }

    def get_price_list(self):
        output = '\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COFFEE SHOP ////////////////////\n'
        output += '\n------------------- PRICE LIST -------------------\n'
        output += '   SIZES:\n'
        for idx, size in self.sizes.items():
            output += f'                {size.name.upper()} - ${size.value:.2f}\n'
        output += '\n   COFFEE:\n'
        for idx, coffee in self.coffees.items():
            output += f'                {coffee.name.upper()} - ${coffee.value:.2f}\n'
        output += '\n   FLAVORING:\n'
        for idx, flavoring in self.flavorings.items():
            output += f'                {flavoring.name.upper()} - ${flavoring.price:.2f}\n'
        output += '\n------------------- ORDER COFFEE ------------------\n'
        output += '\n |||||||||||||||| COFFEE SHOP ||||||||||||||||||||\n'
        return output

    def get_category_options(self, category: str):
        if category == 'size':
            return self.sizes
        elif category == 'coffee':
            return self.coffees
        elif category == 'flavoring':
            return self.flavorings
        return {}

    def format_choices(self, category: str, options: Dict) -> str:
        category_name = category.upper()
        output = f'\n------------------- CHOOSE {category_name} ------------------\n'
        output += f'    Choose a {category}...\n\n'
        for idx, option in options.items():
            value = option.price if hasattr(option, 'price') else option.value
            output += f'        {idx} - {option.name.upper()} --> ${value:.2f}\n'
        quit_option = len(options) + 1
        output += f'        {quit_option} - Quit!\n'
        output += f'\n------------------- CHOOSE {category_name} ------------------\n'
        return output


class CoffeeShop:
    def __init__(self, tip_rate: float = 0.15):
        self.menu = Menu()
        self.orders: List[Order] = []
        self.tip_rate = tip_rate
        self.order_counter = 0
        self.current_state = "start"
        self.current_size = None
        self.current_coffee = None
        self.current_flavoring = None

    def start(self):
        output = self.menu.get_price_list()
        self.output_text(output)
        self.show_choice_buttons("size")

    def show_choice_buttons(self, category: str):
        options = self.menu.get_category_options(category)
        output = self.menu.format_choices(category, options)
        self.output_text(output)
        self.current_state = f"choosing_{category}"
        self.display_buttons(options, category)

    def display_buttons(self, options: Dict, category: str):
        button_container = document.getElementById("button-container")
        button_container.innerHTML = ""

        for idx in sorted(options.keys()):
            option = options[idx]
            btn = document.createElement("button")
            value = option.price if hasattr(option, 'price') else option.value
            btn.textContent = f"{idx} - {option.name.upper()} (${value:.2f})"
            btn.id = f"btn_{category}_{idx}"
            button_container.appendChild(btn)

        quit_btn = document.createElement("button")
        quit_btn.textContent = f"{len(options) + 1} - QUIT"
        quit_btn.style.background = "#ff6b6b"
        quit_btn.id = f"btn_{category}_quit"
        button_container.appendChild(quit_btn)

        for idx in sorted(options.keys()):
            btn = document.getElementById(f"btn_{category}_{idx}")
            btn.addEventListener(
                "click",
                create_proxy(lambda e, idx=idx, cat=category: self.handle_choice(idx, cat)),
            )

        quit_btn = document.getElementById(f"btn_{category}_quit")
        quit_btn.addEventListener(
            "click", create_proxy(lambda e, cat=category: self.handle_quit(cat))
        )

    def handle_choice(self, choice: int, category: str):
        options = self.menu.get_category_options(category)
        if choice not in options:
            self.output_text('\n<span class="error">Invalid choice!</span>', append=True)
            return

        selected = options[choice]
        value = selected.price if hasattr(selected, 'price') else selected.value
        output = f'\n<span class="success">You chose: {choice} - {selected.name.upper()}\n--> ${value:.2f} added to ORDER TOTAL</span>'
        self.output_text(output, append=True)

        if category == "size":
            self.current_size = selected
            self.show_choice_buttons("coffee")
        elif category == "coffee":
            self.current_coffee = selected
            self.show_choice_buttons("flavoring")
        elif category == "flavoring":
            self.current_flavoring = selected
            self.create_order()

    def handle_quit(self, category: str):
        self.output_text('\n<span class="info">You chose: QUIT - Goodbye!</span>', append=True)
        self.reset_shop()

    def create_order(self):
        self.order_counter += 1
        order = Order(
            order_id=self.order_counter,
            size=self.current_size,
            coffee_type=self.current_coffee,
            flavoring=self.current_flavoring,
            tip_rate=self.tip_rate,
        )
        self.orders.append(order)
        self.display_summary()

    def display_summary(self):
        order_word = 'COFFEE' if len(self.orders) == 1 else 'COFFEES'
        output = f"\n|||||||||||| COFFEE SHOP ORDERS |||||||||||||||\n"
        output += f"\n----------- YOU ORDERED {len(self.orders)} {order_word} ---------------"

        for order in self.orders:
            output += order.display()

        total_coffee = sum(order.subtotal for order in self.orders)
        total_tips = sum(order.tip_amount for order in self.orders)
        order_total = sum(order.total for order in self.orders)

        output += f"\n\nCOFFEE: ${total_coffee:.2f}"
        output += f"\nTIP: ${total_tips:.2f}\n"
        output += f"ORDER TOTAL: ${order_total:.2f}\n"

        self.output_text(output, append=True)
        self.show_order_more_buttons()

    def show_order_more_buttons(self):
        button_container = document.getElementById("button-container")
        button_container.innerHTML = ""

        output = "\n------------ ORDER ANOTHER COFFEE? --------------"
        self.output_text(output, append=True)

        yes_btn = document.createElement("button")
        yes_btn.textContent = "1 - YES (Order Another)"
        yes_btn.style.background = "#4caf50"
        yes_btn.id = "btn_yes"
        button_container.appendChild(yes_btn)

        no_btn = document.createElement("button")
        no_btn.textContent = "2 - NO (Exit)"
        no_btn.style.background = "#ff6b6b"
        no_btn.id = "btn_no"
        button_container.appendChild(no_btn)

        document.getElementById("btn_yes").addEventListener(
            "click", create_proxy(lambda e: self.order_another())
        )
        document.getElementById("btn_no").addEventListener(
            "click", create_proxy(lambda e: self.exit_shop())
        )

    def order_another(self):
        self.current_state = "choosing_size"
        self.current_size = None
        self.current_coffee = None
        self.current_flavoring = None
        self.show_choice_buttons("size")

    def exit_shop(self):
        self.output_text(
            '\n<span class="info">Quit - Goodbye! Thanks for your order!</span>', append=True
        )
        self.reset_shop()

    def reset_shop(self):
        button_container = document.getElementById("button-container")
        button_container.innerHTML = ""

        restart_btn = document.createElement("button")
        restart_btn.textContent = "🔄 Start New Order"
        restart_btn.style.background = "#667eea"
        restart_btn.id = "btn_restart"
        button_container.appendChild(restart_btn)

        document.getElementById("btn_restart").addEventListener(
            "click", create_proxy(lambda e: self.start())
        )

    def output_text(self, text: str, append: bool = False):
        output_div = document.getElementById("output")
        if append:
            output_div.innerHTML += text
        else:
            output_div.innerHTML = text
        output_div.scrollTop = output_div.scrollHeight


shop = CoffeeShop(tip_rate=0.15)
shop.start()
