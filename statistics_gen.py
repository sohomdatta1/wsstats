from userdb import get_conn as get_user_conn
from replicadb import get_conn as get_replica_conn
from ws_category import domain_urls as urls
from domains import domains
from datetime import datetime

def catreq(cat, ns):
    return u"select /* SLOW_OK */ COUNT(cl_from) AS num FROM categorylinks WHERE cl_to='%s' AND cl_from IN (SELECT page_id FROM page WHERE page_namespace=%d)"%(cat,ns)

def propreq(vl):
    return u"SELECT /* SLOW_OK */ COUNT(pp_page) AS num FROM page_props WHERE pp_propname='proofread_page_quality_level' AND pp_value=%d"%vl

use_categories = 0

def get_stats(domains):

    import urllib
    res = {}

    for dom in domains:
        print(dom)
        try:
            conn = get_replica_conn(dom)
        except Exception as e:
            print('Not able to connect to %s' % dom)
            print(e)
            continue
        cursor = conn.cursor()
        ns = urls[dom][0]

        q=u"select /* SLOW_OK */ count(page_id) as num from page where page_namespace=%d and page_is_redirect=0"%ns
        cursor.execute(q)
        row = cursor.fetchone ()
        num_pages = int(row[0])

        if len(urls[dom])>1:
            if (use_categories):
                cat3 = urllib.parse.unquote(urls[dom][1])
                cat4 = urllib.parse.unquote(urls[dom][2])
                cursor.execute(catreq(cat3,ns))
            else:
                cursor.execute(propreq(3))
            row = cursor.fetchall()[0]
            num_q3 = int(row[0])
            if (use_categories):
                cursor.execute(catreq(cat4,ns))
            else:
                cursor.execute(propreq(4))
            row = cursor.fetchall()[0]
            num_q4 = int(row[0])
        else:
            num_q3 = 0
            num_q4 = 0

        if len(urls[dom])>3:
            if (use_categories):
                cat0 = urllib.parse.unquote(urls[dom][3])
                cat2 = urllib.parse.unquote(urls[dom][4])
                cursor.execute(catreq(cat0,ns))
            else:
                cursor.execute(propreq(0))
            row = cursor.fetchall()[0]
            num_q0 = int(row[0])
            if (use_categories):
                cursor.execute(catreq(cat2,ns))
            else:
                cursor.execute(propreq(2))
            row = cursor.fetchall()[0]
            num_q2 = int(row[0])
        else:
            num_q0 = 0
            num_q2 = 0

        q = u"select /* SLOW_OK */ count(distinct tl_from) as num from templatelinks left join page on page_id=tl_from left join linktarget on lt_id=tl_target_id where lt_namespace=%d and page_namespace=0;"%ns
        cursor.execute(q)
        row = cursor.fetchone ()
        num_trans = int(row[0])

        cursor.execute (u"select /* SLOW_OK */ count(distinct page_id) from page where page_namespace=0 and page_is_redirect=0;")
        row = cursor.fetchone ()
        num_texts = int(row[0])

        #disambiguation pages
        # first try the __DISAMBIG__ keyword
        q_disamb = u"select count(page_title) from page where page_namespace = 0 and page_is_redirect = 0 and page_id in (select pp_page from page_props where pp_propname = 'disambiguation')"
        cursor.execute(q_disamb)
        row = cursor.fetchone ()
        num_disambig = int(row[0])

        res[dom] = (num_pages, num_q0, num_q2, num_q3, num_q4, num_trans, num_texts, num_disambig)
        
        cursor.close ()
        conn.close ()
    return res

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
        d.insert(0, tm.strftime('%Y-%m-%d %H:%M:%S'))
        d.append(0)
        return tuple(d)
    else:
        d = list(data)
        d = convert_everything_to_int(d)
        d.insert(0, tm.strftime('%Y-%m-%d %H:%M:%S'))
        return tuple(d)

if __name__ == '__main__':
    with get_user_conn() as conn:
        with conn.cursor() as cursor:
            all_stats = get_stats(domains)
            for domain in domains:
                print(f'Inserting for {domain}')
                if domain in all_stats:
                    print(f'Found data for {domain}')
                    all_stat = normalize_data(datetime.now() ,all_stats[domain])
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
                                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', all_stat)
            print('Commiting all this to a database')
            conn.commit()