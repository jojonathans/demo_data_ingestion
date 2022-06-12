import psycopg2

conn    = psycopg2.connect(host='digitalskola7-do-user-7592846-0.b.db.ondigitalocean.com', dbname='deadpool', user='doadmin', password='AVNS_TDrSDUoeoSNF5rVVSLx', port='25061')
curr     = conn.cursor()
csv_file = open('D:\Jonathan\Digital Skola\Week 5\jonathan_products.csv' , 'w')
sql     = 'COPY (select * from products) TO STDOUT WITH CSV HEADER'
curr.copy_expert(sql , csv_file)
csv_file.close()
curr.close()
conn.close()

