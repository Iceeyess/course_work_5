from source.funcs import get_id_employees
from source.funcs import get_companies_description
from source.funcs import get_vacancies
from source.constants import path_for_ids, path_for_vacancies, path_for_companies
from source.constants import hh_company_names, employee_id_API, vacancies_API
import json


#Data retrieves and saves to files
#####################################################

id_employees_list = get_id_employees(hh_company_names, employee_id_API)
get_employers_list = get_companies_description(id_employees_list, employee_id_API)
get_vacancy_list = get_vacancies(id_employees_list, vacancies_API)


with open(path_for_ids, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(id_employees_list, ensure_ascii=False, indent=2))
with open(path_for_companies, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(get_employers_list, ensure_ascii=False, indent=2))
with open(path_for_vacancies, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(get_vacancy_list, ensure_ascii=False, indent=2))


