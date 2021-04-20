import sqlite3

def start(message):
    conn = sqlite3.connect('DUTShirts.db')
    cur = conn.cursor()

    global newUser

    setUserID = str(message.from_user.id)
    setUserName = str(message.from_user.username)

    searchID = "SELECT COUNT(DISTINCT id_user) FROM users WHERE id_user = '" + setUserID + "'; "

    cur.execute(searchID)
    results = cur.fetchone()

    for i in results:
        if i == 0:
            setUserData = "INSERT INTO users VALUES ('" + setUserID + "', '" + setUserName + "', NULL, NULL, NULL, " \
                                                                                             "NULL); "
            cur.execute(setUserData)
            conn.commit()
        else:
            newUser = False