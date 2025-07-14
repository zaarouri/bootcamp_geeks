import psycopg2   
# ---------- exercise gold  ----------
# ---------- helper functions ----------
def add_user(cur, username: str, password: str) -> None:
    cur.execute(
        "INSERT INTO credentials (username, password) VALUES (%s, %s)",
        (username, password)
    )

def check_user(cur, username: str, password: str) -> bool:
    cur.execute(
        "SELECT 1 FROM credentials WHERE username = %s AND password = %s",
        (username, password)
    )
    return cur.fetchone() is not None


# ---------- bootstrap database ----------
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    dbname="auth"      
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS credentials (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL
    );
""")

# seed five demo users only if table is empty
cur.execute("SELECT 1 FROM credentials LIMIT 1;")
if cur.fetchone() is None:
    seed_data = [
        ('abdelmounime', '1234'),
        ('shihab',       '1234'),
        ('salma',        '1234'),
        ('marouan',      '1234'),
        ('yassmine',     '1234'),
    ]
    cur.executemany(
        "INSERT INTO credentials (username, password) VALUES (%s, %s)",
        seed_data
    )
    print("🌱 Demo users inserted.\n")

# ---------- CLI loop ----------
logged_in = None
while True:
    action = input("Type 'login', 'signup' or 'exit': ").strip().lower()

    if action == "exit":
        print("👋 Bye!")
        break

    # ---- LOGIN ----
    if action == "login":
        user = input("Username: ").strip()
        pwd  = input("Password (shown): ")

        if check_user(cur, user, pwd):
            logged_in = user
            print(f"✅ You are now logged in! Welcome, {user}.")
            break
        else:
            print("❌ Invalid username or password.")
            continue

    # ---- SIGN-UP ----
    if action == "signup":
        while True:
            new_user = input("Choose a username: ").strip()
            cur.execute("SELECT 1 FROM credentials WHERE username = %s", (new_user,))
            if cur.fetchone():
                print("Username already taken, try another.")
            else:
                break

        new_pwd = input("Choose a password: ")
        add_user(cur, new_user, new_pwd)
        logged_in = new_user
        print(f"✅ Account created! You are now logged in as {new_user}.")
        break

    print("Invalid command – please type 'login', 'signup' or 'exit'.")

cur.close()
conn.close()

# i didn't do try and except for the moment 