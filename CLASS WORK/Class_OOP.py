# class Student():
#     #data members
#     #name,email,phone,...
#     #member function
#     def __init__(self):
#         self.name = "siddharth"
#         self.email ="siddharthnautiyal07@gmail.com" 
#         self.phone = 9411234567
#         self.section = 'A'

#     def printstudent(self):
#         print("name : {}\nEmail : {},\nphone : {}".format(self.name,self.email,self.phone))
    

#     # def _str_(self):
#     #     pass
# siddharth = Student()
# siddharth.printStudent()
# # print(hitanshi.name)

class Student:
    def __init__(self,a,b):
        self.name=a
        self.stu_class =b
    def __str__(self):
        return self.name
abc = Student("siddharth","msc")
print(abc.name,abc.stu_class)
print(abc)
print(type(abc))

#create a class restuarant that accept itemme & qty as input
#inside your class you are having the item and its price as a dictionary
#create a function calculate cost that prints the itemname,qty ad price 

class restuarant:
   
     def __init__(self,item,qty):
        self.item=item
        self.qty=qty
        self.menu={"rice":30,
            "chicken":40,
             "tea":10}
    
     def findCost(self):
         total = 0
         total = self.menu[self.item] * self.qty
         print(self.item,self.qty,total)

order = restuarant("rice",4)
order.findCost()

order2= restuarant("chicken",3)
order2.findCost()


# define a class expense tracker that stores the expenses
# and income in a dictionary
# implement the method to 
# store the transacation 
# view transactions
# calculate the total expense

class expenseTracker:
    def __init__(self):
        self.transactions ={
            "expense":[],
            "income":[]
        }
    def StoreTransactions(self,type,category,cost,desc,date):
        #expense/income
        #type/category
        #cost/amount
        #description on the transaction
        transaction={
            "category":category,
            "cost":cost,
            "description":desc,
            "date":date
        }
        if type=="expenses":
            self.transactions['expense'].append(transaction)
        else :
            self.transactions['income'].append(transaction)
        return True
    def view_transactions(self):
        print("INCOME")
        for abc in self.transactions['income']:
            print(abc)
        print("EXPENSES")
        for abc in self.transactions['expense']:
            print(abc)

    def totalincomeexpense(self):
        print("total income")
        total_income =0
        for income in self.transactions['income']:
            total_income +=income["cost"]
        print(total_income)

        print("total expenses")
        total_expense=0
        for expenses in self.transactions['expense']:
            total_expense +=expenses['cost']
        print(total_expense)

mytransactions = expenseTracker()
mytransactions.StoreTransactions("expenses","electricity bill",4500,"mdhc","20/09/2023")
mytransactions.StoreTransactions("income","pocket money",14500,"from parents","25/07/2023")
mytransactions.StoreTransactions("expenses","food",9000,"cafe by the valley","29/09/2023")

mytransactions.view_transactions()
mytransactions.totalincomeexpense()
