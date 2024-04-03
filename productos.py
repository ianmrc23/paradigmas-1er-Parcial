from abc import ABC, abstractmethod
import os

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(PaymentMethod):
    def process_payment(self, amount):
        return amount

class CardPayment(PaymentMethod):
    def process_payment(self, amount):
        return amount * 0.7

class QRPayment(PaymentMethod):
    def process_payment(self, amount):
        return amount * 0.9
 
def process_payment(payment_method, total_amount):
    return payment_method.process_payment(total_amount)

class ShippingMethod(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, weight, distance_from_store):
        pass

class StandardShipping(ShippingMethod):
    def calculate_shipping_cost(self, weight, distance_from_store):
        return 5 + weight * 0.5 + distance_from_store * 0.1

class ExpressShipping(ShippingMethod):
    def calculate_shipping_cost(self, weight, distance_from_store):
        return 10 + weight * 1.0 + distance_from_store * 0.2

class InStorePickup(ShippingMethod):
    def calculate_shipping_cost(self, weight, distance_from_store):
        return 0

def calculate_shipping(shipping_method, weight, distance_from_store):
    return shipping_method.calculate_shipping_cost(weight, distance_from_store)

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  # Add an attribute to track the size of the list

    def is_empty(self):
        return self.head is None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        self.size += 1  # Increment the size of the list

    def remove(self, data):
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        if current_node:
            if previous_node:
                previous_node.next_node = current_node.next_node
            else:
                self.head = current_node.next_node
            self.size -= 1  # Decrement the size of the list

    def print_list(self):
        current_node = self.head
        if not current_node:
            print("The list is empty")
        else:
            print("List content:")
            index = 1
            while current_node:
                print(f"{index}. {current_node.data}")
                current_node = current_node.next_node
                index += 1

class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        self.products = LinkedList()
        
    def modify_product_quantity(self, product_name, quantity):
        current_product = self.products.head
        while current_product:
            if current_product.data.product_name == product_name:
                print(f"\n\n* Additional Information About Product Stock in Inventory")
                print(f"\n* Modifying quantity of {product_name}:")
                print(f"\n* Current quantity: {current_product.data.product_quantity}")
                print(f"\n* Quantity to subtract: {quantity}")
                current_product.data.product_quantity -= quantity
                print(f"\n* New quantity: {current_product.data.product_quantity}")
                break
            current_product = current_product.next_node

class Product:
    def __init__(self, product_id, product_name, product_price, product_quantity, product_weight):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_weight = product_weight

class Client:
    def __init__(self):
        self.client_id = None
        self.client_name = None
        self.client_email = None
        self.client_password = None
        self.client_address = None
        self.cliente_distance_from_store = None

