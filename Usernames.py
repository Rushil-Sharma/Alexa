import sqlite3
conn = sqlite3.connect('names.db')
c = conn.cursor()
c.execute("""CREATE TABLE names(
        Itzrushil ,
        Barchepurva ,
        Test ,
        Jarvis ,
        Admin ,
        Main 
        )""")
conn.commit()
conn.close()
username = [
    'Itzrushil' ,
    'Barchepurva' ,
    'Test' ,
    'Jarvis' ,
    'Admin' ,
    'Main'
    ]
