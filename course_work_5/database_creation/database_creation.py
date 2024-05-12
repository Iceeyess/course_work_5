import psycopg2
import json
from source.constants import path_for_vacancies, path_for_companies
#########################################################
#Data file fetch, database creation, save to database tables
#########################################################

with open(path_for_companies, mode='r', encoding='utf-8') as f:
    data_companies = json.load(f)
with open(path_for_vacancies, mode='r', encoding='utf-8') as f:
    data_vacancies = json.load(f)

params = dict(host='localhost', database='course_work_5', port=5432, user='postgres', password='Herbalife1', )
with psycopg2.connect(**params) as connection:
    with connection.cursor() as cursor:
        d_dict = {}
        for company_vacancies in data_vacancies:  # Список компаний
            for vacancy in company_vacancies:  # Список вакансий у компании
                # добавляет в d_dict типы данных к ключам у всех вакансий
                for key, value in vacancy.items():  # элементы вакансии
                    if not d_dict.get(key):
                        d_dict[key] = set()
                        d_dict[key].add(type(value))
                    elif not type(value) in d_dict.get(key):
                        d_dict[key].add(type(value))
    cursor.close()
print(d_dict)