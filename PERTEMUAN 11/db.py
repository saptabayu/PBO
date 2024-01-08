import mysql.connector as mc

class DBConnection:

    def __init__(self):
        self.host = "sql.freedb.tech"
        self.port = 3306
        self.name = "freedb_dbkampusss"
        self.user = "freedb_Sapta Bayu Permana"
        self.password = "3aGpVnS$z7KZQkr"
        self.conn = None
        self.cursor = None
        self.connected = False
        self.affected = 0
        self.connect()

    @property
    def connection_status(self):
        return self.connected

    def connect(self):
        try:
            self.conn = mc.connect(host=self.host, port=self.port, database=self.name, user=self.user,
                                   password=self.password)

            self.connected = True
            self.cursor = self.conn.cursor()
        except mc.Error as e:
            self.connected = False
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False
        else:
            self.conn = None

    def execute_query(self, sql, fetch=True):
        self.connect()
        self.cursor.execute(sql)
        if fetch:
            return self.cursor.fetchall()
        else:
            self.conn.commit()
            self.affected = self.cursor.rowcount
            return self.affected

    def findOne(self, sql):
        return self.execute_query(sql, fetch=True)

    def findAll(self, sql):
        return self.execute_query(sql, fetch=True)

    def insert(self, sql):
        return self.execute_query(sql, fetch=False)

    def update(self, sql, val):
        self.connect()
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def delete(self, sql):
        return self.execute_query(sql, fetch=False)

    def show(self, sql):
        return self.execute_query(sql, fetch=True)

    @property
    def info(self):
        if self.connected:
            return f"Server is running on {self.host} using port {self.port}"
        else:
            return "Server is offline."

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

# Test koneksi database
with DBConnection() as db:
    result = db.info
    print(result)