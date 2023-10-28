def calculate_square_and_cube(sequence):
    squares = [num ** 2 for num in sequence]
    cubes = [num ** 3 for num in sequence]
    return squares, cubes

def main():
    try:
        # Get a sequence of numbers from the user
        input_sequence = input("Enter a sequence of numbers separated by spaces: ")
        
        # Convert the input to a list of float numbers
        numbers = [float(num) for num in input_sequence.split()]

        # Calculate squares and cubes
        squares, cubes = calculate_square_and_cube(numbers)

        # Display the results
        for i, num in enumerate(numbers):
            print(f"Number: {num}, Square: {squares[i]}, Cube: {cubes[i]}")

    except ValueError as e:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
