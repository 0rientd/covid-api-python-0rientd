from requests import get
from bs4 import BeautifulSoup
import re
import json

def main():
    try:
        covid_data = get('https://www.worldometers.info/coronavirus/').text

        soup = BeautifulSoup(covid_data, 'html.parser')

        data_parser = str(soup.find_all("span", {"style": 'color:#aaa'}))
        regex = re.findall(r'(\d*,\d*,\d*)', data_parser)

        json_data = {'Total-Cases': regex[0]}

        with open('data.json', 'w') as outfile:
            json.dump(json_data, outfile)

        print("Created the file data.json successfully")

    except:
        print("Oops! Something happened")


if __name__ == "__main__":
    main()