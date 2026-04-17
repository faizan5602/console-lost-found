import json
from datetime import datetime
import pyfiglet
#Greet Function
red = '\033[91m' 
green = '\033[92m' 
blue = '\033[94m' 
reset = '\033[0m'
yellow = '\033[93m'  
def greet():
     out = pyfiglet.figlet_format("\t\t    Campus Find") 
     print(f"{yellow}{out}{reset}") 
     print(f"{green}\t\t\tWelcome to Campusfind!{reset}") 
     print(f"{red}\tLost something? Found something? Let's fix it together!{reset}") 
   



#Quantity Function (it validate the quantity of item)
def get_quantity():
    qunat=int(input(f"{yellow}Enter item quantity:"))
    if qunat>0:
        return qunat
    else:
        print(f"{red}Quantity must be a positive integer. Please try again.{yellow}")
        return get_quantity()
    



'''It is found item section that inputs the required details of an item and it'll store them in JSON file'''



def add_more_items():
    print("Do you want to add more items?")
    ch=input("Enter your choice in (yes/no or (y/n)):").lower()
    if ch=='yes' or ch=='y':
        found_items()
    elif ch=='no' or ch=='n':
        print("Thank you for using Campusfind!")
    else:
        print("Invalid Input! Please try again.")
        add_more_items()


def found_items():
    text = " FOUND-ITEM SECTION "
    border = "-" * (len(text) + 4)   # top/bottom border length
    
    print(f"\t\t\t{blue}{border}{reset}")
    print(f"\t\t\t{blue}|{reset}{green} {text} {reset}{blue}|{reset}")
    print(f"\t\t\t{blue}{border}{reset}")


    print(f"\n\t{yellow}Please provide the details of the item you found:\n")
# Step 1: Try to load existing items
    try:
        with open("items.json", "r") as file:
            items = json.load(file)   # load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        items = []  # if file doesn't exist or is empty, start fresh
# Step 2: Take new input
    try:
        name = input("Enter item name:").lower()
        quantity = get_quantity()
        location=input("Enter the location where you find this item:").lower()
        d=input("Enter the date in (YYYY-MM-DD):")
        t=input("Enter the time(in (HH:MM)) when you find this item:")
        description=input("Enter the description of your quantity:").lower()
        date=datetime.strptime(d,"%Y-%m-%d")
        date_str=date.strftime("%Y-%m-%d")
        time = datetime.strptime(t, "%H:%M")
        time_str =time.strftime("%H:%M")
    except ValueError:
        print(f"{red}Invalid input. Please enter the correct data types.{yellow}\n")
        return found_items()
# Step 3: Append new item

    items.append({"name": name, "quantity": quantity,'delivered':False,'location':location,'date':date_str,'time':time_str,'description':description,'id':len(items)+1,'received by':None,'receiver contact':None,'received date':None})
# Step 4: Save updated list back to file
    with open("items.json", "w") as file:
        json.dump(items, file, indent=4)
    print("Item added successfully!")
    print("--------------------------------------------------------------------------------------")
    add_more_items()



'''This Function is a sub part of lost item section that perform simple functionality.'''

def further_choice():
    ch = input('Please enter your choice in (yes/no or (y/n)) to proceed further: ').lower()
    if ch =='yes' or ch=='y':
        return True
    elif ch=='no' or ch=='n':
        return False
    else:
        print("Invalid Input! Please try again.")
        return further_choice()



def lost_items():
    text = " LOST-ITEM SECTION "
    border = "-" * (len(text) + 4)   # top/bottom border length
    
    print(f"\t\t\t{blue}{border}{reset}")
    print(f"\t\t\t{blue}|{reset}{green} {text} {reset}{blue}|{reset}")
    print(f"\t\t\t{blue}{border}{reset}")
    print(f"\n\t{yellow}Please provide the details of the item you lost:\n")

    try:
        with open('items.json','r') as file:
            data=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
         print("No items found in the database.")
         return
    
    try:
        name = input("Enter item name: ").lower()
        quantity = get_quantity()
        location=input("Enter the location where you lost this item:").lower()
        d=input("Enter the date in (YYYY-MM-DD):")
        t=input("Enter the time(in 24 hour format(HH:MM)) when you lost this item:")
        date=datetime.strptime(d,"%Y-%m-%d")
        time = datetime.strptime(t, "%H:%M")
    except ValueError:
        print(f"\n{red}Invalid Input.Please enter the correct data types.\n{yellow}")
        return lost_items()
    found=False
    for item in data:
            d_0=datetime.strptime(item['date'], "%Y-%m-%d")
            t_0=datetime.strptime(item['time'], "%H:%M")
            lost_dt = datetime.combine(date, time.time())
            found_dt = datetime.combine(d_0, t_0.time())
            if item['name']==name and item['quantity']==quantity and item['delivered']==False and location==item['location'] and lost_dt <= found_dt:
                    print('Item Found\nDo you want to claim it?\n')
                    choice=further_choice()
                    if choice:
                        found = True
                        item['delivered']=True
                        U_name=input("Enter your name to record the claim:")
                        u_contact=input("Enter your contact number:")
                        item['received by']=U_name
                        item['receiver contact']=u_contact
                        item['received date']=datetime.now().strftime("%Y-%m-%d")
                        print("\n--------------------------------------------------------------------------------------")
                        print(f"\nThanks for using Campusfind {U_name}!\nYou can receive your item from the admin.\nItem Id:{item['id']}\nItem's description:{item['description']}\n")
                        break
                    else:
                        print("You chose not to claim the item at this time.")
                        found=True
                        break
    if not found:
        print(f"{red}Sorry!\nItem does not found\nTry again later!\nIf you have any query contact to admin")

    with open("items.json", "w") as file:
        json.dump(data, file, indent=4)



