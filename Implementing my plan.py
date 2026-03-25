# Name: Alain Irumva
# Username: irumvaa
# Assignment: HW04: A Bug's Life
# Purpose: Calculate the Life Path Number based on birth date
# Acknowledgements: Dr.Heggen
import time
def main():
    """ Main function which takes in the user's input for month, day, and year,
     and prints the user's life path number.
"""
    print(" You are about to find out your Life Path number")
 # Determine the month
    month = int(input("Please, enter your birth month(1-12): "))
    if month < 1 or month > 12: # check if input is correct
        print("Error: Invalid month")
        return
    if month == 2:
        day_max = 28 or 29 # February
    elif month in [4,6,9,11]: # Months with 30 days
        day_max = 30
    else:
        day_max = 31 # Months with 31 days
    #Determine the day
    day = int(input(f"Enter your birth day (1-{day_max}): "))
    if day < 1 or day > day_max: # check if input is correct
        print(f"Error: invalid day for month {month}).")
        return
    year= int(input("enter your birth year in this format (YYYY): "))

    # Life Path formula

    life_path_number = compute_life_path_number(month, day, year)
    print(f"I am back with your life path number, {life_path_number}")
    if life_path_number <10:
        print(" You are likely to be an entrepreneur in the future")
        time.sleep(3)
        print(" Say Amen")
    elif life_path_number == 11 or life_path_number == 22 or life_path_number == 33:
        print(" What a lucky person you are!!!, God has chosen you to be successful")
    else:
        print(" Scientists are still learning about you!!")
def master_number(num):
    """Check if the number is a master number  (11, 22, or 33).
    Args:
        num (int): The number to check.
    Returns:
        bool: True if it is a Master Number, otherwise False."""
    return num in [11,22,33]
def sum_digits(num):
    """compute the sum of digits
    Args:
        num (int): The number whose digits will be summed.
    Returns:
        int: The sum of the digits."""
    return sum(int(digit) for digit in str(num)) #Calculate sum of each digit
def compute_life_path_number(month, day, year):
    """ calculate the life path number based on the data given by the user
     Args:
        month (int): User's birth month.
        day (int): User's birth day.
        year (int): User's birth year.
    Returns:
        int: The calculated Life Path Number."""
    month_value = 11 if month == 11 else sum_digits(month)
    day_value = day if day in [11, 22] else sum_digits(day)
    year_value = sum_digits(year)

    total_value = month_value + day_value + year_value

    if master_number(total_value):
        return total_value

    while total_value > 9:
        total_value = sum_digits(total_value)

    return total_value

if __name__ == "__main__":
    main()
