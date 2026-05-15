class Employee:
    company_name="cisco" #class variable

#Both objects share the same company.
ob1 = Employee()
ob2 = Employee()
print(ob1.company_name)
print(ob2.company_name)





