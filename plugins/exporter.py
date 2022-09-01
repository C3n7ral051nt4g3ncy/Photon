"""Support for exporting the results."""
import csv
import json


def exporter(directory, method, datasets):
    """Export the results."""
    if method.lower() == 'json':
        # Convert json_dict to a JSON styled string
        json_string = json.dumps(datasets, indent=4)
        with open(f'{directory}/exported.json', 'w+') as savefile:
            savefile.write(json_string)
    if method.lower() == 'csv':
        with open(f'{directory}/exported.csv', 'w+') as csvfile:
            csv_writer = csv.writer(
                csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for key, values in datasets.items():
                if values is None:
                    csv_writer.writerow([key])
                else:
                    csv_writer.writerow([key] + values)
        csvfile.close()
