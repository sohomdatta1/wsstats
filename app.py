from flask import Flask, send_file, send_from_directory
from userdb import get_conn
from datetime import datetime
from domains import domains

app = Flask(__name__)


@app.route('/api/stats/<lang>/<int:start_time>/<int:end_time>')
def stats(lang: str, start_time: int, end_time: int):

    if not ( lang in domains):
        return { 
            'success': False
        }

    with get_conn().cursor() as cursor:
        cursor.execute(f'SELECT * FROM `stats_{lang}` WHERE time BETWEEN %s AND %s', (
            datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"),
            datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
        ))
        res = cursor.fetchall()
        return {
            'data': res,
            'success': True
        }

@app.route('/api/alllangalltime')
def alllangalltime():
    alldata= {}
    with get_conn().cursor() as cursor:
        for dom in domains:
            cursor.execute(f'SELECT * FROM `stats_{dom}`')
            res = cursor.fetchall()
            alldata[dom] = {}
            alldata[dom]['data'] = res
    return alldata 

@app.route('/api/all_langs')
def all_langs():
    doms = list(domains)
    doms.sort()
    return doms

@app.route("/")
def index():
    r = send_file('./client/dist/index.html')
    r.headers['Cache-Control'] = 'max-age=604800'
    return r


@app.route("/<path:filename>")
def serve_other_files(filename: str):
    r = send_from_directory('./client/dist', filename)
    r.headers['Cache-Control'] = 'max-age=604800'
    return r

@app.errorhandler(404)
def page_not_found(e):
    r = send_file('./client/dist/index.html')
    r.headers['Cache-Control'] = 'max-age=604800'
    return r


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)