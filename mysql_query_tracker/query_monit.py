import MySQLdb
import pickle
from sys import argv
"""(('Com_delete', '1'), ('Com_insert', '3'), ('Com_select', '44'), ('Com_update', '1'))"""
qry_exec = """show global status where Variable_name in ("Com_select","Com_Insert", "Com_update","Com_delete");"""
arg_a = int(argv[1])
arg_b = int(argv[2])


def file_picker(req_file):
    return {
        0: '/home/ubuntu/scripts/mysql_query_tracker/delete_db',
        1: '/home/ubuntu/scripts/mysql_query_tracker/insert_db',
        2: '/home/ubuntu/scripts/mysql_query_tracker/select_db',
        3: '/home/ubuntu/scripts/mysql_query_tracker/update_db'
    }.get(req_file)


def wrt_pkle(file_name_write, dump_value):
    with open(file_name_write, 'wb') as FileOpenForWrite:
        pickle.dump(dump_value, FileOpenForWrite)


def read_pkle(file_name_read):
    with open(file_name_read, 'rb') as FileOpenForRead:
        old_stats_val = pickle.load(FileOpenForRead)
    return old_stats_val


def destroy_pkle(file_name_empty):
    open(file_name_empty, 'w').close()


def query_calculator(new_val, old_val):
    cur_stats = int(new_val - old_val)
    return cur_stats


def query_calculator_store(new_val_after_Cal, old_val):
    cur_stats_to_store = new_val_after_Cal + old_val
    return cur_stats_to_store

def con_to_db(exec_query):
    con_db = MySQLdb.connect('localhost', 'root', 'root', 'temp')
    cursor = con_db.cursor()
    cursor.execute(exec_query)
    query_out = cursor.fetchall()
    return query_out


val_stats = con_to_db(qry_exec)
print (arg_a, arg_b)
print (val_stats)
print (val_stats[arg_a][arg_b])
val_stm = int(val_stats[arg_a][arg_b])
file_to_be_access = file_picker(arg_a)
old_stats = read_pkle(file_to_be_access)
new_stats = query_calculator(val_stm, old_stats)
destroy_pkle(file_to_be_access)
new_stats_tobe_stored = query_calculator_store(new_stats,old_stats)
wrt_pkle(file_to_be_access, new_stats_tobe_stored)
print (new_stats)
print (new_stats_tobe_stored)