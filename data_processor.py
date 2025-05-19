from process_data import process_data
import sys

if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python data_processor.py <input_file>")
        sys.exit(1)

    # Get the input file name from the command line argument
    input_file = sys.argv[1]
    output_file = "output.txt"  # Define the output file name

    # Call the data processing function
    process_data(input_file, output_file)