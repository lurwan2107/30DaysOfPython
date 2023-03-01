# 1

import requests, json
from bs4 import BeautifulSoup

website =  'http://www.bu.edu/president/boston-university-facts-stats/'

# Extracting the data

fetch_data = requests.get(website)
get_content = fetch_data.content
chanceToPerse = BeautifulSoup(get_content, 'htm.parser')

# Storing as json file

with open('storing_as_json.json', 'w') as sample:
    json.dump(chanceToPerse, sample, ensure_ascii=False, indent=4)




# 2

import requests, json
from bs4 import BeautifulSoup

website2 =  'https://archive.ics.uci.edu/ml/datasets.php'

# Extracting the data

from_web = requests.get(website2)
data_content = from_web.content
Perse = BeautifulSoup(data_content, 'htm.parser')

# Storing as json file

with open('storing_as_json2.json', 'w') as sample:
    json.dump(Perse, sample, ensure_ascii=False, indent=4)
    



    


