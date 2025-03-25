import os
import pymysql
from urllib.request import urlopen
import re
import requests


#Fixing Error One (Data Base should be from an ENV file.)
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'mydatabase')
}


#Fixing Error 2 (Validate your input and escape special characters)
def get_user_input():
    while True:
        user_input = input('Enter your name: ').strip()

        # Validate length (e.g., between 1 and 50 characters)
        if len(user_input) < 1 or len(user_input) > 50:
            print("Error: Name must be between 1 and 50 characters.")
            continue

        # Validate allowed characters (only letters and spaces)
        if not re.match(r'^[A-Za-z\s]+$', user_input):
            print("Error: Name can only contain letters and spaces.")
            continue

        return user_input


def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')



#Fixing Error 3 (Validate your input and escape special characters)
def get_data():
    url = 'https://secure-api.com/get-data'
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    


def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
