def convert_to_target_code(input_file, output_file):
    # Read input file contents
    with open(input_file, 'r') as f:
        expressions = f.readlines()

    # Define target registers
    target_regs = {'a': 'R1', 'b': 'R2', 'c': 'R3'}

    # Generate target code for each expression
    target_code = []
    for expression in expressions:
        # Assuming each line contains an assignment expression like "a = b + c"
        parts = expression.strip().split('=')
        target_var = parts[0].strip()
        source_vars = [var.strip() for var in parts[1].split('+')]
        
        # Generate target code for addition operation
        target_code.append(f"LOAD {target_regs[source_vars[0]]}, {source_vars[0]}")
        target_code.append(f"LOAD {target_regs[source_vars[1]]}, {source_vars[1]}")
        target_code.append(f"ADD {target_regs[source_vars[0]]}, {target_regs[source_vars[1]]}")
        target_code.append(f"STORE {target_regs[source_vars[0]]}, {target_var}")

    # Write target code to output file
    with open(output_file, 'w') as f:
        for line in target_code:
            f.write(line + '\n')

if __name__ == "__main__":
    input_file = "input.txt"  # Change this to your input file name
    output_file = "target_code.asm"  # Change this to your desired output file name
    convert_to_target_code(input_file, output_file)

