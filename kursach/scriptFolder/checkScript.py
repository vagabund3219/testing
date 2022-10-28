import requests

def send_check(full_path):
    url = 'https://proverkacheka.com/api/v1/check/get'
    data = {'token': '17072.ReLJYknAYHiPk5ohg'}
    files = {'qrfile': open(full_path, 'rb')}
    response_text = requests.post(url, data=data, files=files)#send request to API
    parsed_data = response_text.json()
    listOfSum = []
    if (response_text.status_code == 200):
        try:
            for k in parsed_data["data"]['json']['items']:
                if not isinstance(k['quantity'], int):
                    listOfSum.append({'item': k['name'], 'price': float('{:.2f}'.format(k['price']/100*k['quantity'])), 'count': k['quantity']})
                else:
                    listOfSum.append({'item': k['name'], 'price': k['price']/100, 'count': k['quantity']})
            return listOfSum
        except:
            pass
    else:
        print('Error')