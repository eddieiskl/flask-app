import os

# Define the file path
file_path = 'names.txt'

# Function to read names from the file
def read_names_from_file(file_path):
    names = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if ': ' in line:
                    line_number, name = line.split(': ', 1)
                    names.append((int(line_number), name.strip()))
    return names

# Function to save names to the file
def save_names_to_file(names, file_path):
    with open(file_path, 'w') as file:
        for line_number, name in names:
            file.write(f"{line_number}: {name}\n")

# Read existing names from the file
names = read_names_from_file(file_path)

# Get new names from the user and append with the appropriate line number
starting_line_number = len(names) + 1
for i in range(3):
    name = input("Enter a name: ")
    names.append((starting_line_number + i, name))

# Save the updated list of names to the file
save_names_to_file(names, file_path)

# Print all names with their line numbers
for line_number, name in names:
    print(f"Line {line_number}: {name}")