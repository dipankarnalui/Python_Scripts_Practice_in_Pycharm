try:
    open('read_only_file.txt', 'w')  # Attempting to write to a read-only file
except PermissionError:
    print("Error: Permission denied.")
