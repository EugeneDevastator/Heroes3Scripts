import csv
import sys

def parse_csv(filename):
    # Read etalon.csv
    with open('etalon.csv', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        etalon_data = list(reader)
    
    # Read the specified file
    with open(filename, newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        data = list(reader)

    # Extract titles (third row, index 2) for comparison
    etalon_titles = etalon_data[2]
    data_titles = data[2]

    # Sequentially compare titles and create a list of matching indices
    matching_indices = []
    etalon_index = 0

    for data_index, title in enumerate(data_titles):
        if etalon_index < len(etalon_titles) and title == etalon_titles[etalon_index]:
            matching_indices.append(data_index)
            etalon_index += 1

    # Write out the matching columns to a new file
    parsed_filename = filename.split('.')[0] + '_parsed.csv'
    with open(parsed_filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')

        for row in data:
            writer.writerow([row[index] for index in matching_indices if index < len(row)])

    # Print the number of columns in etalon and parsed data
    print("Number of columns in etalon.csv:", len(etalon_titles))
    print("Number of columns in parsed file:", len(matching_indices))

    return parsed_filename

# Assuming the script is run with the filename as the first argument
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the name of the CSV file to parse.")
    else:
        filename = sys.argv[1]
        result_filename = parse_csv(filename)
        print(f"File parsed successfully. Result saved in {result_filename}")

