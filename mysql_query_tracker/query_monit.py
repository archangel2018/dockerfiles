import MySQLdb
from sys import argv
"""(('Com_delete', '1'), ('Com_insert', '3'), ('Com_select', '44'), ('Com_update', '1'))"""
qry_exec = """show global status where Variable_name in ("Com_select","Com_Insert", "Com_update","Com_delete");"""
arg_a = int(argv[1])
arg_b = int(argv[2])
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


val_stats=con_to_db(qry_exec)
print (arg_a,arg_b)
print (val_stats)
print (val_stats[arg_a][arg_b])
val_stm = int(val_stats[arg_a][arg_b])
