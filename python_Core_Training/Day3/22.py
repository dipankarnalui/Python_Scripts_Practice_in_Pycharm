import logging as log

log.basicConfig(level=log.DEBUG, filename="err2.log")
try:
    arr = [10, 20, 30, 40, 50]
    index = input("Enter the index : ")
    index = int(index)
    print("ARR = ", arr[index])

except ValueError as e1:
    log.info(e1, exc_info=True)
except IndexError as e2:
    log.info(e2, exc_info=True)