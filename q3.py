# q3_shopping_cart.py

# PART A

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))

# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']

# Explanation:
# The default list is created only once.
# So the same list is reused in later function calls.


# PART B

def add_item_fixed(item, cart=None):

    if cart == None:
        cart = []

    cart.append(item)

    return cart

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))


# PART C

def create_cart(owner, discount=0):

    cart = {
        "owner": owner,
        "items": [],
        "discount": discount
    }

    return cart


def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):

    try:
        price_tuple[1] = new_price

    except TypeError:
        print("Tuple cannot be modified")


def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total = total + (item["price"] * item["qty"])

    discount = (cart["discount"] / 100) * total

    final_total = total - discount

    return final_total


cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Riya", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 1000, 1)

print("\nCart 1")
print(cart1)

print("\nCart 2")
print(cart2)

print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))

price_data = ("Laptop", 50000)

update_price(price_data, 45000)


# Discussion Points

# discount=0 is safe because int is immutable.
# cart=[] is dangerous because list is mutable.

# Rebinding means assigning a new object.
# Mutating means changing the existing object.

# Mutable:
# list, dict, set

# Immutable:
# tuple, str, int

# If a list is passed into a function and modified,
# the changes reflect outside because lists are mutable.