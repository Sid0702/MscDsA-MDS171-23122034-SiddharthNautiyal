# CREATE A SPORTMART CLASS, WHERE YOU WILL HAVE
# --> INVENTORY / SELF OF ITEMS
# --> ORDERS OF CUSTOMERS

# CREATE A CSV FILE WHICH WILL STORE YOUR INVENTORY DETAILS AND ORDER DETAILS

# WITH THE HELP OF FILE HANDELING TECHNIQUES IN PYTHON,READ THE FILE 
# AND CREATE AND OBJECT FOR TRINITY STORE AND POPULATE THE INVENTORY 
# ITEMS AND ORDERS INTO THE TRINITY STORES.

# TO MAKE SURE THAT YOU HAVE ADDED ALL THE ITEMS IN YOUR FILE,USE A 
# DISPLAY METHOD TO SHOW YOUR INVENTORY AND ORDER HISTORY.

class sportmart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createInventory(self,productid,productName,Quantity,Price):
        temp ={
            "Productid": productid,
            "ProductName": productName,
            "Quantity": Quantity,
            "Price": Price
        }
        self.inventory[productid] = temp

    def createOrder(self,orderid,productid,quantity,price,total):
        temp = {
            "orderid": orderid,
            "productid": productid,
            "quantity": quantity,
            "price": price,
            "total": total
        }
        self.orders[productid] = temp

    def printOrders(self):
        print(self.orders)
    
    def printInventory(self):
        print(self.inventory)

trinity = sportmart()
orders = open("D:/projects/MY MODULE/orders.csv","r")
o_headers = orders.readline()
o_data = orders.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])

trinity.printOrders()
trinity.printInventory()
# inventories = open("inventory.csv")
# i_headers = inventories.readline()
# i_data = inventories.readlines()
# for data in i_data:
#     tmp = inventories.strip().split(',')



while True:
    print("*"*50)
    print("1: To create new order")
    print("2: To update inventory ")
    print("3: To print orders ")
    print("4: To Print inventory")
    print("5: Exit")
    print("*"*50)

    print("Enter the choice")
    choice = int(input("enter the number"))

    if choice == 1:
        store_pet_details()
    if choice == 2:
        
    #if choice == 3:

    #if choice == 4:

    #if choice == 5:
        print("thanku")
        break
    if choice == 6:
        print("invalid input")