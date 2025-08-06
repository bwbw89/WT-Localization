import sys
import os

def main():
    # For relative file pathing
    base_dir = os.path.dirname(os.path.abspath(__file__))

    input_file = os.path.join(base_dir, "input.txt")
    output_file = os.path.join(base_dir, "output.txt")

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    output_lines = []
    one_lines = {}
    for line in lines:
        parts = line.strip().split(';')
        quoted = [p.strip('"') for p in parts if p.startswith('"') and p.endswith('"')]
        if len(quoted) >= 2:
            # For automatically setting the _2 value to that of the _1 value
            key = quoted[0]
            value = quoted[1]

            # Store value of _1 keys in dict
            if key.endswith('_1'):
                one_lines[key[:-2]] = value
                output_lines.append(f'{key};{value}')
            # Change value of _2 to that of _1
            elif key.endswith('_2'):
                base = key[:-2]
                value = one_lines.get(base, value)
                output_lines.append(f'{key};{value}')
            else:
                output_lines.append(f'{key};{value}')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for out_line in output_lines:
            outfile.write(out_line + '\n')




if __name__ == '__main__':
    main()