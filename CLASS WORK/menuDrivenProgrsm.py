nameList = []

def storeName():
    name = input("enter the named to be saved : ")
    name = name.strip().title()
    nameList.append(name)
    return name

def listNames():
    print("*"*30)
    print("names in the list")
    print("*"*30)
    for name in nameList:
        print(name)
        print("*"*30)

def searchName(search):
    search = search.strip().title()
    for name in nameList:
        if name == search:
            print("name exist in the list")

while True:
    print("*"*30)
    print("1.enter the name")
    print("2.list the name")
    print("3.search for name")
    print("4.exit")
    print("*"*30)

    choice = int(input("enter your choice?"))
    print("you have entered choice: ",choice)

    if choice == 1:
        name = storeName()
        print("Name {}added succesfully!".format(name))
    elif choice == 2:
        listNames()
    elif choice == 3:
        name = input("enter a name to be search")
        searchName(name)
    elif choice == 4:
        exit()
    else:
        print("wrong output")





