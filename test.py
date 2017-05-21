# coding:utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    db = MySQLdb.connect("localhost", "root", "", "iot",charset='utf8')

    sql = "SELECT * FROM iot_test"

    cursor = db.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    # for record in results:
        # print record[1].decode('utf-8'), record[2].decode('utf-8')

    db.close()

except MySQLdb.Error as e:
    print "Error %d: %s" % (e.args[0], e.args[1])
