import json
import requests
import time

HEADERS_BASE = {
    'Host': 'api.glassdoor.com',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A551 Safari/8536.25 GDApple/0.0.0',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'br, gzip, deflate',
    'content-length': '0',
}

PARAMS_BASE = (
    ('responseType', 'json'),
    ('t.p', '16'),
    ('t.k', 'fz6JLNgLgVs'),
    ('version', '1.1'),
    ('filter.defaultLocation', 'false'),
    ('filter.defaultEmploymentStatuses', 'false'),
    ('employerId', '43129'),
    ('sort.ascending', 'false'),
    ('action', 'employer-review'),
    ('includeReviewText', 'true'),
    ('s.expires', '1562342531413'),
    ('signature', 'AePA4NybsbFRRw2wYLDpox8eOxs='),
    ('locale', 'en_US'),
    ('gdAppVersion', '6.15.4'),
)

if __name__ == "__main__":
    all_reviews = {'reviews': []}

    for page_number in range(1, 264):
        print('page number: ' + str(page_number))
        params = (('pageNumber', str(page_number)),) + PARAMS_BASE
        referer = 'https://api.glassdoor.com/api-internal/api.htm?responseType=json&t.p=16&t.k=fz6JLNgLgVs&version=1.1&pageNumber={}&filter.defaultLocation=false&filter.defaultEmploymentStatuses=false&employerId=43129&sort.ascending=false&action=employer-review&includeReviewText=true&s.expires=1562342531413&signature=AePA4NybsbFRRw2wYLDpox8eOxs%3D&locale=en_US&gdAppVersion=6.15.4'.format(str(page_number))
        headers = HEADERS_BASE
        headers.update({'Referer': referer})

        response = requests.get('https://api.glassdoor.com/api-internal/api.htm', headers=headers, params=params)
        data = response.json()['response']
        for review in data['reviews']:
            all_reviews['reviews'].append(review)
            print(review['headline'])

        time.sleep(2)

    with open('data/tesla_reviews.json', 'w') as outfile:
        json.dump(all_reviews, outfile)
