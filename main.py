import requests, bs4;

def getDestination(liElement):
    return liElement.find('div', 'location').contents[0];

url = 'https://www.yachtworld.com/';
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers);
print(response);
# print(requests.get('https://httpbin.org/ip').json());

# soup = bs4.BeautifulSoup(response.text, 'lxml');

# list = soup.find_all('li', {'class': 'listing-result'})

# for item in list:
    # print(getDestination(item));
