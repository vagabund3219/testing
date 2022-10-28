import requests

def send_check(file):
    url = 'https://proverkacheka.com/api/v1/check/get'
    data = {'token': '17072.ReLJYknAYHiPk5ohg'}
    files = {'qrfile': file}
    response = requests.post(url, data=data, files=files)#send request to API
    parsed_data = response.json()
    list_of_items = []
    if (response.status_code == 200):
        try:
            for k in parsed_data["data"]['json']['items']:
                if not isinstance(k['quantity'], int):
                    list_of_items.append({'item': k['name'], 'price': float('{:.2f}'.format(k['price']/100*k['quantity'])), 'count': k['quantity']})
                else:
                    list_of_items.append({'item': k['name'], 'price': k['price']/100, 'count': k['quantity']})
            return list_of_items
        except:
            pass
    else:
        print('Error')