def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input().strip())
    result = check_even(n)
    if result is True:
        if n in range(2, 5):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")