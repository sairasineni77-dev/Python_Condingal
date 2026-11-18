def filter_squares(start, end):
    even_squares = []
    odd_squares = []

    # Loop through the range (end + 1 makes the end number inclusive)
    for num in range(start, end + 1):
        square = num ** 2
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)

# Example call
filter_squares(1, 10)
