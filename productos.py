import os

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
    def __init__(self, product_id, product_name, product_price, product_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

class Client:
    def __init__(self):
        self.client_id = None
        self.client_name = None
        self.client_email = None
        self.client_password = None
        self.client_address = None

class Cart:
    def __init__(self):
        self.head = None

    def add_product(self, product, quantity):
        product_copy = Product(product.product_id, product.product_name, product.product_price, quantity)
        new_node = Node(product_copy)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
            
    def view_cart(self):
        if not self.head:
            print("Your cart is empty.")
            return

        total_price = 0
        current = self.head
        print("\n╔════════════════════════════════════════════════════╗")
        print("║" + "Your Cart".center(52) + "║")
        print("╠═════════════════════════════╦══════════╦═══════════╣")
        print("║ Product Name                ║ Quantity ║ Price     ║")
        print("╠═════════════════════════════╬══════════╬═══════════╣")
        while current:
            product = current.data
            quantity = product.product_quantity
            price = product.product_price
            total_price += price * quantity
            print(f"║ {product.product_name.ljust(27)} ║ {str(quantity).ljust(8)} ║ ${price * quantity:.2f}{' '.rjust(5)}║")
            current = current.next_node
        print("╠═════════════════════════════╩══════════╩═══════════╣")
        print(f"║ {'Total Price:'.ljust(40)} ${total_price:.2f}{' '.rjust(5)}║")
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
            print("Your cart is empty.")
            return

        current = self.head
        product_list = []
        while current:
            product_list.append(current.data)
            current = current.next_node

        print("Products in your cart:")
        for i, product in enumerate(product_list, 1):
            print(f"{i}. {product.product_name} - Quantity: {product.product_quantity}")

        while True:
            choice = input("Enter the number of the product you want to remove (or 0 to go back): ")
            if choice == "0":
                return
            elif choice.isdigit():
                product_index = int(choice) - 1
                if 0 <= product_index < len(product_list):
                    break
                else:
                    print("Invalid product number. Please enter a valid number.")
            else:
                print("Invalid input. Please enter a number.")

        product_to_remove = product_list[product_index]
        while True:
            quantity_to_remove = input(f"Enter the quantity to remove for {product_to_remove.product_name}: ")
            if quantity_to_remove.isdigit():
                quantity_to_remove = int(quantity_to_remove)
                if quantity_to_remove >= product_to_remove.product_quantity:
                    self.remove_entire_product(product_to_remove)
                    print(f"{product_to_remove.product_name} removed from your cart.")
                    break
                elif quantity_to_remove > 0:
                    product_to_remove.product_quantity -= quantity_to_remove
                    print(f"{quantity_to_remove} units of {product_to_remove.product_name} removed from your cart.")
                    break
                else:
                    print("Invalid quantity. Please enter a valid quantity.")
            else:
                print("Invalid input. Please enter a number.")

        print("Process completed successfully.")

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
            product_price = float(data[-2])
            product_quantity = int(data[-1])
            
            current_category = employee.find_category(category_id)
            if not current_category:
                current_category = Category(category_id, category_name)
                employee.add_category(current_category)
            
            new_product = Product(product_id, product_name, product_price, product_quantity)
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
    
    # exportamos el inventario para uso del cliente
    categories = employee_main()
    
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
            # Checkout
            pass
        
        elif choice == "4":
            # Exit without buying
            exit_without_buying()
            
        else:
            # Invalid choice
            print("Invalid choice. Please enter a valid option.")

def show_main_menu():
    print(("\n               Welcome to the store!\n\n").upper())
    print("\n╔══════════════════════════════════════════════════╗")
    print("║                    MAIN  MENU                    ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║   1. Show categories                             ║")
    print("║   2. Cart menu                                   ║")
    print("║   3. Checkout                                    ║")
    print("║   4. Exit without buying                         ║")
    print("╚══════════════════════════════════════════════════╝")

def show_categories(categories):
    printed_categories = set()
    print("\n╔══════════════════════════════════════════════════╗")
    print("║             AVAILABLE CATEGORIES                 ║")
    print("╠══════════════════════════════════════════════════╣")
    current_category = categories.head
    while current_category:
        if current_category.data.category_name not in printed_categories:
            print(f"║ {current_category.data.category_id}. {current_category.data.category_name.ljust(40)}      ║")
            printed_categories.add(current_category.data.category_name)
        current_category = current_category.next_node
    print("╚══════════════════════════════════════════════════╝")
    
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
                print("Invalid category number. Please enter a valid category number.")
        else:
            print("Invalid input. Please enter a number.")
    
    chosen_category = find_category_by_id(categories, category_choice)
    if chosen_category:
        show_products_in_category(chosen_category, client_cart)
    else:
        print("Category not found.")

def find_category_by_id(categories, category_id):
    current_category = categories.head
    while current_category:
        if current_category.data.category_id == category_id:
            return current_category.data
        current_category = current_category.next_node
    return None

def show_products_in_category(category, client_cart):
    clear_screen()
    print("╔══════════════════════════════════════════════════╗")
    print(f"║ {((f"{category.category_name}").upper()).center(48)} ║")
    print("╠════╦════════════════════════╦════════════╦═══════╣")
    print("║ ID ║ Product Name".ljust(30) + "║ Stock".ljust(13) + "║ Price ║")
    print("╠════╬════════════════════════╬════════════╬═══════╣")
    
    current_product = category.products.head
    while current_product:
        product = current_product.data
        product_id = str(product.product_id)
        product_name = product.product_name
        stock = str(product.product_quantity)
        price = str(product.product_price)
        print(f"║ {product_id.ljust(3)}║ {product_name.ljust(23)}║ {stock.ljust(11)}║ ${price.ljust(5)}║")
        current_product = current_product.next_node
    
    print("╚════╩════════════════════════╩════════════╩═══════╝")
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
                print("Invalid product number. Please enter a valid product number.")
        else:
            print("Invalid input. Please enter a number.")

def print_product(product):
    print("Product ID:", product.product_id)
    print("Product Name:", product.product_name)
    print("Product Price:", product.product_price)
    print("Product Quantity:", product.product_quantity)

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
                    
                    category.modify_product_quantity(name, quantity)
                    
                    wait_for_key()
                    break
                else:
                    print("Invalid quantity. Please enter a valid quantity.")
            else:
                print("Invalid input. Please enter a number.")

def show_cart_menu():
    print("\n╔══════════════════════════════════════════════════╗")
    print("║                    CART  MENU                    ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║   1. View Cart                                   ║")
    print("║   2. Remove Item                                 ║")
    print("║   3. Clear Cart                                  ║")
    print("╚══════════════════════════════════════════════════╝")

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
            print("Invalid choice. Please enter a valid option.")

def print_category(category):
    print("\n" + "=" * 50)
    print(f"Category: {category.category_name}")
    print("=" * 50)
    print("\nID  |  Product Name            |  Stock  |  Price")
    print("-" * 50)
    current_product = category.products.head
    while current_product:
        product = current_product.data
        print(f"{str(product.product_id).ljust(3)} | {product.product_name.ljust(25)} | {str(product.product_quantity).ljust(7)} | ${str(product.product_price)}")
        current_product = current_product.next_node
    print("=" * 50)

def checkout():
    print("\nCheckout options:")
    # Opciones de pago aquí
                    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_key():
    input("\n* Press Enter to continue...")
    
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
    1) irte sin pagar
    2) pagar en efectivo
    3) pagar con tarjeta
    4) pagar con qr
    5) pagar con tarjeta y efectivo
    6) otros metodos
4. irte sin comprar nada 
"""