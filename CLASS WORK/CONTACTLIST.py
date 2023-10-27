# Write a menu driven program to
# 1. add contact details like name,phone,email entered by user
# 2. display the contact details
# 3. edit a particular contact
# 4. delete a particular contact
# 5. search a name in the list,if found display the details


class contact:
    def __init__(self):
        self.contactlist=[]

    def details(self,name,phoneNo,email):
        contactDetails ={
            'Name': name,
            'PhoneNo': phoneNo,
            'email': email
        }
        self.contactlist.append(contactDetails)
    
    def display(self):
        print("THE CONTACT LIST ")
        for i in self.contactlist:
            print("  Name  ",i['Name'])
            print("  PhoneNo  ",i['PhoneNO'])
            print("  Email  ",i['email'])

    def edit(self,search_name):
        self.found = False
        for i in self.contactlist:
            if (i['Name'] == search_name):
                self.newName = input("enter the new name or press enter")
                self.newPhoneNO = input("enter the new phone no or press enter")
                self.newEmail = input("enter the new email or press enter ")

                if self.newName:
                    i['Name']=self.newName
                if self.newPhoneNO:
                    i['PhoneNO']=self.newPhoneNO
                if self.newEmail:
                    i['email']=self.newEmail
                self.found=True
        if self.found == False:
            print("Contact not found")

    def delete(self,delete_contact):
        self.found = False
        for i in self.contactlist:
            if (i['Name']==delete_contact):
                self.contactlist.remove(i['Name']) 




    
obj = contact()
name = input("enter the name").strip().title()
phoneNo = int("enter the phone no")
email = input("enter the email").strip().lower()
contact.details(name,phoneNo,email)
contact.display()
