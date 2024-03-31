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
                current_product.data.product_quantity -= quantity
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
        self.head = None  # Head of the linked list

    def add_product(self, product):
        new_node = Node(product)  # Create a new node
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node  # Append the new node to the end of the list

    def modify_quantity(self, product_name, quantity):
        current = self.head
        while current:
            if current.data.product_name == product_name:
                current.data.product_quantity = quantity
                break
            current = current.next_node
            
    def remove_product(self, product):
        current = self.head
        prev = None
        while current:
            if current.data["product"] == product:
                if prev:
                    prev.next_node = current.next_node
                else:
                    self.head = current.next_node
                return  # Exit the function after removing the product
            prev = current
            current = current.next_node
        print("Product not found in cart.")
        return  # Added to exit the function if the product is not found

    def view_cart(self):
        if not self.head:
            print("Your cart is empty.")
            return

        total_price = 0
        current = self.head
        print("\n╔══════════════════════════════════════════════════╗")
        print("║                   Your Cart                       ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║ Product Name                | Quantity | Price     ║")
        print("╠════════════════════════════╦══════════╦═══════════╣")
        while current:
            product = current.data
            quantity = product.product_quantity
            price = product.product_price
            print(f"║ {product.product_name.ljust(27)} │ {str(quantity).ljust(8)} │ ${price * quantity:.2f} ║")
            total_price += price * quantity
            current = current.next_node
        print("╠════════════════════════════╩══════════╩═══════════╣")
        print(f"║           Total Price: ${total_price:.2f}          ║")
        print("╚══════════════════════════════════════════════════╝")

class Order:
    def __init__(self, client, cart):
        self.client = client
        self.cart = cart
        self.order_id = None
        self.order_status = None
        self.order_details = None

    def place_order(self):
        # Implementar lógica para realizar el pedido
        pass

    def cancel_order(self):
        # Implementar lógica para cancelar el pedido
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
            product_quantity = float(data[-1])
            
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
    
    # imprimir inventario de prueba
    # print_inventory(categories)
    
    return categories
    
def client_main():
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
        show_main_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Show categories
            show_categories(categories)
            access_category(categories, client_cart)
            
        elif choice == "2":
            # Cart menu
            #show_cart()
            pass
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
    print("\n╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║              Welcome to the store!               ║")
    print("║                                                  ║")
    print("║                  Main Menu:                      ║")
    print("║                                                  ║")
    print("║         1. Show categories                       ║")
    print("║                                                  ║")
    print("║         2. Cart menu                             ║")
    print("║                                                  ║")
    print("║         3. Checkout                              ║")
    print("║                                                  ║")
    print("║         4. Exit without buying                   ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")

def show_categories(categories):
    printed_categories = set()  # Set to keep track of printed categories
    print("\n╔══════════════════════════════════════════════════╗")
    print("║             Available Categories                 ║")
    print("╠══════════════════════════════════════════════════╣")
    current_category = categories.head
    while current_category:
        if current_category.data.category_name not in printed_categories:
            print(f"║ {current_category.data.category_id}. {current_category.data.category_name.ljust(40)}      ║")
            printed_categories.add(current_category.data.category_name)  # Add printed category to the set
        current_category = current_category.next_node
    print("╚══════════════════════════════════════════════════╝")
    
def access_category(categories, client_cart):
    while True:
        category_choice = input("Enter the category number you want to access (or 0 to go back to the main menu): ")
        
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
    print("╔══════════════════════════════════════════════════╗")
    print(f"║ {(f"Products in {category.category_name}").center(48)} ║")
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
        choice = input("\nEnter the product number you want to add to cart (or 0 to go back): ")
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
            quantity = input("Enter the quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= chosen_product.product_quantity:
                    name = chosen_product.product_name
                    
                    client_cart.add_product(chosen_product)
                    
                    client_cart.modify_quantity(name, quantity)
                    
                    print(f"{quantity} {name} added to cart.")
                    
                    category.modify_product_quantity(name, quantity)
                    
                    print(f"Se actualizo: {name} {chosen_product.product_quantity} unidades menos")
                    
                    break
                else:
                    print("Invalid quantity. Please enter a valid quantity.")
            else:
                print("Invalid input. Please enter a number.")

def exit_without_buying():
    print("You have chosen to exit without buying anything. Goodbye!")
    exit()







def show_cart_menu():
    print("\n╔════════════════════════════════════════╗")
    print("║               Cart Menu                 ║")
    print("╠════════════════════════════════════════╣")
    print("║   1. View Cart                          ║")
    print("║   2. Remove Item                        ║")
    print("║   3. Clear Cart                         ║")
    print("║   4. Back                               ║")
    print("╚════════════════════════════════════════╝")

def remove_item_from_cart(cart):
    item_to_remove = input("Enter the product to remove: ")
    cart.remove_from_cart(item_to_remove)

def clear_cart(cart):
    cart.clear()

def checkout():
    print("\nCheckout options:")
    # Opciones de pago aquí
                    


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