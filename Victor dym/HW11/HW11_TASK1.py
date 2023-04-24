def checking_information(age):
    try:
        if age > 0 and age % 2 == 0:
            print(f"Your age - {age} is EVEN")
        elif age > 0 and age % 3 == 0:
            print(f"Your age - {age} is ODD")
        elif age <= 0:
            raise ValueError("Your age cannot be lower than 0 or 0 itself((((")

    except ValueError as e:
        print(f"{e}")
    except:
        print("oops, error")

checking_information(int(input("Enter Your age: ")))
