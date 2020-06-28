from requests import get
from bs4 import BeautifulSoup
import re
import json
import shutil
import sys

covid_data = get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(covid_data, 'html.parser')

json_data = {
    "data": [
        {

        }
    ]
}

def main():
    try:
        data_parser = str(soup.find_all("div", {"class": 'maincounter-number'}))
        regex1 = re.findall(r'(\d*,\d*,\d*)', data_parser)
        regex2 = re.findall(r'(\d*,\d*)', data_parser)
        regex2 = regex2[3]

        json_data = {
            "data": [
                {
                    "Global-Cases": regex1[0],
                    "Global-Recovered": regex1[1],
                    "Global-Deaths": regex2,
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

def countries():
    count = 0

    for countries in soup.find_all('tr'):
        try:
            regex_country_name = re.search(r'<a class="mt_a" href="(.*)">(.*)</a>', str(countries))
            regex = re.findall(r'<td style="font-weight: bold; text-align:right">(.*)</td>', str(countries))
            regex_deaths = re.findall(r'<td style="font-weight: bold; text-align:right;">(.*) </td>', str(countries))
            json_data['data'].append({
                "Country": regex_country_name.group(2), 
                "Country-Cases": regex[0], 
                "Country-Recovered": regex[1], 
                "Country-Deaths": regex_deaths[0],
            })

        except:
            pass

        count = count + 1

    with open('data_country.json', 'w') as outfile:
            json.dump(json_data, outfile)

    print("Created the file data_country.json successfully")

    try:
        file = "data_country.json"
        shutil.move(file, "app/data_country.json")
        print("Moved file with successfully!", file=sys.stdout)

    except:
        print("File data.json not found!", file=sys.stdout)


if __name__ == "__main__":
    main()