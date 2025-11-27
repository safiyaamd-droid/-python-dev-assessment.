def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    If the list is empty, returns 0 and prints a warning.
    """
    if not numbers:  # check if the list is empty
        print("Warning: Empty list provided, returning 0 as average.")
        return 0
    total = sum(numbers)
    return total / len(numbers)


def get_list_element(my_list, index):
    """
    Returns the element at the given index from my_list.
    Handles IndexError and TypeError with friendly messages.
    """
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds.")
        return None
    except TypeError:
        print("Error: Provided input is not a list.")
        return None


# Example usage
if __name__ == "__main__":
    # Test calculate_average
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15]
    data3 = []  # Empty list

    print(f"Average of data1: {calculate_average(data1)}")
    print(f"Average of data2: {calculate_average(data2)}")
    print(f"Average of data3: {calculate_average(data3)}")

    print()

    # Test get_list_element
    sample_list = [10, 20, 30]

    print("Element at index 1:", get_list_element(sample_list, 1))       
    print("Element at index 5:", get_list_element(sample_list, 5))       
    print("Element from non-list:", get_list_element("not a list", 0))  

