import psycopg2

# Database connection parameters
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'restaurant'

connection = psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname=DATABASE
)

cursor = connection.cursor()

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        try:
            cursor.execute("INSERT INTO menu (item_name, item_price) VALUES (%s, %s);", (self.item_name, self.item_price))
            connection.commit()
            print(f"✅ '{self.item_name}' added.")
        except Exception as e:
            print("❌ Error saving item:", e)

    def update(self, new_name, new_price):
        try:
            cursor.execute("UPDATE menu SET item_name = %s, item_price = %s WHERE item_name = %s;", (new_name, new_price, self.item_name))
            connection.commit()
            print(f"✅ '{self.item_name}' updated to '{new_name}' with price {new_price}")
            self.item_name = new_name
            self.item_price = new_price
        except Exception as e:
            print("❌ Error updating item:", e)

    def delete(self):
        try:
            cursor.execute("DELETE FROM menu WHERE item_name = %s;", (self.item_name,))
            connection.commit()
            print(f"✅ '{self.item_name}' deleted.")
        except Exception as e:
            print("❌ Error deleting item:", e)

    @staticmethod
    def show_menu():
        try:
            cursor.execute("SELECT * FROM menu")
            results = cursor.fetchall()
            print("\n📋 Current Menu:")
            for row in results:
                print(f"{row[0]}: {row[1]} - {row[2]} dh")
        except Exception as e:
            print("❌ Error showing menu:", e)
    