#Admin Function(It takes user name and password of admin and give the details of all items)

def update_delivery_status():
    print(f"{blue}Do you want to update the delivery status of an item((yes/no) or(y/n))?{yellow}")
    admin_ch=input("Enter your choice:").lower()
    if admin_ch=='yes' or admin_ch=='y':
        return True
    elif admin_ch=='no' or admin_ch=='n':
        return False
    else:
      print(f"{red}Invalid Input! Please try again.{yellow}")
      return update_delivery_status()
    
#ID validation Section    
def get_item_id():    
    try: 
        item=int(input("Enter the item id to update it's delivery status:"))
    except ValueError:
        
        print("Invalid Input! Please enter a valid item id.")
        return get_item_id()
    return item
def id_valid():
    retry=input("Do you want to try again? (yes/no or (y/n)):").lower()
    if retry in ['yes','y']:
        return True
    elif retry in ['no','n']:
        return False
    else:
        print(f"{red}Invalid Input! Please try again.{yellow}")
        id_valid()


def admin():
        text = " ADMIN-SECTION "
        border = "-" * (len(text) + 4)   # top/bottom border length
    
        print(f"\t\t\t{blue}{border}{reset}")
        print(f"\t\t\t{blue}|{reset}{green} {text} {reset}{blue}|{reset}")
        print(f"\t\t\t{blue}{border}{reset}")


        print(f"\n\t{yellow}Please provide your login credentials:\n")
        try:
                with open('login.json','r') as file:
                        data=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
                print("Login data not found or corrupted.")
                return
                
        user_name=input("Enter Your User Name:").lower()
        password=input("Enter Your Password:")
        found=False
        for user in data['user']:
                if user_name==user['username'] and password==user['password']:
                        found=True
                        break
        if found:
                print("\nWELCOME BACK!\nStats are given below\n")
                try:
                        with open('items.json','r') as file:
                                data=json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                        print("No items found in the database.")
                        return
                print(f"{'Name':<25} {'Quantity':<10} {'Location':<20}{'Date':<15} {'Time':<10} {'Delivered':<15} {'Id':<5}{'Received by':<15} {'Receiver contact':<20}{'Received date':<15}\n")
                for items in data:
                        print(f"{items['name']:<25} {str(items['quantity']):<10} {items['location']:<25}{items['date']:<15} {items['time']:<10} {str(items['delivered']):<15} {str(items['id']):<5} {str(items['received by']):<15} {str(items['receiver contact']):<15}{str(items['received date']):<15}")
                
                update=update_delivery_status()
                updated=False
                if update:
                        while True:
                            item=get_item_id()
                            for items in data: 
                                    if item==items['id'] and items['delivered']==False:
                                            items['delivered']=True
                                            updated=True
                                            U_name=input("Enter your name to record the claim:")
                                            u_contact=input("Enter your contact number:")
                                            items['received by']=U_name
                                            items['receiver contact']=u_contact
                                            items['received date']=datetime.now().strftime("%Y-%m-%d")
                                            break
                            if updated:                                     
                                    with open('items.json','w') as file:
                                            json.dump(data,file,indent=4)
                                    print(f"{green}Delivery status updated successfully!{reset}") 
                                    break
                            else:
                                    print(f"{red}Action denied! Either item not found or already delivered.{yellow}")
                                    if id_valid():
                                          continue
                                    else:
                                        break
                else:
                     print(f"{blue}No updates required{reset}") 
                                 
        else:
             print(f"{red}Request Denied!{yellow}\nInvalid Username or Password.\n")
             admin()




#User() funnction is a simple selection function

def user():
    text = " USER-SECTION "
    border = "-" * (len(text) + 4)   # top/bottom border length
    
    print(f"\t\t\t{blue}{border}{reset}")
    print(f"\t\t\t{blue}|{reset}{green} {text} {reset}{blue}|{reset}")
    print(f"\t\t\t{blue}{border}{reset}")

    print(f"\t\n{yellow}Are you looking to report a lost item or found item?\nIf 'yes', then\nPress 1 to report Lost item\nPress 2 for found item.")
    try:
        ch=int(input("Enter your choice:"))
        if ch==1:
            lost_items()
        elif ch==2:
            found_items()
        else:
            print(f"{red}Invalid Input! Please try again.{yellow}\n")
            user()
    except ValueError:
         print(f"\n{red}Invalid Input! Please try again.{yellow}\n")
         return user()
    

#It is a simple descision function to perform further action

def desicion():
    text = " HOME-SECTION "
    border = "-" * (len(text) + 4)   # top/bottom border length
    
    print(f"\t\t\t{blue}{border}{reset}")
    print(f"\t\t\t{blue}|{reset}{green} {text} {reset}{blue}|{reset}")
    print(f"\t\t\t{blue}{border}{reset}")

    print(f"\n{yellow}Are you a USER or ADMIN?\nPress 1 for USER\nPress 2 for ADMIN")
    try:
        choice=int(input("Enter your choice:"))
        if choice==1:
            user()
        elif choice==2:
            admin()
        else:
            print(f"{red}Invalid Input! Please try again.{yellow}\n")
            desicion()
    except ValueError:
         print(f"\n{red}Invalid Input! Please try again.{yellow}\n")
         return desicion()

    

greet()
desicion()
