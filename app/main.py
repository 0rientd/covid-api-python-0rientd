from requests import get
from bs4 import BeautifulSoup
import re
import json
import shutil
import sys

def main():
    try:
        covid_data = get('https://www.worldometers.info/coronavirus/').text

        soup = BeautifulSoup(covid_data, 'html.parser')

        data_parser = str(soup.find_all("div", {"class": 'maincounter-number'}))
        regex1 = re.findall(r'(\d*,\d*,\d*)', data_parser)
        regex2 = re.findall(r'(\d*,\d*)', data_parser)
        regex2 = regex2[3]

        brazil_cases = get_Brazil(soup)

        json_data = {
            "data": [
                {
                    "Total-Cases": regex1[0],
                    "Recovered": regex1[1],
                    "Deaths": regex2,
                    "Brazil-Cases": brazil_cases
                }
            ]
        }

        with open('data.json', 'w') as outfile:
            json.dump(json_data, outfile)

        print("Created the file data.json successfully")

        try:
            file = "data.json"
            shutil.move(file, "app/data.json")
            print("Moved file with successfully!", file=sys.stdout)

        except:
            print("File data.json not found!", file=sys.stdout)

    except:
        print("Oops! Something happened in main.py")

def get_Brazil(soup):
    soup = soup
    data_parser = str(soup.find_all("td", {"style": 'font-weight: bold; text-align:right'}, {"class": 'sorting_1'}))
    regex = re.findall(r'(\d*,\d*,\d*)', data_parser)

    return regex[3]

if __name__ == "__main__":
    main()