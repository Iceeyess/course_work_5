import psycopg2
import json
from source.constants import path_for_vacancies, path_for_companies

#########################################################
# Data file fetch, database creation, save to database tables
#########################################################

with open(path_for_companies, mode='r', encoding='utf-8') as f:
    data_companies = json.load(f)
with open(path_for_vacancies, mode='r', encoding='utf-8') as f:
    data_vacancies = json.load(f)

params = dict(host='localhost', database='course_work_5', port=5432, user='postgres', password='Herbalife1', )
with psycopg2.connect(**params) as connection:
    with connection.cursor() as cursor:
        # Словарь для формирования возможных ключей и, возможных типов значений.
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
        #  Удаляем старые таблицы, если ранее существовали.
        cursor.execute(f"""
        DROP TABLE IF EXISTS areas;
        DROP TABLE IF EXISTS salaries;
        DROP TABLE IF EXISTS types;
        DROP TABLE IF EXISTS addresses;
        DROP TABLE IF EXISTS employers;
        DROP TABLE IF EXISTS vacancies;
        """)

        # Создаем новую таблицу.
        cursor.execute(f"""
        
        CREATE TABLE vacancies (vacancy_id INT PRIMARY KEY, --modified name
        premium BOOL NOT NULL,
        name_ VARCHAR(100) NOT NULL, --modified name
        area_id SERIAL NOT NULL, 
        salary_id SERIAL NOT NULL, 
        type_id SERIAL NOT NULL, --modified name
        address_id SERIAL NOT NULL, 
        published_at TIMESTAMP NOT NULL,
        created_at TIMESTAMP NOT NULL,
        url VARCHAR(200) NOT NULL,
        alternate_url VARCHAR(200) NOT NULL,
        employer_id SERIAL NOT NULL
        );
        
        CREATE TABLE areas(
        vacancy_id INT REFERENCES vacancy(vacancy_id),
        area_id SERIAL,
        id_ INT NOT NULL, --modified name
        name_ VARCHAR(50), --modified name
        url VARCHAR(100) NOT NULL
        );
        
        CREATE TABLE salaries(
        vacancy_id INT REFERENCES vacancy(vacancy_id),
        salary_id SERIAL PRIMARY KEY,
        from_ real, --modified name
        to_ real, --modified name
        currency VARCHAR(5) NOT NULL,
        gross BOOL NOT NULL
        );
        
        CREATE TABLE types(
        vacancy_id INT REFERENCES vacancy(vacancy_id),
        type_id SERIAL PRIMARY KEY,
        id_ VARCHAR(10) NOT NULL, --modified name
        name_ VARCHAR(20) NOT NULL --modified name
        );
        
        CREATE TABLE addresses(
        vacancy_id INT REFERENCES vacancy(vacancy_id),
        address_ID SERIAL PRIMARY KEY,
        city VARCHAR(100),
        street VARCHAR(100),
        building VARCHAR(100),
        lat DOUBLE PRECISION,
        lng DOUBLE PRECISION,
        description TEXT,
        raw TEXT,
        id_ INT NOT NULL
        );
        
        CREATE TABLE employers (
        vacancy_id INT REFERENCES vacancy(vacancy_id),
        employer_id SERIAL PRIMARY KEY NOT NULL,
        company_id INT NOT NULL, --modified name
        name_ VARCHAR(100) NOT NULL, --modified name
        url VARCHAR(100) NOT NULL,
        alternate_url VARCHAR(100) NOT NULL,
        logo_urls TEXT NOT NULL,
        vacancies_url VARCHAR(100),
        accredited_it_employer BOOL,
        trusted_ BOOL --modified name
        );
        
        """)
        connection.commit()

        for company_vacancies in data_vacancies:  # Список компаний
            for vacancy in company_vacancies:  # Список вакансий

                #  добавляем данные в таблицы
                #  vacancy table
                add_vacancy = (
                    vacancy['id'], vacancy['premium'], vacancy['name'], vacancy['published_at'], vacancy['created_at'],
                    vacancy['url'], vacancy['alternate_url'])
                cursor.execute(f"""
                                INSERT INTO vacancies(vacancy_id, premium, name_, published_at, created_at, url, 
                                alternate_url) VALUES (%s, %s, %s, %s, %s, %s, %s) returning *;
                                """, add_vacancy)
                #  area table
                add_area = (vacancy['id'], vacancy['area']['id'], vacancy['area']['name'], vacancy['area']['url'])
                cursor.execute(f"""
                INSERT INTO areas (vacancy_id, id_, name_, url) VALUES (%s, %s, %s, %s) returning *;
                """, add_area)

                # salary table. Если значение ключа salary None, то вносим вручную данные в таблицу.
                if vacancy.get('salary'):
                    add_salary = (
                    vacancy['id'], vacancy['salary']['from'], vacancy['salary']['to'], vacancy['salary']['currency'],
                    vacancy['salary']['gross'])
                else:
                    add_salary = (vacancy['id'], 0, 0, 'null', 'false')
                cursor.execute(f"""
                INSERT INTO salaries (vacancy_id, from_, to_, currency, gross) VALUES (%s, %s, %s, %s, %s) returning *;
                """, add_salary)
                # type table
                add_type = (vacancy['id'], vacancy['type']['id'], vacancy['type']['name'])
                cursor.execute(f"""
                                INSERT INTO types (vacancy_id, id_, name_) VALUES (%s, %s, %s) returning *;
                                """, add_type)
                #  address table
                if vacancy.get('address'):
                    add_address = (vacancy['id'], vacancy['address']['city'], vacancy['address']['street'],
                                   vacancy['address']['building'], vacancy['address']['lat'], vacancy['address']['lng'],
                                   vacancy['address']['description'], vacancy['address']['raw'],
                                   vacancy['address']['id'])
                    cursor.execute(f"""
                                INSERT INTO addresses(vacancy_id, city, street, building, lat, lng, description, raw, 
                                id_) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning *;
                                """, add_address)
                else:
                    cursor.execute(f"""
                                INSERT INTO addresses(id_) VALUES (0) returning *;
                                """, add_address)
                # employer table
                add_employer = (
                    vacancy['id'], vacancy['employer'].get('id'), vacancy['employer'].get('name'),
                    vacancy['employer'].get('url'), vacancy['employer'].get('alternate_url'),
                    str(vacancy['employer'].get('logo_urls')), vacancy['employer'].get('vacancies_url'),
                    vacancy['employer'].get('accredited_it_employer'), vacancy['employer'].get('trusted'))
                cursor.execute(f"""
                                INSERT INTO employers(vacancy_id, company_id, name_, url, alternate_url, logo_urls, 
                                vacancies_url, accredited_it_employer, trusted_) VALUES 
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning *;
                                """, add_employer)

                connection.commit()
connection.close()
