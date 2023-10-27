# details of students in class
# {   name:
#     reg no:
#     phone:
#     email:
# }
# search Reg no and print all the details

# check if the reg.no ,exists, if exixts replace all the details with the new one

# print("CLASS DETAILS")
# n = int(input("enter the total no of name to be enter"))
# for i in range(n):
#     name = input("enter the name")
#     reg_no = int(input("enter the reg no"))
#     phone

contactList=[]



def contactDetails():
    name=input("enter the name")
    phoneNo=input("enter the contact no")
    email=input("enter the id")

    contactDict={}
    contactDict['Name'] = name
    contactDict['phone no'] = phoneNo
    contactDict['email'] = email

    contactList.append(contactDict)
    print(contactList)

def display():
    print("*"*30)
    print("ENter contact details are")
    print(contactList)

def search():
    nameSearch = input("enter the name to be search")
    found = False
    index = 0
    for name in contactList:
        if name['Name']==nameSearch:
            found = True
            break
        index += 1
    if found == True:
        print('Name is found in the list')
        print(contactList[index]['Name'])
        print(contactList[index]['Phone'])
        print(contactList[index]['Email'])
    else:
        print('Name NOT found!!')
        



