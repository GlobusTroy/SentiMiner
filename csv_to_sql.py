import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='Sentiiner')
cursor = mydb.cursor()

csv_data = csv.reader(file('Tweet Data/AAPL.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO AAPL VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")',
          row)
#close the connection to the database.
cursor.close()
print "Done"
