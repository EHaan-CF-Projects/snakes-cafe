appetizers = ['Wings', 'Tots', 'Meatballs']
entree = ['Fish and Chips', 'Goulash', 'Lasagna']
desserts = ['Spaghetti Eis', 'Lava Cake', 'Warm Cookies']
drinks = ['Tea', 'Coffee', 'Water']



MENU = f"""

**  Welcome to the Snakes Cafe!  **
**  Please see our menu below.   **

** To quit at any time, type "quit" **

Appetizers
----------
{appetizers[0]}
{appetizers[1]}
{appetizers[2]}

Entrees
-------
{entree[0]}
{entree[1]}
{entree[2]}

Desserts
--------
{desserts[0]}
{desserts[1]}
{desserts[2]}

Drinks
--------
{drinks[0]}
{drinks[1]}
{drinks[2]}

"""
print(MENU)

item = ''
customer_order = {}

while item != 'quit':
    item = input('What would you like to order? ').lower()
    if item in customer_order:
        customer_order[item] += 1
        print('** %s orders of %s have been added to your meal **' % (customer_order[item], item.capitalize()))
    elif item not in customer_order:
        customer_order[item] = 1
        print('** 1 order of %s has been added to your meal **' % item.capitalize())

