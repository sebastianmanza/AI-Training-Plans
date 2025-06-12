import psycopg2

class database_connect:
    @staticmethod
    def init_db():
        try:
            # Establish connection
            conn = psycopg2.connect(database = "UserListAi",
                                    user = "postgres",
                                    host = "localhost",
                                    password = "Control1500#",
                                    port = "5432")
            return conn
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            return None