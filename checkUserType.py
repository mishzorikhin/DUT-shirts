import sqlite3

def checkUserType (userID):
    conn = sqlite3.connect('DUTShirts.db')
    cur = conn.cursor()
    print(userID)



    inquiry = "SELECT * FROM users WHERE id_user = "+ str(userID) +""
    cur.execute(inquiry)

    result = cur.fetchone()

    if result[5]==1:
        return True


