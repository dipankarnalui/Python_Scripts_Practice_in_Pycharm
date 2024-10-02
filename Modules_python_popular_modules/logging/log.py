import logging

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of the logging messages
    filename='app.log',  # Log messages will be written to this file
    filemode='w'  # Overwrite the logging file each time (use 'a' to append)
)


# Example functions to demonstrate logging
def divide(x, y):
    logging.debug(f"Dividing {x} by {y}")
    if y == 0:
        logging.error("Attempt to divide by zero")
        return None
    return x / y


def main():
    logging.info("Program started")

    result1 = divide(10, 2)
    if result1 is not None:
        logging.info(f"Result of division: {result1}")

    result2 = divide(10, 0)
    if result2 is not None:
        logging.info(f"Result of division: {result2}")

    logging.info("Program finished")


if __name__ == "__main__":
    print("logging is stored in app.logging file")
    main()
