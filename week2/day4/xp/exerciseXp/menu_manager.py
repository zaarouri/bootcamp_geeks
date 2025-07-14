import psycopg2
from menu_item import MenuItem

# Reuse database connection settings
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'restaurant'

def get_connection():
    return psycopg2.connect(
        host=HOSTNAME,
        user=USERNAME,
        password=PASSWORD,
        dbname=DATABASE
    )

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT item_name, item_price FROM menu WHERE item_name = %s;", (name,))
            row = cur.fetchone()
            return MenuItem(*row) if row else None
        finally:
            cur.close()
            conn.close()

    @classmethod
    def all_items(cls):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT item_name, item_price FROM menu ORDER BY id;")
            rows = cur.fetchall()
            return [MenuItem(name, price) for name, price in rows]
        finally:
            cur.close()
            conn.close()