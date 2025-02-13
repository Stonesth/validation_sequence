import os
from utils import adjust_sequence, read_file, write_file

def modify_file(input_file_path, output_file_path, start_line, start_position, end_position):
    lines = read_file(input_file_path)

    # Adjust sequences starting from the specified line
    lines = adjust_sequence(lines, start_line, start_position, end_position)
    
    write_file(output_file_path, lines)

if __name__ == "__main__":
    input_dir = os.path.join(os.path.dirname(__file__), '../files')
    output_dir = os.path.join(os.path.dirname(__file__), '../output')

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    start_line = 3  # Specify the line where the sequence starts
    start_position = 3  # Specify the starting position of the sequence
    end_position = 6  # Specify the ending position of the sequence

    for filename in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        modify_file(input_file_path, output_file_path, start_line, start_position, end_position)