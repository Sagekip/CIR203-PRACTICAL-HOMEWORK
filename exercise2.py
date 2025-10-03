"""
Exercise 2: Lists in Logistics Management (Supply Chain Sector)
Topic: Python Lists
Scenario: A logistics company tracks delivery routes and package counts.
"""

print("=== Exercise 2: Python Lists in Logistics Management ===\n")

Task 1: Create list of 10 delivery routes

print("1. Original delivery routes:")
routes = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
print("   ", routes)
print()

Task 2: Append new route and remove discontinued one

print("2. Updating routes:")
routes.append("Nashville")
print("   After adding Nashville:", routes)
routes.remove("Chicago")
print("   After removing Chicago:", routes)
print()

Task 3: Sort alphabetically and reverse

print("3. Sorting and reversing:")
routes.sort()
print("   Sorted alphabetically:", routes)
routes.reverse()
print("   Reversed order:", routes)
print()

 Task 4: Count routes starting with "N"

print("4. Routes starting with 'N':")
count_n = sum(1 for route in routes if route.startswith("N"))
print(f"   Number of routes starting with 'N': {count_n}")
n_routes = [route for route in routes if route.startswith("N")]
print("   Routes starting with 'N':", n_routes)
print()

Task 5: List comprehension for routes longer than 10 characters

print("5. Routes longer than 10 characters:")
long_routes = [route for route in routes if len(route) > 10]
print("   Long routes:", long_routes)
