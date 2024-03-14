from userdb import get_conn, init_db
from datetime import datetime

def convert_everything_to_int(data: list) -> list:
    new_data = []
    for val in data:
        if type(val) is int:
            new_data.append(val)
        elif type(val) is list:
            if len(val) == 0:
                new_data.append(0)
            else:
                raise f'{val} has len() of {len(val)} which is incompatible with the universe'
        elif val is None:
            new_data.append(0)
        else:
            raise f'I don\'t know, we have this now {val}'
    return new_data


def normalize_data(tm: int, data: tuple[int]) -> tuple:
    if len(data) == 7:
        d = list(data)
        d = convert_everything_to_int(d)
        d.insert(0, datetime.utcfromtimestamp(tm).strftime('%Y-%m-%d %H:%M:%S'))
        d.append(0)
        return tuple(d)
    else:
        d = list(data)
        d = convert_everything_to_int(d)
        d.insert(0, datetime.utcfromtimestamp(tm).strftime('%Y-%m-%d %H:%M:%S'))
        return tuple(d)

def run_upload():
    init_db()
    with get_conn() as conn:
        with conn.cursor() as cursor:
            with open( 'new_stats.py' ) as f:
                for line in f.readlines():
                    tm, data = eval( line )
                    print(f' Inserting for {datetime.utcfromtimestamp(tm).strftime("%Y-%m-%d %H:%M:%S")} ')
                    for domain, values in data.items():
                        dt = normalize_data(tm, values)
                        cursor.execute(f'''INSERT INTO `stats_{domain}` (
                                time,
                                num_of_pages,
                                num_of_q0,
                                num_of_q1,
                                num_of_q2,
                                num_of_q3,
                                num_of_q4,
                                num_of_trans,
                                num_of_disambig
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', dt)
            print('Commiting')
            conn.commit()


run_upload()
