import json

# Original books data (you can load this from the 'books.json' file)
# Open and read the JSON file
with open('_data/books.json', 'r') as file:
    books = json.load(file)

# Sort the books by the 'name' field within each category
sorted_books = {category: sorted(items, key=lambda x: x['name']) for category, items in books.items()}

# Output the sorted structure (optional: you can write it back to 'books.json' as well)
sorted_json = json.dumps(sorted_books, indent=4)
# print(sorted_json)

# If you want to save it back to 'books.json', uncomment the following lines:
with open('_data/books.json', 'w') as f:
    json.dump(sorted_books, f, indent=4)
