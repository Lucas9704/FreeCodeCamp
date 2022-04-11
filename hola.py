user_input = input("Enter a list of numbers, comma-separated\n>> ")
user_input_as_list = user_input.split(",")
user_input_as_numbers_in_list = map(float, user_input_as_list)  # maybe int?
# This will fail if the user entered any input that ISN'T a number


def sum(lst):
    accumulator = 0
    for element in lst:
        accumulator += element
    return accumulator
