import pymysql as sql
from cnf import config
from domains import domains
import os

def delete_all_data_do_not_use_in_prod():
    if os.environ.get( 'TOOLFORGE' ):
        raise f'This seems like a production system, please refrain from resetting the database'
    with get_conn().cursor() as cursor:
        cursor.execute('DROP TABLE stats_sr,stats_de,stats_hu,stats_old,stats_nap,stats_gl,stats_fo,stats_or,stats_vi,stats_en,stats_ro,stats_eu,stats_lij,stats_bn,stats_az,stats_lt,stats_sk,stats_pms,stats_da,stats_zh,`stats_zh-min-nan`,stats_ban,stats_eo,stats_no,stats_bg,stats_hi,stats_it,stats_hr,stats_br,stats_vec,stats_fi,stats_ta,stats_fa,stats_et,stats_mr,stats_cs,stats_fr,stats_pa,stats_as,stats_ar,stats_he,stats_es,stats_ml,stats_bs,stats_sv,stats_kn,stats_hy,stats_yi,stats_pt,stats_sl,stats_gu,stats_be,stats_cy,stats_ru,stats_la,stats_ko,stats_wa,stats_jv,stats_sa,stats_el,stats_ja,stats_pl,stats_nl,stats_uk,stats_sah,stats_th,stats_te,stats_ca,stats_li,stats_mk,stats_is,stats_id,stats_tr;')

def init_db():
    initdbconn = sql.connections.Connection(user=config['username'], password=config['password'], host=config['host'])
    with initdbconn.cursor() as cursor:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {config["username"]}__wsstats_p;')
        cursor.execute(f'USE {config["username"]}__wsstats_p')
        for domain in domains:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS `stats_{domain}` (
                        time datetime NOT NULL,
                        num_of_pages int NOT NULL,
                        num_of_q0 int NOT NULL,
                        num_of_q1 int NOT NULL,
                        num_of_q2 int NOT NULL,
                        num_of_q3 int NOT NULL,
                        num_of_q4 int NOT NULL,
                        num_of_trans int NOT NULL,
                        num_of_disambig int NOT NULL,
                        PRIMARY KEY(time)
                        );''')
    initdbconn.close()
    
def get_conn():
    dbconn = sql.connections.Connection(user=config['username'], password=config['password'], host=config['host'], database=f'{config["username"]}__wsstats_p')
    return dbconn
