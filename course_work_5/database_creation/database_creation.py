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
        DROP TABLE IF EXISTS vacancy;
        DROP TABLE IF EXISTS area;
        DROP TABLE IF EXISTS salary;
        DROP TABLE IF EXISTS type_;
        DROP TABLE IF EXISTS address;
        DROP TABLE IF EXISTS employer;
        """)

        # Создаем новую таблицу.
        cursor.execute(f"""
        
        CREATE TABLE area(
        area_id SERIAL PRIMARY KEY,
        id_ INT NOT NULL, --modified name
        name_ VARCHAR(50), --modified name
        url VARCHAR(100) NOT NULL
        );
        
        CREATE TABLE salary(
        salary_id SERIAL PRIMARY KEY,
        from_ real, --modified name
        to_ real, --modified name
        currency VARCHAR(5) NOT NULL,
        gross BOOL NOT NULL
        );
        
        CREATE TABLE type_(
        type_id SERIAL PRIMARY KEY,
        id_ VARCHAR(10) NOT NULL, --modified name
        name_ VARCHAR(20) NOT NULL --modified name
        );
        
        CREATE TABLE address(
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
        
        CREATE TABLE employer (
        employer_id SERIAL PRIMARY KEY NOT NULL,
        id_ INT NOT NULL, --modified name
        name_ VARCHAR(100) NOT NULL, --modified name
        url VARCHAR(100) NOT NULL,
        alternate_url VARCHAR(100) NOT NULL,
        logo_urls TEXT,
        vacancies_url VARCHAR(100),
        accredited_it_employer BOOL,
        trusted_ BOOL --modified name
        );
        
        CREATE TABLE vacancy (id_ int PRIMARY KEY, --modified name
        premium BOOL NOT NULL,
        name_ VARCHAR(100) NOT NULL, --modified name
        area_id INT NOT NULL, --перепроверить на необходимость NULL
        salary_id INT NOT NULL,  --перепроверить на необходимость NULL
        type_id INT NOT NULL, --modified name
        address_id INT NOT NULL, --перепроверить на необходимость NULL
        published_at TIMESTAMP NOT NULL,
        created_at TIMESTAMP NOT NULL,
        url VARCHAR(200) NOT NULL,
        alternate_url VARCHAR(200) NOT NULL,
        employer_id INT NOT NULL, --перепроверить на необходимость NULL
        FOREIGN KEY (area_id) REFERENCES area(area_id), 
        FOREIGN KEY (salary_id) REFERENCES salary(salary_id),
        FOREIGN KEY (type_id) REFERENCES type_(type_id),
        FOREIGN KEY (address_id) REFERENCES address(address_id),
        FOREIGN KEY (employer_id) REFERENCES employer(employer_id)
        );
        """)
        connection.commit()

        for company_vacancies in data_vacancies:  # Список компаний
            for vacancy in company_vacancies:  # Список вакансий

                # добавляем данные в таблицы
                add_area = (vacancy['area']['id'], vacancy['area']['name'], vacancy['area']['url'])
                cursor.execute(f"""
                INSERT INTO area (id_, name_, url) VALUES (%s, %s, %s) returning *;
                """, add_area)

                # Если значение ключа salary None, то вносим вручную данные в таблицу.
                if vacancy.get('salary'):
                    add_salary = (vacancy['salary']['from'], vacancy['salary']['to'], vacancy['salary']['currency'],
                                  vacancy['salary']['gross'])
                else:
                    add_salary = (0, 0, 'null', 'false')
                cursor.execute(f"""
                INSERT INTO salary (from_, to_, currency, gross) VALUES (%s, %s, %s, %s) returning *;
                """, add_salary)

                add_type = (vacancy['type']['id'], vacancy['type']['name'])
                cursor.execute(f"""
                                INSERT INTO type_ (id_, name_) VALUES (%s, %s) returning *;
                                """, add_type)
                if vacancy.get('address'):
                    add_address = (
                        vacancy['address']['city'], vacancy['address']['street'], vacancy['address']['building'],
                        vacancy['address']['lat'], vacancy['address']['lng'], vacancy['address']['description'],
                        vacancy['address']['raw'], vacancy['address']['id'])
                    cursor.execute(f"""
                                INSERT INTO address(city, street, building, lat, lng, description, raw, id_) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) returning *;
                                """, add_address)
                else:
                    cursor.execute(f"""
                                INSERT INTO address(id_) VALUES (0) returning *;
                                """, add_address)

                add_employer = (
                    vacancy['id'], vacancy['name'], vacancy['url'], vacancy['alternate_url'],
                    vacancy.get('logo_urls'), vacancy.get('vacancies_url'), vacancy.get('accredited_it_employer'),
                    vacancy.get('trusted'))
                cursor.execute(f"""
                                INSERT INTO employer(id_, name_, url, alternate_url, logo_urls, vacancies_url, 
                                accredited_it_employer, trusted_) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) returning *;
                                """, add_employer)

                add_vacancy = (
                    vacancy['id'], vacancy['premium'], vacancy['name'], vacancy['published_at'], vacancy['created_at'],
                    vacancy['url'], vacancy['alternate_url'])
                cursor.execute(f"""
                                INSERT INTO vacancy(id_, premium, name_, published_at, created_at, url, alternate_url)
                                VALUES (%s, %s, %s, %s, %s, %s, %s) returning *;
                                """, add_vacancy)
                connection.commit()
connection.close()