class Cart:
    def __init__(self):
        self.head = None

    def add_product(self, product, quantity):
        product_copy = Product(product.product_id, product.product_name, product.product_price, quantity, product.product_weight)
        new_node = Node(product_copy)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
    
    def calculate_totals(self):
        total_price = 0
        total_weight = 0
        current = self.head
        while current:
            product = current.data
            quantity = product.product_quantity
            price = product.product_price
            weight = product.product_weight
            total_price += price * quantity
            total_weight += weight * quantity
            current = current.next_node
        return total_price, total_weight
          
    def view_cart(self):
        if not self.head:
            print("Your cart is empty.")
            return

        total_price, total_weight = self.calculate_totals()
        total_price = "{:.2f}".format(total_price)
        total_weight = "{:.2f}".format(total_weight)
        
        print("\n╔════════════════════════════════════════════════════╗")
        print("║" + "Your Cart".center(52) + "║")
        print("╠══════════════════════╦════════════╦════════════════╣")
        print("║ Product Name         ║  Quantity  ║      Price     ║")
        print("╠══════════════════════╬════════════╬════════════════╣")
        current = self.head
        while current:
            product = current.data
            quantity = product.product_quantity
            price = round(product.product_price * quantity, 2)
            print(f"║ {product.product_name.ljust(20)} ║  {str(quantity).ljust(9)} ║ $ {str(price).ljust(12)} ║")
            current = current.next_node
        print("╠══════════════════════╩════════════╩════════════════╣")
        print(f"║ {'Total Price:'.ljust(35)} $ {total_price.ljust(12)} ║")
        print(f"║ {'Total Weight:'.ljust(35)}Kg {total_weight.ljust(12)} ║")
        print("╚════════════════════════════════════════════════════╝")

    def clear_cart(self):
        if not self.head:
            print("\n* Your cart is already empty.")
            return

        print("\n* Clearing your cart...")
        current = self.head
        while current:
            product_name = current.data.product_name
            print(f"\n* Removing {product_name} from your cart.")
            current = current.next_node

        # Clearing the cart by setting the head to None
        self.head = None
        print("\n* Your cart has been successfully cleared.")
    
    def remove_product(self):
        if not self.head:
            print("\n* Your cart is empty.")
            return

        current = self.head
        product_list = []
        while current:
            product_list.append(current.data)
            current = current.next_node

        print("\n* Products in your cart:")
        for i, product in enumerate(product_list, 1):
            print(f"\n{i}. {product.product_name} - Quantity: {product.product_quantity}")

        while True:
            choice = input("\n* Enter the number of the product you want to remove (or 0 to go back): ")
            if choice == "0":
                return
            elif choice.isdigit():
                product_index = int(choice) - 1
                if 0 <= product_index < len(product_list):
                    break
                else:
                    print("\n* Invalid product number. Please enter a valid number.")
            else:
                print("\n* Invalid input. Please enter a number.")

        product_to_remove = product_list[product_index]
        while True:
            quantity_to_remove = input(f"\n* Enter the quantity to remove for {product_to_remove.product_name}: ")
            if quantity_to_remove.isdigit():
                quantity_to_remove = int(quantity_to_remove)
                if quantity_to_remove >= product_to_remove.product_quantity:
                    self.remove_entire_product(product_to_remove)
                    print(f"\n* {product_to_remove.product_name} removed from your cart.")
                    break
                elif quantity_to_remove > 0:
                    product_to_remove.product_quantity -= quantity_to_remove
                    print(f"\n* {quantity_to_remove} units of {product_to_remove.product_name} removed from your cart.")
                    break
                else:
                    print("\n* Invalid quantity. Please enter a valid quantity.")
            else:
                print("\n* Invalid input. Please enter a number.")

        print("\n* Process completed successfully.")

    def remove_entire_product(self, product):
        current = self.head
        previous = None
        while current:
            if current.data == product:
                if previous:
                    previous.next_node = current.next_node
                else:
                    self.head = current.next_node
                return
            previous = current
            current = current.next_node

class Order:
    def __init__(self, client, cart):
        self.client = client
        self.cart = cart
        self.order_id = None
        self.order_status = None
        self.order_details = None

    def place_order(self):
        pass

    def cancel_order(self):
        pass

class Employee:
    def __init__(self):
        self.employee_id = None
        self.employee_name = None
        self.employee_role = None
        self.categories = LinkedList()

    def add_category(self, category):
        self.categories.add_to_end(category)

    def add_product_to_category(self, category_name, product):
        current_category = self.find_category(category_name)
        if current_category:
            current_category.products.add_to_end(product)

    def find_category(self, category_id):
        current = self.categories.head
        while current:
            if current.data.category_id == category_id:
                return current.data
            current = current.next_node
        return None

def read_inventory(file_path):
    employee = Employee()
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split()
            category_id = int(data[0])
            category_name = data[1]
            product_id = int(data[2])
            product_name = data[3]
            product_price = float(data[-3])  # Índice -3 para el precio
            product_quantity = int(data[-2])  # Índice -2 para la cantidad
            product_weight = float(data[-1])  # Índice -1 para el peso
            
            current_category = employee.find_category(category_id)
            if not current_category:
                current_category = Category(category_id, category_name)
                employee.add_category(current_category)
            
            new_product = Product(product_id, product_name, product_price, product_quantity, product_weight)
            current_category.products.add_to_end(new_product)
    
    return employee.categories

