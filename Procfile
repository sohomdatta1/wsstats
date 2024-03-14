web: gunicorn -w 4 -b 0.0.0.0 app:app --timeout 90000  --access-logfile -
upload_old_data: python3 upload_previous_data.py
generate_new_data: python3 statistics_gen.py