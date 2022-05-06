import threading

def print_cube(num):
    """
    Function to print cube of a given number
    :param num:
    :return:
    """
    print(f"Cube: {num * num *num}")


def print_square(num):
    """
    Function to print square of a given number
    :param num:
    :return:
    """
    print(f"Square: {num * num}")


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square(25))
    t2 = threading.Thread(target=print_cube(25))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")