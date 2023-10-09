def has_newline_at_end(filename):
    try:
        with open(filename, 'rb') as file:
            file.seek(-1, 2)  # Go to the last character in the file.
            last_char = file.read(1)
            return last_char == b'\n'
    except FileNotFoundError:
        return False

filename = '1-calculation.py'  # Replace with the name of your file.
result = has_newline_at_end(filename)

if result:
    print(f"The file '{filename}' has a newline at the end.")
else:
    print(f"The file '{filename}' does not have a newline at the end.")
