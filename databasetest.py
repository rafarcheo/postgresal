import psycopg2

#user - pythontest
#pass - test

# Connect to an existing database
conn = psycopg2.connect("dbname=test user=pythontest")