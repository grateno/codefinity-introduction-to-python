# Input variables
days_until_expiration = 3
days_until_expiration == 4 < 6 
discount = 10
stock_level = 50
product_type  = "Perishable"
# product_type = "non_perishable"
if product_type == "Perishable":
    if days_until_expiration <=3 and stock_level > 50:
          print("30% discount applied ")  
    elif days_until_expiration <= 6 and stock_level > 50:
       print("20% discount applied ")
    elif days_until_expiration  > 6 and stock_level <= 50:
       print("10% discount applied")
else:
     print ("No discount available for non-perishable items.")




