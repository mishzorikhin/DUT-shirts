import sqlite3


def order(UserID, selectionTshirt, selectionSize, selectionAdress, selectionPhone, selectionName,selectionDelivery, feedback):
    conn = sqlite3.connect('DUTShirts.db')
    cur = conn.cursor()

    setUserData = "INSERT INTO orders VALUES ('" + str(UserID) + "', '" + str(selectionTshirt) + "', '" + str(selectionSize) + "', '" + str(selectionPhone) + "', '" + str(selectionAdress) + "', '" + str(selectionAdress) + "', '" + str(selectionName) + "','" + str(selectionDelivery) + "','" + str(feedback) + "','" + '0' "'); "
    cur.execute(setUserData)
    conn.commit()
