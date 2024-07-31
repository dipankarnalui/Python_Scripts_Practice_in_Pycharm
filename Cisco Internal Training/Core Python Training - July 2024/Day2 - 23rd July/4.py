'''
WORLD LIMIT: prompt the user to enter a sentence from the keyboard

a sentence can have min words = 2, max wored = 8

if number of words within the limit - WITHIN THE LIMIT
if it exceeds limit - OUT OF LIMIT

Given:-
-------
Enter a sent : hello world of unix
Expected:-
----------
your string has 5 words - within limit

Given:-
-------
Enter a sent : sample text was added using text editor on os
Expected:-
----------
your sent has 10 words - out of limit
'''

min=2
max=8
s1=input("Enter sentence = ")
words=s1.split()
if len(words)>min and len(words)<max :
    print(f"your string has {len(words)} words - within limit")
elif len(words)<min or len(words)>max:
    print(f"your string has {len(words)} words - OUT OF LIMIT")