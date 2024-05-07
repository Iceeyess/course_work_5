import requests

hh_company_names = ['Lada', 'УАЗ', 'Русский стандарт', 'Райффайзен банк', 'Сбербанк']
employee_id_API = 'https://api.hh.ru/employers'


def get_id_employees(company_names: list[str], url: str) -> list[str]:
    params = dict(text='')
    headers = {'User-Agent': 'HH-User-Agent'}
    res = []
    for company_name in company_names:
        params['text'] = company_name
        response = requests.get(url, params=params, headers=headers).text
        res.append(response)
    return res


for x in get_id_employees(hh_company_names, employee_id_API):
    print(x)