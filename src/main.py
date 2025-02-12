import os
from utils import adjust_sequence, read_file, write_file

def modify_file(input_file_path, output_file_path):
    lines = read_file(input_file_path)

    # Adjust sequences starting from line 3
    start_line = 3
    lines = adjust_sequence(lines, start_line)

    write_file(output_file_path, lines)

if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), '../files/VFIN0V90.BLVB04.I2D160.CODAGLOB.G1534V00')
    output_file_path = os.path.join(os.path.dirname(__file__), '../output/VFIN0V90.BLVB04.I2D160.CODAGLOB.G1534V00')

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    modify_file(input_file_path, output_file_path)