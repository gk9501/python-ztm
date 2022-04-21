while True:
    try:
        age = int(input("What is your age? "))
        print(10/age)
        # raise ValueError('hey, cut it out!') => raising exceptions from within the code
    except ValueError:
        print("Please enter a number!")
        continue
    except ZeroDivisionError:
        print("Please enter an age higher than zero!")
        break
    else:
        print("Thank you!")
        break
    finally:
        print("Ok, I'm finally done")
