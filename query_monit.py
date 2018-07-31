import MySQLdb
import sys
def wrt_pkle():
def read_pkle():
def destroy_pkle():
def query_calculator():
def con_to_db(exec_query):
    con_db = MySQLdb.connect('localhost', 'root', 'root', 'temp')
    cursor = con_db.cursor()
    cursor.execute(exec_query)
    query_out = cursor.fetchall()
    return query_out
val_stats=con_to_db('show global status where Variable_name in ("Com_select","Com_Insert", "Com_update","Com_delete");')
#val_insert=con_to_db('show global status like "Com_update";')
#val_delete=con_to_db('show global status like "Com_insert";')
#val_update=con_to_db('show global status like "Com_delete";')
arg_a = int(sys.argv[1])
arg_b = int(sys.argv[2])
print (arg_a,arg_b)
print (val_stats)
print (val_stats[arg_a][arg_b])
val_stm = val_stats[arg_a][arg_b]
#print (val_insert)[0][1]
#print (val_delete)[0][1]
#print (val_update)[0][1]