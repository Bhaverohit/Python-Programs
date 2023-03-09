while (True):
    choice = input("Enter a number : ")

    print("Press Q to quit")
    if (choice == 'q'):
        print("Thank You!!!")
        break

    try:
        choice = int(choice)
        if (choice > 5):
            print("You Entered greater than 5")

    except Exception as e:
        print(f"Your Input is wrong: {e}")

    finally:
        print("Finally code always runs")
