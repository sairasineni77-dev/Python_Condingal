def shutdown(user_input):
    if user_input == "Yes":
        print("shutting down")
    elif user_input == "no":
        print("abort shut down")
    else:
        print("sorry.")

# Ask the user for input and call the function
choice = input("Do you want to shut down? (Yes/no): ")
shutdown(choice)
