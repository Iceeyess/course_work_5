from source.dbmanager import DBManager

if __name__ == '__main__':
    db_conn = DBManager()
    with db_conn:
        db_conn.get_vacancies_with_keyword('Python', 'Курьер')