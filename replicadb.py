import pymysql as sql
from cnf import config
import os

server_lastpart = '.analytics.db.svc.wikimedia.cloud'

def get_conn(dom):
    dom =  dom.replace('-', '_')
    dbname = f'{dom}wikisource'
    if dom == 'old':
        dbname = 'sourceswiki'
    dbconn = sql.connections.Connection(user=os.environ.get( 'TOOL_REPLICA_USER' ), password=os.environ.get( 'TOOL_REPLICA_PASSWORD' ), host=f'{dbname}{server_lastpart}', database=f'{dbname}_p')
    return dbconn