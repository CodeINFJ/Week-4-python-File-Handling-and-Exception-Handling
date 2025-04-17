# Reads a file, modifies its content, writes to a new file, and handles errors.

def file_read_write_with_error_handling():
    input_filename = input("Enter the filename to read: ")

    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        print(f"✅ Read from '{input_filename}'")

        modified_content = content.upper()  # Modify content

        output_filename = input("Enter a filename to save the modified content: ")
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        print(f"✅ Written to '{output_filename}'")

    except FileNotFoundError:
        print(f"❌ '{input_filename}' not found.")
    except IOError as e:
        print(f"⚠️ Error: {e}")

file_read_write_with_error_handling()
