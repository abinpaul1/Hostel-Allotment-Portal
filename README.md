# Hostel-Management

## Setup instructions

- apt install python3
- apt install python3-pip
- apt install mysql-server
- apt install libmysqlclient-dev
- pip3 install -r req.txt
- Setup mysql and configure a new user before continuing
- Nano ~/.my.cnf then add
  - [client]
  - user = username
  - password = your_password
- Run mysql: mysql
  - create database hostels
- To populate with default data: python3 setup_script.py
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py createsuperuser
  - fill in admin login details
- python3 manage.py runserver
