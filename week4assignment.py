# File Read & Write Challenge

# This program reads from 'original.txt',
# converts the content to uppercase,
# and writes it into 'modified.txt'.

try:
    # Open the original file for reading
    with open("original.txt", "r") as infile:
        content = infile.read()

    # Modify the content (convert to uppercase here)
    modified_content = content.upper()

    # Write the modified content into a new file
    with open("modified.txt", "w") as outfile:
        outfile.write(modified_content)

    print("Modified file created successfully: modified.txt")

except FileNotFoundError:
    print("Error: The file 'original.txt' does not exist.")
except IOError:
    print("Error: Could not read/write the file.")



# Error Handling Lab

# --------------------------------------------
# This program asks the user for a filename
# and tries to read it, handling possible errors.

filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except IOError:
    print("Error: An unexpected I/O error occurred.")
