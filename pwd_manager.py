import sqlite3
from pwd_generator import Generator

conn = sqlite3.connect('data.db')
c = conn.cursor()
go = Generator()

# c.execute("""CREATE TABLE password_list (
#     website_name text,
#     password text
# )""")

class Commands:
    def new_query(self, wbname, pwd):
        """this function enables the user to insert a new password query

        Args:
            wbname (str): it is the website name which is linked to the password
            pwd (str): it is the password linked to the wbname
        """
        with conn:
            c.execute("INSERT INTO password_list VALUES (?,?)", (wbname, pwd))
        pass

    def update_query(self, wbname):
        """this function enables the user to update a query

        Args:
            wbname (str): the website name to change the pass
        """
        with conn:
            newpwd = go.generate_pwd()
            c.execute(f"UPDATE password_list SET password=? WHERE website_name=?", (newpwd, wbname))        

    def remove_query(self, wbname):
        """this function enables the user to remove a query

        Args:
            wbname (str): website name to delete its query
        """
        with conn:
            c.execute(f"DELETE FROM password_list WHERE website_name=?", (wbname))
        pass

    def view_all(self):
        """this function enables the user to view all his queries
        """
        c.execute("SELECT * FROM password_list")
        print(c.fetchall())
        pass


conn.commit()
