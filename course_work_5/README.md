Задание
Проект по БД
В рамках проекта вам необходимо получить данные о компаниях и вакансиях с сайта hh.ru, спроектировать таблицы в БД
PostgreSQL и загрузить полученные данные в созданные таблицы.

Основные шаги проекта

- Получить данные о работодателях и их вакансиях с сайта hh.ru. Для этого используйте публичный API hh.ru и библиотеку
  requests
  .
- Выбрать не менее 10 интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
- Спроектировать таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД
  используйте библиотеку
  psycopg2
  .
- Реализовать код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
- Создать класс DBManager для работы с данными в БД.

Класс DBManager

Создайте класс
DBManager
, который будет подключаться к БД PostgreSQL и иметь следующие методы:

get_companies_and_vacancies_count()
— получает список всех компаний и количество вакансий у каждой компании.

get_all_vacancies()
— получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.

get_avg_salary()
— получает среднюю зарплату по вакансиям.

get_vacancies_with_higher_salary()
— получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.

get_vacancies_with_keyword()
— получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
Класс DBManager должен использовать библиотеку psycopg2 для работы с БД.

Детали оформления решения
Проект выложен на GitHub.
Оформлен файл README.md с информацией, о чем проект, как его запустить и как с ним работать.
Есть Python-модуль для создания и заполнения данными таблиц БД.

Описание:
Данный проект создает базу данных из данных полученных по API, которые состоят из подтаблиц:
- addresses
- areas
- employers
- salaries
- types
- vacancies

Данные API ответа имеют следующую структуру и вариации данных:
1. id: {<class 'str'>}
2. premium: {<class 'bool'>}
3. name: {<class 'str'>}
4. department: {<class 'NoneType'>, <class 'dict'>}
5. has_test: {<class 'bool'>}
6. response_letter_required: {<class 'bool'>}
7. area: {<class 'dict'>}
8. salary: {<class 'NoneType'>, <class 'dict'>}
9. type: {<class 'dict'>}
10. address: {<class 'NoneType'>, <class 'dict'>}
11. response_url: {<class 'NoneType'>}
12. sort_point_distance: {<class 'NoneType'>}
13. published_at: {<class 'str'>}
14. created_at: {<class 'str'>}
15. archived: {<class 'bool'>}
16. apply_alternate_url: {<class 'str'>}
17. branding: {<class 'dict'>}
18. show_logo_in_search: {<class 'NoneType'>, <class 'bool'>}
19. insider_interview: {<class 'NoneType'>, <class 'dict'>}
20. url: {<class 'str'>}
21. alternate_url: {<class 'str'>}
22. relations: {<class 'list'>}
23. employer: {<class 'dict'>}
24. snippet: {<class 'dict'>}
25. contacts: {<class 'NoneType'>}
26. schedule: {<class 'dict'>}
27. working_days: {<class 'list'>}
28. working_time_intervals: {<class 'list'>}
29. working_time_modes: {<class 'list'>}
30. accept_temporary: {<class 'bool'>}
31. professional_roles: {<class 'list'>}
32. accept_incomplete_resumes: {<class 'bool'>}
33. experience: {<class 'dict'>}
34. employment: {<class 'dict'>}
35. adv_response_url: {<class 'NoneType'>}
36. is_adv_vacancy: {<class 'bool'>}
37. adv_context: {<class 'NoneType'>}


Для нашего проекта мы выбрали только основные данные по работодателю, которые описаны в таблицах:
- addresses:
*vacancy_id, address_ID, city, street, building, lat, lng, description, raw, id_.
- areas:
*vacancy_id, area_id, employer_area_id, name_, url
- employers:
*vacancy_id, employer_id, company_id, name_, url, alternate_url, logo_urls, vacancies_url, accredited_it_employer, trusted_.
- salaries:
*vacancy_id, premium, name_, area_id, salary_id, type_id, address_id, published_at, created_at, url, alternate_url, employer_id.
- types:
*vacancy_id, type_id, vacancy_type_id, name_.
- vacancies:
*vacancy_id, premium, name_, area_id,salary_id, vacancy_type_id, address_id, published_at, created_at, url, alternate_url, employer_id.


Все данные берутся из вложенных словарей.
*vacancy_id - ссылка на id вакансии из таблицы vacancies. Является связывающей таблицы колонкой.Все остальные ячейки берутся из вложенных словарей у API, а так же SERIAL тип данных.

Вводная часть перед применением:
Для того, чтобы создать таблицу, необходимо сначала создать таблицу "course_work_5" в локальном PSQL, или сверить их со своими данными. В таком случае меняется параметр database в переменной params.
Так же данные необходимо сверить со своими: 12 строка database_creation.py файла (Переменная params).
Если необходимо получить по специфическим работодателям данные по вакансиям, то данные меняются в файле constants.py в папке source(переменная hh_company_names). Описание остальных констант, так же в этом файле.
Лимит по вакансиям установлен в размере до 100 штук на работодателя, в функции get_vacancies, папка source file funcs.py, параметр per_page, согласно тех. документации hh.ru. 

