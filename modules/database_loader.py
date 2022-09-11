"""docsting"""
import csv

def load_database(filename:str = None, include_header = True):
    """docsting"""
    if filename is None:
        filename = "example-data.csv"
    with open("database/" + filename, encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        csv_data = []
        for row in csv_reader:
            if include_header:
                include_header = False
                continue
            if len(row) > 0:
                csv_data.append(row)
        return csv_data

def write_database(data_list:list, filename:str = None, include_header = True):
    """docsting"""
    if filename is None:
        filename = "example-data.csv"
    with open ("database/" + filename, 'w', newline='', encoding = "utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        if include_header:
            csv_writer.writerow(["TeamH", "TeamA", "GoalsH", "GoalsA", "Year", "Matchday"])
        for data in data_list:
            if len(data) > 0:
                csv_writer.writerow(data)
