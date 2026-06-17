grocery_inventory = {"Dairy":"Milk", "Bakery": "Bread", "Produce": "Apples"}
grocery_inventory = {                    
    "milk": (113, "Dairy"),
    "Eggs" :(116, "Dairy"),
    "Bread":(117, "Bakery"),
    "Apples":(141, "Produce")
} 
#Retrieve and store Bread's details
bread_details = grocery_inventory.get("Bread")
print("Details of bread:", bread_details)

grocery_inventory['Cookies']  = (143, "Bakery")
print("Inventory after adding cookies:, grocery_inventory")
#Remove Eggs
grocery_inventory.pop ("Eggs")
print("inventory after removing Eggs:", grocery_inventory)
