class student:
    def __init__(self,name,phone):           #init is used to initalize data members 
        self.name = name
        self.phone = phone

    def printStudent(self):
        print(self.name,self.phone)

# create a petstore class where you have the details of pets available and their details.
# the class will have methods 
# store a new pet details 
# search for a pet
# sell a pet 
# list all pets
#,type_of_animal,name,age,breed,weight
# importing your petstore class, create a petstoremain file,
# where you will implement a menu driven program for admin -who will manage the store & user who will see the pets and buy


class petstore:
    def __init__(self):
        self.petdatas = []

    def store_pet_details(self):
        name = input("ENTER THE PET NAME")
        type_of_animal = input("ENTER THE TYPE OF PET ")
        age = input("ENTER THE PET AGE")
        breed = input("ENTER THE PET BREED IT BELONGS TOO ")
        weight = input(" ENTER THE PET WEIGHT ")
        petdata =[name,type_of_animal,age,breed,weight]
        print(petdata)
        self.petdatas.append(petdata)

    def search_for_pet(self):
        search_name = input(" Enter the name to be search ")
        for pet_name in self.petdatas[0]:
            if(pet_name == search_name):
                print("Pet found in the list"+pet_name)
        # else:
        #     print("Pet didn't found in the list")

    def sell_a_pet(self):
        name_of_pet_sell = input(" enter the pet name which to be sell ")
        for pet_name in self.petdatas[0]:
            if(pet_name == name_of_pet_sell):
                self.petdatas.remove(name_of_pet_sell)
                print(name_of_pet_sell ,"The pet has been sold")
        # else:
        #     print("invalid details entered ")

    def lists_all_pets(self):
        print(self.petdatas)


view=petstore()
# view.store_pet_details()
view.search_for_pet()

# while True:
#     print("*"*50)
#     print("1: To Store the pet details ")
#     print("2: To Search the pet details ")
#     print("3: To Sell a pet ")
#     print("4: To Print All the pet details ")
#     print("5: Exit")
#     print("*"*50)

#     print("Enter the choice")
#     choice = int(input("enter the number"))

#     if choice == 1:
#         store_pet_details()
#     if choice == 2:
        
#     if choice == 3:

#     if choice == 4:

#     if choice == 5:
#         print("thanku")
#         break
#     if choice == 6:
#         print("invalid input")



