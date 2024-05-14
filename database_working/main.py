from source.dbmanager import DBManager

if __name__ == '__main__':
    with DBManager() as db_conn:
        cur = db_conn.get_companies_and_vacancies_count()