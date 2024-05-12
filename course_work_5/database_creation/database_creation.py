import os
import json
from source.constants import path_for_ids, path_for_vacancies, path_for_companies
#########################################################
#Data file fetch, database creation, save to database tables
#########################################################

with open(path_for_companies, mode='r', encoding='utf-8') as f:
    data_companies = json.load(f)
with open(path_for_vacancies, mode='r', encoding='utf-8') as f:
    data_vacancies = json.load(f)

for company_vacancies in data_vacancies:  # Список компаний
    for vacancy in company_vacancies:  # Список вакансий у компании
        d_dict = dict()
        for key, value in vacancy.items():  # элементы вакансии
            pass
        print(vacancy)