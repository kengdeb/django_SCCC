
import os
import sys
import ntpath

def connectDB(db_name):
    import pyodbc
    conn=False ;error=''
    try: #Do not put a space after the Driver keyword in the connection string
        conn_str='DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql-supplychain.database.windows.net;DATABASE='+db_name+';'\
                    'UID=scccadm;PWD=P@ssw0rd@1;' #'Trusted_Connection=yes;' #'autocommit=True')
        conn = pyodbc.connect(conn_str)
    except Exception as e: error=str(e)
    if not conn: print('Error, did not connect DB by pyodbc.connect(conn_str)',error)
    return conn

def sql_execute_query(db_name,query,sql_var=None,is_print_query=False): #if no paremeter, set to None
    import pandas as pd
    #---1. Set parameters for query
    if query=='' or db_name=='': return None #if sql_var={}, sql_var.values()=[]
    sql_var=None if isinstance(sql_var,dict) and not sql_var else sql_var
    params=list(sql_var.values()) if isinstance(sql_var,dict) else sql_var #sql_var.items()
    df=None
    conn=connectDB(db_name)#.connect()
    if not conn: return None
    try:
        cursor=conn.cursor()
        if params is None : rows=cursor.execute(query).fetchall()
        else: rows=cursor.execute(query,params).fetchall() #SQL Server format-->#while rows: print(rows)
        #print('yyyyyyyy Complete {}...'.format(query[:200]))
        #-------------------------------------
        columns=[column[0] for column in cursor.description] #must before move cursor
        df=pd.DataFrame.from_records(rows,columns=columns) #df=pd.read_sql(sql=query,con=conn,params=params)
        print('**********ttttttttttt')
        if is_print_query:
            # print(f"------Execute query----- \n{query} \nWith param; {params}")
            if cursor.nextset():
                try: print('------Query -----',cursor.fetchall()[0][0])
                except Exception as e:
                    print('zzzzzzzz Error when print query',e)
                    return None

        cursor.commit() #need when update db ,ex.'delete_predo_shipment'
    except Exception as e:
        print('zzzzzzzz Error; cannot execute {} :: {}'.format(query,e))
    finally:
        cursor.close()
        conn.close()
    # df=filter_columns(df)
    return df


# query='select top 10 * from shipmenttracking'
# df=sql_execute_query('sqldb-datawarehouse',query,None,True)
# print(df)