def print_inventory(categories):
    current_category = categories.head

    while current_category:
        category = current_category.data
        print(f"{category.category_name}:")
        
        current_product = category.products.head
        while current_product:
            product = current_product.data
            print(f"- {product.product_name}: Price: ${product.product_price:.2f}, Stock: {product.product_quantity}")
            current_product = current_product.next_node
        
        current_category = current_category.next_node                    

def employee_main():
    employee = Employee()
    employee.employee_id = 1
    employee.employee_name = "John Doe"
    employee.employee_role = "Clerk"

    # empleado automatico
    categories = read_inventory("inventory.txt")
    
    # modo empleado
    # falta implementar

    return categories
    
def client_main():
    clear_screen()
    # Crear un cliente
    client = Client()
    client_cart = Cart()
    
    client.client_id = 1
    client.client_name = "Alice"
    client.client_email = "alice@example.com"
    client.client_password = "password123"
    client.client_distance_from_store = 5
    
    # exportamos el inventario para uso del cliente
    categories = employee_main()
    
    print(("\n               Welcome to the store!\n\n").upper())
    while True:
        clear_screen()
        show_main_menu()
        
        choice = input("\n* Enter your choice: ")
        
        if choice == "1":
            clear_screen()
            # Show categories
            show_categories(categories)
            access_category(categories, client_cart)
            
        elif choice == "2":
            clear_screen()
            # Cart menu
            cart_menu(client_cart)
        elif choice == "3":
            clear_screen()
            # Checkout
            checkout_menu(client, client_cart)
            
            pass
        
        elif choice == "4":
            # Exit without buying
            exit_without_buying()
            
        else:
            # Invalid choice
            print("\n* Invalid choice. Please enter a valid option.")
            wait_for_key()

def show_main_menu():
    print("\n╔════════════════════════════════════════════════════╗")
    print("║                     MAIN  MENU                     ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║   1. Show categories                               ║")
    print("║   2. Cart menu                                     ║")
    print("║   3. Checkout                                      ║")
    print("║   4. Exit without buying                           ║")
    print("╚════════════════════════════════════════════════════╝")

def show_categories(categories):
    printed_categories = set()
    print("\n╔════════════════════════════════════════════════════╗")
    print("║               AVAILABLE CATEGORIES                 ║")
    print("╠════════════════════════════════════════════════════╣")
    current_category = categories.head
    while current_category:
        if current_category.data.category_name not in printed_categories:
            print(f"║ {current_category.data.category_id}. {current_category.data.category_name.ljust(42)}      ║")
            printed_categories.add(current_category.data.category_name)
        current_category = current_category.next_node
    print("╚════════════════════════════════════════════════════╝")
    
def access_category(categories, client_cart):
    while True:
        category_choice = input("\n* Enter the category number you want to access (or 0 to go back to the main menu): ")
        
        if category_choice == "0":
            return
        elif category_choice.isdigit():
            category_choice = int(category_choice)
            if 0 < category_choice <= categories.size:
                break
            else:
                print("\n* Invalid category number. Please enter a valid category number.")
        else:
            print("\n* Invalid input. Please enter a number.")
    
    chosen_category = find_category_by_id(categories, category_choice)
    if chosen_category:
        show_products_in_category(chosen_category, client_cart)
    else:
        print("\n* Category not found.")

def find_category_by_id(categories, category_id):
    current_category = categories.head
    while current_category:
        if current_category.data.category_id == category_id:
            return current_category.data
        current_category = current_category.next_node
    return None

def show_products_in_category(category, client_cart):
    clear_screen()
    print("╔════════════════════════════════════════════════════╗")
    print(f"║ {((f"{category.category_name}").upper()).center(50)} ║")
    print("╠════╦══════════════════════════╦════════════╦═══════╣")
    print("║ ID ║ Product Name".ljust(32) + "║ Stock".ljust(13) + "║ Price ║")
    print("╠════╬══════════════════════════╬════════════╬═══════╣")
    
    current_product = category.products.head
    while current_product:
        product = current_product.data
        product_id = str(product.product_id)
        product_name = product.product_name
        stock = str(product.product_quantity)
        price = str(product.product_price)
        print(f"║ {product_id.ljust(3)}║ {product_name.ljust(25)}║ {stock.ljust(11)}║ ${price.ljust(5)}║")
        current_product = current_product.next_node
    
    print("╚════╩══════════════════════════╩════════════╩═══════╝")
    handle_product_selection(category, client_cart)
    
