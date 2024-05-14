import psycopg2


class DBManager:
    """Класс для работы с существующей базой данных на localhost"""

    def __init__(self, host='localhost', database='course_work_5', port=5432, username='postgres', password='Herbalife1') -> None:
        """Именные параметры уже внутри функции, однако их можно изменить на свои при создании экземпляра класса."""
        self.host = host
        self.database = database
        self.port = port
        self.user = username
        self.password = password

    def __enter__(self):
        """Создает соединение для ЭК"""
        try:
            self.conn = psycopg2.connect(**self.__dict__)
            return self.conn

        except psycopg2.OperationalError:
            print(f"Ошибка соединения с базой данных. Проверьте введенные настройки.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Выполняет коммиты и закрытие Базы данных"""
        self.conn.commit()
        self.conn.close()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        cur = self.conn.cursor()
        cur.execute("""
        SELECT e.name_, COUNT(v.vacancy_id) as quantity_vacancies
        FROM vacancies v
        INNER JOIN employers e USING(vacancy_id)
        GROUP BY e.name_;
        """)
        return cur.fetchall()