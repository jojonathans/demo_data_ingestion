# host : 35.222.95.127
# user : postgres
# password : P@ssw0rd
# database: postgres
import psycopg2 as pg 
host  = '35.222.95.127' 
port  = "5432"
database = "postgres"
user = "postgres"
password="P@ssw0rd"
dsn = "dbname=" +database + " user=" + user + " host=" + host + " port=" + port + " password=" + password

conn = pg.connect(dsn)

#select
def read_from_db(conn , query):
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

#insert
def exec_db(conn,query,data=None):
    cur = conn.cursor()
    cur.execute(query,data)
    conn.commit()
    cur.close()

def read_customer():
    query =  """
        select 
        customer_id,
        customer_unique_id,
        customer_zip_code_prefix,
        customer_city,
        customer_state 
        from olist_customers_dataset_csv 
        limit 100
    """
    data = read_from_db(conn,query)
    allrows = []
    for row in data:
        elmt = {}
        elmt["customer_id"] = row[0]
        elmt["customer_unique_id"] = row[1]
        elmt["customer_zip_code_prefix"] = row[2]
        elmt["customer_city"] = row[3]
        elmt["customer_state"] = row[4]
        allrows.append(elmt)
    return allrows

# data = read_customer()
# print(data)

def write_customer():
    query = """
        insert into olist_customers_dataset_csv(customer_id,customer_unique_id,customer_zip_code_prefix,customer_city,customer_state )
        values(%s,%s,%s,%s,%s)
    """
    exec_db(conn,query ,('666','666','666','asd','as'))
    print("berhasil insert data")

write_customer();

def update_customer():
    query = """
        update olist_customers_dataset_csv set customer_city = 'halo'
        where customer_id = '666'
    """
    exec_db(conn,query)
    print("berhasil update data")
update_customer()