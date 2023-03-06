#======= Shoe Inventory Manager =======#

# This programme runs a shoe inventory for a Nike store manager.
# It has the following parts: (1) "Shoe" class, that defines shoe objects and has various functions 
# for returning class attributes, (2) a list of shoe objects imported from inventory.txt, (3) a series
# of functions for manipulating and altering the information in inventory.txt, and (4) a user menu.

import os

# (1)
#========The beginning of the class==========
class Shoe:
    
    """This class defines shoe objects, and contains functions to return certain class attributes
    as well as __repr__ and __str__ forms"""

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
     
    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product
    
    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def __repr__(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]
    
    def __str__(self):
        return f"""
Country - {self.country}
code - {self.code}
product - {self.product}
cost - {self.cost}
quantity - {self.quantity}"""

# (2)
#=============Shoe list===========

shoe_list = []

# (3)
#==========Functions outside the class==============
# This function reads information from "inventory.txt" and passes each line as an object to the Shoe class.
def read_shoes_data(): 
    
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            lines = file.readlines()
            
            each_shoe = []
            
            for line in lines:
                line = line.rstrip("\n").strip(" ").split(", ")
                each_shoe.append(line)
            
            itemised = []
    
            for ele in each_shoe:
                itemised += ele[0].split(",")
            
            individual_shoes = []
            
            n = 0
            
            for ele in range(n, len(itemised)):
                if n < (len(itemised)): # This might be wrong!!
                    item = itemised[n:n+5]
                    individual_shoes.append(item)
                    n = n+5
                else:
                    break
            
            for ele in individual_shoes:
                shoe_list.append(Shoe(ele[0], ele[1], ele[2], ele[3], ele[4]))
            
            file.close()
    except FileNotFoundError:
        print("\nSorry, that file doesn't seem to exist...\n")

# This function allows the user to enter a new shoe object to shoe_list.
def capture_shoes():
     
    print("\nYou're entering a new shoe:\n")
    shoe_list.append(Shoe(input("Enter the country: "), 
                    input("Enter the code: "),
                    input("Enter the product name: "),
                    input("Enter the cost: "),
                    input("Enter the quantity: ")))

# This function allows the user to view all the shoes stored in shoe_list.     
def view_all():
    
    for ele in shoe_list:
        print(f"{Shoe.__str__(ele)}")
        
# This function: (1) finds all the quantities of the objects in shoe_list and returns the object with
# the lowest quantity. (2) It then allows the user to update the quantity and writes to "inventory.txt".
def re_stock():
    
    try: 
        quants = []
        
        for ele in shoe_list:
            quantity = Shoe.get_quantity(ele)
            quantity = int(quantity)
            quants.append(quantity)
            
        minimum = min(quants)
        minimum = str(minimum)
        
        min_list = []
    
        for item in shoe_list:
            if (Shoe.get_quantity(item)) == minimum:
                min_list.append(Shoe.__repr__(item))
                print(f"\nThe shoe with the lowest stock quantity is:\n{Shoe.__str__(item)}.\n")
                break
            else:
                continue
        
        while True:
            user_choice = input("""Would you like to:
Add to this quantity of shoes and update - "a"
Exit                                     - "e"
:
""")
            user_choice = user_choice.lower().strip()
        
            if user_choice == "a":
                new_quantity = input("\nPlease enter the new quantity: \n")
                min_list[0][4] = new_quantity
                print(f"You have changed the stock quantity to: {min_list[0][4]}.")
            
                try:
                    with open("inventory.txt", "r+") as file, open("temp.txt", "a+") as temp:
                        
                        first_line = file.readline(-1)
                        temp.write(first_line)
                        
                        lines = file.readlines()
                        
                        for line in lines:
                            line = line.split(",")
                        
                            if line[1] == min_list[0][1]:
                                min_string = ",".join(min_list[0])
                                line = " ".join(line)
                                new_line = f"{line.replace(line, min_string)}\n"
                                temp.write(new_line)
                            else:
                                line = ",".join(line)
                                temp.write(line)
                                
                        os.remove("inventory.txt")
                        os.rename("temp.txt", "inventory.txt")       
                        temp.close()
                        
                except IndexError:
                    continue
            elif user_choice == "e":
                break
    except ValueError:
        print("\n")

# This function allows the user to search for a shoe by code and returns the shoe object.
def search_shoe():
    
    user_code = input("Enter the shoe code:")
    
    codes_list = []
    
    for ele in shoe_list:
        codes_list.append(Shoe.get_code(ele))
     
    codes_count = 0
    
    for ele in codes_list:
        if ele != user_code:
            codes_count += 1
        else:
            continue
    
    if codes_count == len(codes_list):
        print("The code you entered doesn't exist...")
    else:
        for ele in shoe_list:
            if (Shoe.get_code(ele)) == user_code:
                found_shoe = Shoe.__str__(ele)
                print(found_shoe)
            else:
                continue

# This function gives the user the total value per shoe (i.e. quantity x cost).
def value_per_item():
    
    for item in shoe_list:
        cost = int(Shoe.get_cost(item))
        quantity = int(Shoe.get_quantity(item))
        value = cost * quantity
        print(f"{Shoe.get_product(item)} has a total value of £{value}.")

# This function finds the shoe with the largest quantity and prints that it is for sale.
def highest_qty():
    
    quants = []
        
    for ele in shoe_list:
        quantity = Shoe.get_quantity(ele)
        quantity = int(quantity)
        quants.append(quantity)
            
    maximum = max(quants)
    maximum = str(maximum)
    
    max_list = []

    for item in shoe_list:
        if (Shoe.get_quantity(item)) == maximum:
            max_list.append(Shoe.__repr__(item))
            print(f"\nThe shoe with the lowest stock quantity is:\n{Shoe.__str__(item)}.\n")
            break
        else:
            continue
   
    print(f"\nThe shoe with the highest stock quantity is: {max_list[0][2]} (code:{max_list[0][1]}).\nThis shoe is for sale!\n")

# (4)    
#==========Main Menu=============
# This is a user menu for accessing the different functions above.

print("Welcome to the inventory!")

read_shoes_data()

while True:
    
    user_choice = input("""Please select an option from the following:
See all the shoes in the inventory - "a"               
Enter new shoe                     - "b"
Update stock quantity              - "c"
Search shoe by code                - "d"
See all shoe values                - "e"
Search shoe with highest stock     - "f"
Exit                               - "z"
:
""")

    user_choice.lower().strip()
    
    if user_choice == "a":
        
        view_all()
        
    elif user_choice == "b":
        
        capture_shoes()
    
    elif user_choice == "c":
        
        re_stock()
        
    elif user_choice == "d":
        
        search_shoe()
        
    elif user_choice == "e":
    
        value_per_item()  
    
    elif user_choice == "f":
    
        highest_qty()
    
    elif user_choice == "z":
        
        break
    
    else:
        print("\n Sorry, I didn't get that... Try again!\n")