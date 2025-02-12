def adjust_sequence(lines, start_line, start_position, end_position):
    previous_sequence = int(lines[start_line - 1][start_position:end_position])
    previous_value = lines[start_line - 1][start_position:end_position]
    sequence_length = end_position - start_position
    
    for i in range(start_line, len(lines)):
        try:
            current_value = lines[i][start_position:end_position]
            current_sequence = int(current_value)
        except ValueError:
            continue
        
        if current_sequence != previous_sequence + 1 and current_sequence != previous_sequence:
            new_sequence = previous_sequence + 1
            group_value = current_sequence
            for j in range(i, len(lines)):
                if lines[j][start_position:end_position] == current_value:
                    lines[j] = lines[j][:start_position] + f"{new_sequence:0{sequence_length}}" + lines[j][end_position:]
                else:
                    break
            previous_sequence = new_sequence
        else:
            previous_sequence = current_sequence
    
    return lines

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)