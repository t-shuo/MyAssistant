import sqlite3
import local_settings

def sql_execute(sql_statement):
    con = sqlite3.connect(local_settings.database)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS top_websites ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        site, \
        domain_name, \
        similarweb_ranking, \
        semrush_visits, \
        category, \
        principal_country_territory, \
        image, \
        created_on TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP \
    )")

    res = cur.execute(sql_statement)
    con.commit()
    sql_res = res.fetchall()
    con.close()
    return sql_res

if __name__ == "__main__":
    sql_execute(sql_statement)