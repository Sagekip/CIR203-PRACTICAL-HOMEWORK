"""
Exercise 4: Dictionaries in E-Commerce (Retail Sector)
Topic: Python Dictionaries
Scenario: An online store manages product inventory using dictionaries.
"""

print("=== Exercise 4: Python Dictionaries in E-Commerce ===\n")

1: Create dictionary with 5 products

print("1. Initial inventory:")
inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 22,
    "Monitor": 8,
    "USB Cable": 100
}
print("   ", inventory)
print()

2: Add new product and update existing one

print("2. Updating inventory:")
inventory["Webcam"] = 30
print("   After adding Webcam:", inventory)
inventory["Monitor"] = 12
print("   After updating Monitor quantity:", inventory)
print()

 3: Function to return products with stock < 10

print("3. Low stock items (less than 10):")
def get_low_stock(inventory_dict, threshold=10):
    return {product: quantity for product, quantity in inventory_dict.items() 
            if quantity < threshold}

low_stock = get_low_stock(inventory)
print("   Low stock items:", low_stock)
print()

 4: Delete discontinued product

print("4. Removing discontinued product:")
if "Mouse" in inventory:
    del inventory["Mouse"]
print("   After removing Mouse:", inventory)
print()

5: Loop through items using .items()

print("5. Current inventory (using .items()):")
print("   Current Stock Levels:")
for product, quantity in inventory.items():
    print(f"   - {product}: {quantity} units")
