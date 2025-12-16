def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

inp='dbsahd'
r=is_palindrome(inp)
print(r)