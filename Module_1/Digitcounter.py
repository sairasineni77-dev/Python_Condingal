num = input("Enter a number: ")

# Remove negative signs if present, then calculate length
digit_count = len(num.replace("-", ""))

print(f"Total digits: {digit_count}")