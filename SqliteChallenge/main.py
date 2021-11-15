import sqlite3

try:
    conn = sqlite3.connect("weather.sqlite")
    print("Opened database successfully.")
except Exception as e:
    print("Error opening DB:", e)

try:
    c = conn.cursor()
    c.execute("""create table samples
                    (id integer primary key autoincrement not null,
                    date text not null,
                    location text not null,
                    min_temp real not null,
                    max_temp real not null,
                    avg_temp real not null);""")
    conn.commit()
    print("Table created successfully.")
except Exception as e:
    print("Error creating table:", e)

try:
    sql = """insert into samples (date,location,min_temp,max_temp,avg_temp)
             values (?,?,?,?,?)"""
    data = ('2018-05-24', 'Winnipeg, MB', -12.6, 10.2, 5.4)
    c.execute(sql, data)
    conn.commit()
    print("Added sample successfully.")
except Exception as e:
    print("Error inserting sample.", e)

try:
    for row in c.execute("select * from samples"):
        print(row)
except Exception as e:
    print("Error fetching samples.", e)

conn.close()