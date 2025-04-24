import xml.etree.ElementTree as ET
import json

def extract_xbrl_tags(queries):
    results = []
    i = 0
    for idx, query in enumerate(queries):
        doc_path = f'./DowJones30/{query["doc_path"]}'
        print(f"Processing file: {doc_path}")
        tags = query.get('id', [])

        if not tags:
            continue

        try:
            tree = ET.parse(doc_path)
            root = tree.getroot()
        except FileNotFoundError:
            print(f"File not found: {doc_path}")
            continue
        except ET.ParseError as e:
            print(f"XML Parsing Error in {doc_path}: {e}")
            continue

        # Create a set of tags for fast membership checking
        tag_set = set(tags)

        # First pass: Gather all elements with 'id' attribute
        id_elements = []
        for elem in root.iter():
            elem_id = elem.get('id')
            if elem_id:  # Only add if id is not None
                id_elements.append((elem_id, elem))

        extracted_data = []
        
        window_size = 100 // len(tags) if tags else 0

        for idx, (elem_id, elem) in enumerate(id_elements):
            if elem_id in tag_set:
                start = max(0, idx - window_size // 2)
                end = min(len(id_elements), idx + window_size // 2 + 1)

                for _, current_elem in id_elements[start:end]:
                    extracted_string = format_element_data(current_elem)
                    extracted_data.append(extracted_string)

        # Format output for the current query
        if extracted_data:
            result = {
                "id": idx + 1,
                "query": query['query'],
                "text": ''.join(extracted_data),
                "answer": query.get("raw_answer")  
            }
            results.append(result)
    return results

def format_element_data(elem):
    return (f"file:{elem.get('contextRef')}.xml\n"
            f"<{elem.tag} contextRef=\"{elem.get('contextRef', 'None')}\" "
            f"decimals=\"{elem.get('decimals', 'None')}\" "
            f"id=\"{elem.get('id', 'None')}\" "
            f"unitRef=\"{elem.get('unitRef', 'None')}\">{elem.text.strip() if elem.text else 'None'}</{elem.tag}>\n")
# Load queries from JSON file
with open('./XBRL_200.json', 'r') as file:
    queries = json.load(file)

# Run the function and get results
formatted_results = extract_xbrl_tags(queries)

# Print the results as JSON
formatted_json = json.dumps(formatted_results, indent=4)  # Use indent for pretty printing

# Optionally, save the formatted JSON back to a file
with open('./Updated_200_XBRL.json', 'w') as outfile:
    outfile.write(formatted_json)