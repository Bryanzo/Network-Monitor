# lets Python work with SQL databases
import sqlite3

# lets Python run terminal commands like ping
import subprocess


# list of devices we want to monitor
devices = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]


# connect to database
# this creates network.db if it does not exist
connection = sqlite3.connect("/Users/bryansackey/network.db")


# cursor lets Python execute SQL commands
cursor = connection.cursor()


# delete old devices table if it already exists
cursor.execute("DROP TABLE IF EXISTS devices")


# create a fresh table
cursor.execute("""
CREATE TABLE devices (
    id INTEGER PRIMARY KEY,
    ip TEXT,
    status TEXT
)
""")


# loop through every IP address
for ip in devices:

    # run ping command
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # determine if device is UP or DOWN
    if result.returncode == 0:
        status = "UP"
    else:
        status = "DOWN"


    # insert device status into SQL database
    cursor.execute("""
    INSERT INTO devices (ip, status)
    VALUES (?, ?)
    """, (ip, status))


    # print result to screen
    print(f"{ip} is {status}")


# save changes to database
connection.commit()


# retrieve all database rows
cursor.execute("SELECT * FROM devices")

rows = cursor.fetchall()


print("\nDatabase Records:\n")


# print each row from database
for row in rows:
    print(row)


# close database connection
connection.close()