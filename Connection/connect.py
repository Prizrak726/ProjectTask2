from peewee import *

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('SereD62_Task2',
                         user='SereD62_Task2',
                         password='111111',
                         host='10.11.13.118',
                         port=3306)
if __name__ == '__main__':

    print(mysql_db.connect())

