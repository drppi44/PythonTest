Test project for python\django

Deployment:
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py loaddata initial_data



Deploy postgres database and user:
1. CREATE DATABASE drppi44;
2. CREATE USER drppi44 WITH PASSWORD 'drppi44';
3. GRANT ALL PRIVILEGES ON DATABASE drppi44 TO drppi44;

Tips:
1. settings_local.py for postgres database
2. link for products added for the last day is only avaliable for logged in user ( login_url  '/admin' )
