class Customers:
    def __init__(self,name,sname,age,ıd):
        self.name=name
        self.sname=sname
        self.age=age
        self.ıd=ıd
class CustomerManager:
    def List(self,listofallproduct):
        for i in range(len(listofallproduct)):
            print(f"name:{listofallproduct[i].name} sname:{listofallproduct[i].sname} age:{listofallproduct[i].age} ıd:{listofallproduct[i].ıd}")
    def Add(self):
        newcustomer=input("\nenter the name to be added\n")
        print("{} is added to customer list.\n".format(newcustomer))
    def Delete(self,customer):
        print(f"{customer.name} {customer.sname} is deleted")

customer1=Customers("jack","hamilton",44,100)
customer2=Customers("ammy","wattsohn",23,101)
allcustomers=[customer1,customer2]
customermanager = CustomerManager()
while(True):
    print("You can select the thing that you want to do\n" +
                    "1-List the all customers\n" +
                    "2-Add new Customer\n" +
                    "3-Delete Customer\n")
    functionselected=int(input())
    if(functionselected==1):
        customermanager.List(allcustomers)
    if(functionselected==2):
        customermanager.Add()
    if(functionselected==3):
        ıd_of_deleting_cus=int(input("Enter the ıd of the customer to be deleted"))
        if(ıd_of_deleting_cus==100):
            customermanager.Delete(customer1)
        if (ıd_of_deleting_cus == 101):
            customermanager.Delete(customer2)
    if(functionselected==-1):
        break;
    print("enter -1 for close the program")