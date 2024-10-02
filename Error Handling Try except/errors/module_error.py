module_name = "non_existent_module"

try:
    # Attempting to import a module
    module = __import__(module_name)
except ModuleNotFoundError:
    print(f"Error: The module '{module_name}' was not found.")
