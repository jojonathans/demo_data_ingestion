# import psycopg2

# conn    = psycopg2.connect(host='digitalskola7-do-user-7592846-0.b.db.ondigitalocean.com', dbname='deadpool', user='doadmin', password='AVNS_TDrSDUoeoSNF5rVVSLx', port='25061')
# curr     = conn.cursor()
# csv_file = open('D:\Jonathan\Digital Skola\Week 5\jonathan_products.csv' , 'w')
# sql     = 'COPY (select * from products) TO STDOUT WITH CSV HEADER'
# curr.copy_expert(sql , csv_file)
# csv_file.close()
# curr.close()
# conn.close()
import psycopg2
import os

SQL_USER = os.environ.get('OLTP_USERNAME')
SQL_PASS = os.environ.get('OLTP_PASSWORD')
SQL_HOST = os.environ.get('OLTP_HOST')
SQL_PORT = os.environ.get('OLTP_PORT')
SQL_DB = os.environ.get('OLTP_DATABASE')

conn = psycopg2.connect(host=SQL_HOST, dbname=SQL_DB, user=SQL_USER, password=SQL_PASS, port=SQL_PORT)
cur = conn.cursor()
sql = 'COPY (select * from products) TO STDOUT WITH CSV HEADER'
csv_file = open('D:\Jonathan\Digital Skola\Week 5\jonathan_products.csv' , 'w')
cur.copy_expert(sql,csv_file)
csv_file.close()
cur.close
conn.close

