from source.dbmanager import DBManager

if __name__ == '__main__':
    db_conn = DBManager()
    with db_conn:
        print(db_conn.get_companies_and_vacancies_count())