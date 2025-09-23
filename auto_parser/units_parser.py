import sys
import os

def main():
    # For relative file pathing
    base_dir = os.path.dirname(os.path.abspath(__file__))

    input_file = os.path.join(base_dir, "input.csv")
    output_file = os.path.join(base_dir, "output.csv")

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(f"Processing: {input_file}")
    print(f"Output to: {output_file}")

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        output_lines = []
        
        for line in lines:
            line = line.rstrip('\n\r')
            parts = line.split(';')
            
            # Keep only the english parts
            if len(parts) >= 2:
                processed_line = ';'.join(parts[:2])
            else:
                processed_line = line
            
            output_lines.append(processed_line)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for out_line in output_lines:
                outfile.write(out_line + '\n')
        
        print(f"Successfully processed {len(output_lines)} lines.")
        print(f"Output saved to: {output_file}")

    except Exception as e:
        print(f"Error processing file: {str(e)}")




if __name__ == '__main__':
    main()