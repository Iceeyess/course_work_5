import os

# Список компаний, который можно менять вручную
hh_company_names = ['МТС Банк', 'Почта Банк', 'Банк Русский Стандарт', 'Промсвязьбанк', 'Банк ВТБ', 'Банк России',
                    'Альфа-банк', 'Тинькофф Банк', 'Россельхозбанк', 'Газпромбанк']

employee_id_API = 'https://api.hh.ru/employers/'  #  API ссылка на получение данных о работодателе
vacancies_API = 'https://api.hh.ru/vacancies/' #  API ссылка на получение данных о вакансиях