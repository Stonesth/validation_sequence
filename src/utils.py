def adjust_sequence(lines, start_line):
    previous_sequence = int(lines[start_line - 1][3:6])
    previous_value = lines[start_line - 1][3:6]
    
    for i in range(start_line, len(lines)):
        try:
            current_value = lines[i][3:6]
            current_sequence = int(current_value)
        except ValueError:
            continue
        
        if current_sequence != previous_sequence + 1 and current_sequence != previous_sequence:
            new_sequence = previous_sequence + 1
            group_value = current_sequence
            for j in range(i, len(lines)):
                if lines[j][3:6] == current_value:
                    lines[j] = lines[j][:3] + f"{new_sequence:03}" + lines[j][6:]
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