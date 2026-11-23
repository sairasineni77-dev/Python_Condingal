# Initialize the test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the original dictionary
print("The original dictionary is:", test_dict)

# Ask the user to enter the value they want to check
K = int(input("Enter the value to check its frequency: "))

# Count the frequency of the entered value
count = 0
for key in test_dict:
    if test_dict[key] == K:
        count += 1

# Print the result
print(f"Frequency of {K} is: {count}")
