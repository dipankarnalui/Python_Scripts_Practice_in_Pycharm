#Feature is given
#Write Test Cases
#Automate the Test Case
'''
meeting room with 5 lights
for every 5 people entering the room one light get lit
when every max lights are lit
lock the room
alarm email to be send to admin@roommanagment.com
'''

#TC1 for number of people not a factor of 5, Eg. 7
#TC2, what if the light has error
#TC3, simultaneously 10 people entering, parallel processing
#TC4, when Max 25 people enters, verify all the lights are set to True
#TC5, when all 5 lights = true, set room lock flag = entry closed, stack overflow condition
#TC6, when room is locked, send_mail("msg = room occupied", "email to: admin@roommanagment.com")
#TC7: verify the reply msg from admin that confirms the mail was received by the admin
#TC8: exit
#TC9: entry and exit criteria
people_list=[]
def enter(person):
    max_people = 25
    if len(people_list) < max_people:
        people_list.append(person)
        if len(people_list) > 1 and len(people_list) < 5:
            light1=True
        if len(people_list) > 5 and len(people_list) < 10:
            light2 = True
        if len(people_list) > 10 and len(people_list) < 15:
            light3 = True
    elif len(people_list) == max_people:
        room_lock = True
        check=send_mail("msg = room occupied", "email to: admin@roommanagment.com")
        if check == "received":
            print("msg was received by admin")
def send_mail(a,b):
    print("msg sent")
    return "received"
if __name__ == "__main__":
    min_people = 5
    max_people = 25
    enter("emp1")
    enter("emp2")
    enter("emp3")
    enter("emp4")
    enter("emp5")


