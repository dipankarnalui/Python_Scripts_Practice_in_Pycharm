#host (laptop) --- modem(wifi)---router--- internet -- router(Public IP + Port)----google(remote host)
#www.google.com (URl -- IP) ..DNS..
#SCTP---live video/protocol
#trcert - protocol

balanced = "{[()]}"
not_balanced = "{[(]}"

input = "{{{{{{[[[(((((()))))][)][][][][]]]}}}}}}"
length = len(input)
print("Length of the string = ", length)
half = int(length / 2)
print("Max iteration is needed to check if it's a balanced string = ",half)
count = 1
print("Iteration ", count)
print(input)
while(count != half ):
    count = count + 1
    print("Iteration ", count)
    if ('()' in input ) or ( '{}' in input) or ( '[]' in input):
        input = input.replace('[]', '')
        input = input.replace('{}', '')
        input = input.replace('()', '')
        print(input)
    else:
        print("Not a Balance string")
        break
    if len(input) == 0 :
        print("Balance string")
        break
