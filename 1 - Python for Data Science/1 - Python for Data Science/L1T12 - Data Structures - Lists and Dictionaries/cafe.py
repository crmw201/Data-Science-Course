# List of menu items

menu_list = ['tea', 'coffee', 'croissant', 'beer']

# Dictionary of stock value of each item

stock_value_dict = {'tea': 100, 
                    'coffee': 200, 
                    'croissant': 50, 
                    'beer': 50}

#Price of each item

price_dict = {'tea': 1, 
              'coffee': 1,
            'croissant': 2, 
            'beer': 5}

#Calculate total stock worth, (quantity of stock * price) using for loop
                            # (stock_value_dict * price_dict)

#Create variable to start from zero and add on to through loop

total_stock_worth = 0
for item in menu_list:
    item_value = stock_value_dict[item] * price_dict[item]
    total_stock_worth += item_value

print("£",total_stock_worth)


