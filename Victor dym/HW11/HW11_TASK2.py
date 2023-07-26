try:
    number_day = int(input("Enter you number: "))
    dictionary = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    for key in dictionary:
        if key == number_day:
            print(dictionary[key])
        elif number_day not in range(1, 8):
            raise ValueError("Your number is not in range")

except ValueError as e:
    print(f"{e}")