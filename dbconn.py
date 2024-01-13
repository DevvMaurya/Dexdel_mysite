import mysql.connector as sql
class connection:
    def __init__(self):
        self.connection_details = {
            'user': 'root',
            'pswd': 'MySql@123',
            'host': '127.0.0.1',
            'db': 'dexdel_data'
        }

    def initial_connection(self):
        try:
            conn = sql.connect(user = self.connection_details['user'],host = self.connection_details['host'],passwd = self.connection_details['pswd'],database = self.connection_details['db'])
            return conn
        except Exception as e:
            print('Connection Problem..🔴 \n',e)

    def get_cursor(self):
        # c = 
        return self.initial_connection().cursor()
    
    def commit(self):
        self.initial_connection().commit()
'''
🔴🔴Connot import this file in views.py file.
why...?
'''

if __name__ == '__main__':
    pass
    # obj = connection()
    # cur = obj.get_cursor()
    # print(cur)