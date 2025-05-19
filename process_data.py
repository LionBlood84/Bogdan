import sys

def process_data(input_file, output_file):
    # Reads data from an input file, performs calculations, and writes the results to an output file.
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Read all lines from the input file
            lines = infile.readlines()

            # Ensure there are at least 3 data values
            if len(lines) < 3:
                print("Error: Input file must contain at least 3 data values.")
                return

            # Extract the first three data values and convert them to floats
            try:
                data1 = float(lines[0].strip())
                data2 = float(lines[1].strip())
                data3 = float(lines[2].strip())
            except ValueError:
                print("Error: Could not convert data values to numbers. Please ensure the input file contains numerical data.")
                return

            # Perform calculations
            sum_of_squares = data1**2 + data2**2 + data3**2
            average = (data1 + data2 + data3) / 3

            # Write the results to the output file
            outfile.write(f"Sum of Squares: {sum_of_squares:.2f}\n")
            outfile.write(f"Average: {average:.2f}\n")

            print(f"Data processed successfully. Results written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
