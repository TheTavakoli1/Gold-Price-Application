import sqlite3

def Data():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (GoldPrice INT, Weight INT, Wages INT,
                    Profit INT, Tax INT, TotalPrice INT)''')
    connect.commit()
    connect.close()

Data()
