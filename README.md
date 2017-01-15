On an Ubuntu system you can install the PostgreSQL database system with this command:

* sudo apt-get install postgresql postgresql-contrib

Test if the PostgreSQL database system is up and running with this command:

* sudo /etc/init.d/postgresql status
* python-database-postgresql
PostreSQL database status

If you do not see the above screen, try one of these commands:

* sudo service postgresql start
* sudo service postgresql restart

Install psycopg2
Psycopg is a PostgreSQL database adapter for Python.
This command installs the module:

* sudo apt-get install python-psycopg2

We create a database and database user (also called a role)

* sudo -u postgres createuser -D -A -P pythonspot

* sudo -u postgres createdb -O pythonspot testdb

Reload the database:

* sudo /etc/init.d/postgresql reload