import requests
import json

def extract_cik_from_txt(file_path):
    ciks = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by the colon and get the last part
            parts = line.strip().split(':')
            if len(parts) > 1:
                cik = parts[1].strip()  # Get the CIK part and remove whitespace
                if cik.isdigit():  # Check if the CIK is numeric
                    ciks.append(cik)
    return ciks

def write_ciks_to_json(cik_numbers, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(cik_numbers, json_file, indent=4)  # Write CIK numbers to JSON with indentation

def main(txt_file, output_file):
    cik_numbers = extract_cik_from_txt(txt_file)
    write_ciks_to_json(cik_numbers, output_file)  # Write to JSON file
    print(f"Extracted CIK numbers written to {output_file}")

if __name__ == "__main__":
    txt_file_path = './cik-lookup-data-3.txt'  # Update with your file path
    output_file_path = './cik_numbers.json'  # Specify the output JSON file path
    main(txt_file_path, output_file_path)
