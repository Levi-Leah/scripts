import os
import xml.etree.ElementTree as ET

def extract_abstract(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    content_with_root = f'<root>{content}</root>'
    
    try:
        root = ET.fromstring(content_with_root)
        abstract_element = root.find('abstract/para')
        
        # Check if abstract element exists and if its text contains "{Abstract}"
        if abstract_element is not None and "{Abstract}" in abstract_element.text:

            return None

        abstract = abstract_element.text if abstract_element is not None else "No abstract found"

        return file_path, abstract
    except ET.ParseError as e:
        print(f"Error parsing XML in file {file_path}: {e}")
        return file_path, "Error parsing XML"

def search_recursive(directory_path):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith(".xml"):
                file_path = os.path.join(foldername, filename)
                result = extract_abstract(file_path)

                # Only print if result is not None
                if result is not None:
                    print(f"{result[0]}")
                

# Specify the root directory containing XML files
root_directory = '/home/levi/rhel-8-docs/'

# Perform recursive search
search_recursive(root_directory)
