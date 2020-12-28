import sqlite3

class DBM:

    def __init__(self):
        try:
            self.con = sqlite3.connect('myjobs.db')
            print("[ Success ] Database is now connected")
        except Exception as e:
            print(e)

    def get_connection(self):
        return self.con

    def create_jobs_table(self):
        db_cursor = self.con.cursor()
        query_string = '''
        CREATE TABLE jobs(
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name text NOT NULL,
            posting_position text NOT NULL,
            posting_number text,
            contact_email text,
            contact_phone text,
            city text NOT NULL,
            province text NOT NULL,
            posting_site text NOT NULL,
            search_position text NOT NULL,
            job_ur BLOB NOT NULL,
            posting_date text NOT NULL DEFAULT CURRENT_DATE,
            access_date text NOT NULL
        )
        '''
        try:
            db_cursor.execute(query_string)
            self.con.commit()
            print("[ Success ] Database table 'jobs' was created.")
        except Exception as e:
            print(f"[ Error ] {e}")
        
        