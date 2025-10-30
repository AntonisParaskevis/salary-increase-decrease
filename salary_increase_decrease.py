while True:
    try:
        # Prompt the user to enter the current salary
        salary = float(input("Enter the current salary\n"))
        
        # If the user has entered either zero or a negative number, prompt them to enter a valid input
        if salary <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter a number greater than zero.")

# Store the salary in the original_salary variable to save it for later use during the program's execution
original_salary = salary

# Increase the salary by 10%
salary = salary + salary * 0.1

# Then, reduce the salary by 10%
salary = salary - salary * 0.1

# Calculate the salary change percentage
change_percentage = ((salary - original_salary) / original_salary) * 100

# Display the new salary
print("New salary: $" + str(round(salary, 2)) + ".")

# Display the salary change percentage, rounded to 2 decimals
print("Salary change percentage: " + str(round(change_percentage, 2)) + "%.")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")