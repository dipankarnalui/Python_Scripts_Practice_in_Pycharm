#Questions:
'''
Implement a restaurant waitlist data structure. It should support the following features:
1) A party of customers can join the waitlist.
2) A previously joined party can leave the waitlist at any time.
3) The restaurant can ask the data structure for the first party that fits a given table size (a table size is given as an argument).
'''
#Data Structure
'''
d1={    
        '1':['c6'],
        '2':['c1','c4','c7'],
        '3':['c2'],
        '4':['c3'],
        '5':['c5','c10']                  
    }
'''

d1 = {}

#customer-party joins the waiting list to get table
def add_waitlist(cust_party, mem_count):
    if mem_count in d1.keys():
        d1[mem_count].append(cust_party)
    elif mem_count not in d1.keys():
        d1[mem_count]=[cust_party]
    return dict(sorted(d1.items()))

#customer-party leave the restaurant after eating complete or, if they cancel the booking, remove the existing customer
def remove_waitlist(cust_party):
    for k in d1.keys():
        if cust_party in d1[k]:
            d1[k].remove(cust_party)
    return dict(sorted(d1.items()))

def allocate_table(table_size):
    key_list=list(d1.keys())
    key_list.sort()
    print(key_list)
    for i in range(len(key_list)-1, -1, -1):
        print("checking member_count = ",i+1)
        print("checking cust_party list=",d1[key_list[i]])
        print("checking length of cust_party=", len(d1[key_list[i]]))
        if len(d1[key_list[i]])==0:
            print("There is no cust_party avaialable with this table_size, go to next table_size")
            table_size = table_size - 1
        elif len(d1[key_list[i]]) > 0:
            print("More than 1 customer is present. Allocating the first cust_party from this list as FCFS.")
            cust_party_allocated=d1[key_list[i]][0]
            print("cust_party_allocated = ", cust_party_allocated)
            return cust_party_allocated
            d1[keys[i]].remove(cust_party_allocated)
            break

if __name__ == "__main__":
    table_size = 5
    while(True):
        print("------------------------------------------------------")
        print("1. Add new customer using add_waitlist()")
        print("2. Delete existing customer using remove_waitlist()")
        print("3. Send the customer to table using allocate_table()")
        print("4. Exit the program.")
        print("------------------------------------------------------")
        option=int(input("Enter your option: "))
        print("------------------------------------------------------")
        if option==1:
            cust_party, mem_count = input("Enter the new customer-party-name, member-count separated by comma = ").split(",")
            if int(mem_count)>table_size:
                print("Customer Party has more member count than the actual table size. Not adding in the waitlist. Do some other arrangements.")
            else:
                cust_existing_in_wait_list=False
                for k,v in d1.items():
                    if cust_party in d1[k]:
                        print("customer-party was already present and waiting in the waitlist. cannot add again.")
                        cust_existing_in_wait_list=True
                if not cust_existing_in_wait_list:
                    d=add_waitlist(cust_party, mem_count)
                    print(f"After adding the customer, the waitlist dictionary content = {d}")
        elif option==2:
            cust_party = input("Enter the existing customer-party-name to delete from waitlist = ")
            cust_existing_in_wait_list = False
            for k,v in d1.items():
                if cust_party in d1[k]:
                    print("customer-party is present in the waitlist.")
                    cust_existing_in_wait_list = True
            if cust_existing_in_wait_list:
                remove_waitlist(cust_party)
                print(f"After deleting the customer, waitlist dictionary content = {d}")
        elif option==3:
            cust_party_got_table=allocate_table(table_size)
            print(f"The table is now allocated to the customer = {cust_party_got_table}")
        elif option==4:
            print("Thanks you! Visit Again.")
            break
        else:
            print("Enter wrong data. Try Again")