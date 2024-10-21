import csv
import json

def csv_to_json(csv_file, json_file, delimiter=','):
    """
    Convert a CSV file to a JSON file with a custom delimiter.
    
    :param csv_file: Path to the CSV file
    :param json_file: Path to the output JSON file
    :param delimiter: Delimiter used in the CSV file (default is ',')
    """
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=delimiter)
        for row in csv_reader:
            data.append(row)
    
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Successfully converted {csv_file} to {json_file}")

# Example usage
if __name__ == "__main__":
    csv_to_json('sample.csv', 'output.json', delimiter=';')
