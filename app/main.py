from requests import get
from bs4 import BeautifulSoup
import re
import json
import shutil
import sys

def main():
    try:
        covid_data = get('https://www.worldometers.info/coronavirus/').text
        covid_data_brazil = get('https://www.worldometers.info/coronavirus/country/brazil/').text

        soup = BeautifulSoup(covid_data, 'html.parser')
        soup_brazil = BeautifulSoup(covid_data_brazil, 'html.parser')

        data_parser = str(soup.find_all("div", {"class": 'maincounter-number'}))
        regex1 = re.findall(r'(\d*,\d*,\d*)', data_parser)
        regex2 = re.findall(r'(\d*,\d*)', data_parser)
        regex2 = regex2[3]

        brazil_cases = get_Brazil(soup_brazil)

        json_data = {
            "data": [
                {
                    "Global-Cases": regex1[0],
                    "Global-Recovered": regex1[1],
                    "Global-Deaths": regex2,
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
    data_parser = str(soup.find_all("div", {"class": 'maincounter-number'}))
    regex = re.findall(r'(\d*,\d*,\d*)', data_parser)

    return regex[0]

if __name__ == "__main__":
    main()