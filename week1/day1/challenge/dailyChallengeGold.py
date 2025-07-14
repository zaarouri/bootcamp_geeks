from datetime import datetime

birthdate = input("Enter your birthdate (DD-MM-YYYY): ")

try:
    day, month, year = map(int, birthdate.split('-'))
    today = datetime.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    last_digit = age % 10

    cake = f"""
       {' 🕯️ ' * last_digit}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
    """

    print(cake)

    # Leap year check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(cake)

except:
    print("Invalid format. Please use DD-MM-YYYY.")
