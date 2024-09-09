import os
import json

# Define the domain
domain = "https://github.com/batara42/b42/raw/main/Library"

# Function to get extension for file type detection
def get_file_extension(filename):
    return os.path.splitext(filename)[-1].lower()

# Function to build the file link
def generate_link(path):
    return f"{domain}/{path.replace(' ', '%20')}?download="

# Function to process the tree command output and generate data
def process_tree(directory):
    library_data = {}

    for root, _, files in os.walk(directory):
        folder_name = os.path.basename(root)
        books = []

        for file in files:
            if get_file_extension(file) in ['.pdf', '.epub', '.mobi']:
                book_info = {
                    "name": file,
                    "folder": folder_name,
                    "link": generate_link(os.path.join(folder_name, file))
                }
                books.append(book_info)

        if books:
            library_data[folder_name] = books

    return library_data

# Directory path for the Library folder
library_dir = "./Library"
current_dir = "./_data"

# Process the directory and generate the JSON
library_data = process_tree(library_dir)

# Write the data to a JSON file
output_file = os.path.join(current_dir, "books.json")
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(library_data, json_file, ensure_ascii=False, indent=4)

print(f"Data file created at: {output_file}")
