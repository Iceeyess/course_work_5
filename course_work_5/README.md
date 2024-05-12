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
Данный проект создает базу данных из данных полученных по API, которые состоят из подтаблиц.
Данные имеют следующую структуру:
1) 'id': '98541299', 
2) 'premium': False, 
3) 'name': 'Менеджер проектов по маркетингу', 
4) 'department': 
4.1) {'id': '4496-4496-office', 'name': 'МТС Банк. Головной офис'}, 
5) 'has_test': False, 
6) 'response_letter_required': False, 
7) 'area': 
7.1) {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1' }, 
8) 'salary': None, 
9) 'type': 
9.1) {'id': 'open', 'name': 'Открытая'}, 
10) 'address': 
10.1) {'city': 'Москва', 'street': 'проспект Андропова', 'building': '18к1', 'lat': 55.695027, 'lng': 37.662812, 'description': None, 'raw': 'Москва, проспект Андропова, 18к1', 'metro': None, 'metro_stations': [], 'id': '470181'}, 
11) 'response_url': None, 
12) 'sort_point_distance': None, 
13) 'published_at': '2024-05-07T12:41:49+0300', 
14) 'created_at': '2024-05-07T12:41:49+0300', 
15) 'archived': False, 
16) 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=98541299', 
17) 'branding': 
17.1) {'type': 'MAKEUP', 'tariff': None}, 
18) 'show_logo_in_search': True, 
19) 'insider_interview': None, 
20) 'url': 'https://api.hh.ru/vacancies/98541299?host=hh.ru', 
21) 'alternate_url': 'https://hh.ru/vacancy/98541299', 
22) 'relations': [], 
23) 'employer': 
23.1) {'id': '4496', 'name': 'МТС Финтех', 'url': 'https://api.hh.ru/employers/4496', '
alternate_url': 'https://hh.ru/employer/4496', 'logo_urls': 
23.2) {'240': 'https://img.hhcdn.ru/employer-logo/3091701.png', '
90': 'https://img.hhcdn.ru/employer-logo/3091700.png', '
original': 'https://img.hhcdn.ru/employer-logo-original/662642.png'}, '
vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4496', 'accredited_it_employer': False, 'trusted': True}, 
24) 'snippet': 
24.1) {'requirement': 'Знание инструментов маркетинга и умение их применять. Хорошая коммуникация. Инициативность.
Организованность.', 'responsibility': 'Поддержка продуктовых запусков: постановка задач смежным командам для создания
визуальной и текстовой коммуникации, и контроль их исполнения. Контроль и актуализация...'}, 
25) 'contacts': None, 
26) 'schedule': 
26.1) {'id': 'fullDay', 'name': 'Полный день'}, 
27) 'working_days': [], 
28) 'working_time_intervals': [], 
29) 'working_time_modes': [], 
30) 'accept_temporary': False, 
31) 'professional_roles':
31.1)[{'id': '68', 'name': 'Менеджер по маркетингу, интернет-маркетолог'}], 
32) 'accept_incomplete_resumes': False, 
33) 'experience': 
33.1) {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 
34) 'employment': 
34.1) {'id': 'full', 'name': 'Полная занятость'}, 
35) 'adv_response_url': None, 
36) 'is_adv_vacancy': False, 
37) 'adv_context': None
