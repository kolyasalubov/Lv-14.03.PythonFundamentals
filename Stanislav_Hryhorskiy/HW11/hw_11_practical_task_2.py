# *** Task 2 ***
# Write a program that analyzes the entered number and,
# depending on the number, gives the day of the week that
# corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of entering numbers from 8 and more,
# as well as cases of entering nonnumerical data.

WEEK_DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def is_valid_day_number(number: int) -> None:
    """
    Function that raise 'ValueError' if number not in range [1; 7]
    """
    if number not in range(1, 8):
        raise ValueError("a day of the week must be in the range [1; 7]")


def main(literal: str) -> None:
    """
    Function that return the day of the week corresponds to entered number.
    In case of incorrect data, an exception 'ValueError' is raised.
    """
    try:
        is_valid_day_number(int(literal))
    except ValueError as error:
        print(f"ValueError: {error}")
    else:
        print(f"The day of the week corresponds "
              f"to entered number: '{WEEK_DAYS.get(int(literal))}'.")


if __name__ == "__main__":
    main(input("Enter the number of the day of the week: "))
