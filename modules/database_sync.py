"""
syncs the local database with webscraper data
"""
import datetime

import modules.webscraper
import modules.database_loader

def sync(filename:str = None):
    """docsting"""
    if filename is None:
        filename = "example-data.csv"
    #
    current_year = datetime.datetime.now().year
    db_data = modules.database_loader.load_database()
    for value in db_data:
        if value == current_year - 2:
            return
    web_range = modules.webscraper.load_range()
    new_csv_data = []
    for year in web_range:
        print(year)
        current_year_data = []
        if year != current_year:
            md1 = modules.webscraper.load_matchday(year, 1)
            current_year_data.append(md1)
            matchdays = (len(md1) * 4) - 1 # should be -2, but range needs +1
            for matchday in range(2, matchdays):
                current_year_data.append(modules.webscraper.load_matchday(year, matchday))
            new_csv_data.extend(current_year_data)
    modules.database_loader.write_database(new_csv_data, filename)
