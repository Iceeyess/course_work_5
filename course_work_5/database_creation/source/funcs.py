import requests


def get_id_employees(company_names: list[str], url: str) -> list[str]:
    params = dict(text='')
    headers = {'User-Agent': 'HH-User-Agent'}
    res = []
    for company_name in company_names:
        params['text'] = company_name
        response = requests.get(url, params=params, headers=headers).json()['items']
        for resp in response:
            res.append((resp['id']))
    return res


def get_companies_description(id_list: list[str], url: str) -> list[str]:
    headers = {'User-Agent': 'HH-User-Agent'}
    result = []
    for id_ in id_list:
        response = requests.get(url + id_, headers=headers).json()
        result.append(response)
    return result


def get_vacancies(id_list: list[str], url: str) -> list[dict]:
    headers = {'User-Agent': 'HH-User-Agent'}
    result = []
    for id_ in id_list:
        params = dict(employer_id=id_, per_page=100)
        response = requests.get(url, params=params, headers=headers).json()
        result.append(response['items'])
    return result