def handle_product_selection(category, client_cart):
    while True:
        choice = input("\n* Enter the product number you want to add to cart (or 0 to go back): ")
        if choice == "0":
            return
        elif choice.isdigit():
            product_number = int(choice)
            if 0 < product_number <= category.products.size:
                add_product_to_cart(category, product_number, client_cart)
                break
            else:
                print("\n* Invalid product number. Please enter a valid product number.")
        else:
            print("\n* Invalid input. Please enter a number.")

def print_product_table(product):
    id = product.product_id
    name = product.product_name
    price = round(product.product_price, 2)
    quantity = product.product_quantity
    print("\n╔════════════════════════════════════════════════════╗")
    print("║                 Product Information                ║")
    print("╠════════════════════╦═══════════════════════════════╣")
    print("║      Attribute     ║             Value             ║")
    print("╠════════════════════╬═══════════════════════════════╣")
    print(f"║  Product ID        ║         {str(id).ljust(21)} ║")
    print(f"║  Product Name      ║         {name.ljust(21)} ║")
    print(f"║  Product Price ($) ║         {str(price).ljust(21)} ║")
    print(f"║  Product Quantity  ║         {str(quantity).ljust(21)} ║")
    print("╚════════════════════╩═══════════════════════════════╝")

def add_product_to_cart(category, product_number, client_cart):
    current_product = category.products.head
    chosen_product = None
    while current_product:
        if current_product.data.product_id == product_number:
            chosen_product = current_product.data
            break
        current_product = current_product.next_node
    
    if chosen_product:
        while True:
            quantity = input("\n* Enter the quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= chosen_product.product_quantity:
                    name = chosen_product.product_name
                    client_cart.add_product(chosen_product, quantity)
                    
                    print(f"\n* Added {quantity} {name}(s) to cart.")
                    
                    clear_screen()
                    category.modify_product_quantity(name, quantity)
                    
                    wait_for_key()
                    break
                else:
                    print("\n* Invalid quantity. Please enter a valid quantity.")
            else:
                print("\n* Invalid input. Please enter a number.")

def show_cart_menu():
    print("\n╔════════════════════════════════════════════════════╗")
    print("║                     CART  MENU                     ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║   1. View Cart                                     ║")
    print("║   2. Remove Item                                   ║")
    print("║   3. Clear Cart                                    ║")
    print("╚════════════════════════════════════════════════════╝")

def exit_without_buying():
    print("\n* You have chosen to exit without buying anything. Goodbye!")
    exit()

def cart_menu(client_cart):
    while True:
        clear_screen()
        show_cart_menu()

        choice = input("\n* Enter your choice (or 0 to go back to the main menu): ")
        if choice == '1':
            clear_screen()
            client_cart.view_cart()
            wait_for_key()
        elif choice == '2':
            clear_screen()
            client_cart.remove_product()
            wait_for_key()
        elif choice == '3':
            clear_screen()
            client_cart.clear_cart()
            wait_for_key()
        elif choice == '0':
            break
        else:
            print("\n* Invalid choice. Please enter a valid option.")
            wait_for_key()

def print_category(category_list):
    current_category_node = category_list.head
    while current_category_node:
        current_category = current_category_node.data
        
        print("\n╔════════════════════════════════════════════════════╗")
        print("║" + f"Category: {current_category.category_name}".center(52) + "║")
        print("╠═══════════════════════════════╦══════════╦═════════╣")
        print("║         Product Name          ║  Stock   ║  Price  ║")
        print("╠═══════════════════════════════╬══════════╬═════════╣")
        
        current_product_node = current_category.products.head
        while current_product_node:
            product = current_product_node.data
            price = "{:.2f}".format(product.product_price)
            print(f"║ {product.product_name.ljust(29)} ║ {str(product.product_quantity).ljust(8)} ║ ${price.rjust(6)} ║")
            current_product_node = current_product_node.next_node
        print("╚═══════════════════════════════╩══════════╩═════════╝")
    
        current_category_node = current_category_node.next_node

def show_checkout():
    print("\n╔════════════════════════════════════════════════════╗")
    print("║                   CHECKOUT  MENU                   ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║   1. Pay with Cash                                 ║")
    print("║   2. Pay with Card (30% discount)                  ║")
    print("║   3. Pay with QR (10% discount)                    ║")
    print("╚════════════════════════════════════════════════════╝")

def show_shipping_methods():
    print("\n╔════════════════════════════════════════════════════╗")
    print("║                  SHIPPING METHODS                  ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║   1. Standard Shipping                             ║")
    print("║   2. Express Shipping                              ║")
    print("║   3. In-Store Pickup                               ║")
    print("╚════════════════════════════════════════════════════╝")

def checkout_menu(client, client_cart):
    total_amount, total_weight = client_cart.calculate_totals()
    destination = client.client_distance_from_store
    
    client_cart.view_cart()
    
    while True:
        
        show_checkout()
        
        choice = input("\n* Select payment method (or 0 to go back to the main menu): ")
        if choice == '0':
            return
        elif choice == '1':
            payment_method = CashPayment()
            break
        elif choice == '2':
            payment_method = CardPayment()
            break
        elif choice == '3':
            payment_method = QRPayment()
            break
        else:
            clear_screen()
            client_cart.view_cart()
            print("\n* Invalid payment method. Please enter a valid option.")

    total_with_discount = process_payment(payment_method, total_amount)
    
    clear_screen() 
    client_cart.view_cart()   
    while True:
        
        show_shipping_methods()

        choice = input("\n* Select shipping method (or 0 to go back to the main menu): ")

        if choice == '0':
            return
        elif choice == '1':
            shipping_method = StandardShipping()
            break
        elif choice == '2':
            shipping_method = ExpressShipping()
            break
        elif choice == '3':
            shipping_method = InStorePickup()
            break
        else:
            clear_screen()
            client_cart.view_cart()
            print("\n* Invalid shipping method. Please enter a valid option.")

    clear_screen()
    print(f"\n* Total amount with discount: {total_with_discount:.2f}")
    
    shipping_cost = calculate_shipping(shipping_method, total_weight, destination)
    print(f"\n* Shipping cost: {shipping_cost:.2f}")

    total_amount_with_shipping = total_with_discount + shipping_cost
    print(f"\n* Total amount with discount and shipping: {total_amount_with_shipping:.2f}")
    
    farewell_message()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_key():
    input("\n* Press Enter to continue...")
    
def farewell_message():
    print("\n* Thank you for visiting us! We hope to see you again soon!")
    exit()

if __name__ == "__main__":
    #employee_main()
    client_main()
 
 

"""
1. mostrar categorias
    se muestran todas las categorias
    1) acceder a una categoria x
        se muestran todos los productos
        1) agregar producto x al carrito, agregar cantidad y del producto
        2) retroceder
    2) retroceder
2. menu carrito
    1) ver todo el carrito
    se muestra cada producto con su cantidad y precio unitario y precio total
        1) retroceder
    2) eliminar articulo
        se muestra cada producto con su cantidad 
        1) elegir producto a eliminar y cantidad a eliminar
    3) eliminar todo: elimina todo el carrito
    4) retroceder
3. pagar compra 
    1) irte con todos los productos sin pagar
    2) pagar en efectivo
    3) pagar con tarjeta
    4) pagar con qr
    5) pagar con tarjeta y efectivo
4. irte sin comprar nada 
"""


""" 
Errores a corregir:
1. al eliminar un producto del carrito hay que actualizar de nuevo el stock
2. cambiar el stilo a checkout, no se imprime como tabla
"""