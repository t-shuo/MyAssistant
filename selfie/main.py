def main():
    get_websites = False
    sql_statement = "SELECT MAX(created_on) FROM top_websites"
    latest_date = database.sql_execute(sql_statement)[0][0]
    if latest_date == None:
        get_websites = True
    else:
        latest_date = datetime.datetime.strptime(latest_date, '%Y-%m-%d %H:%M:%S')
        if (datetime.datetime.now()-latest_date).days > 10:
            get_websites = True
    
    if get_websites:
        get_top_websites()


def get_top_websites():
    proxies = {}
    try:
        proxies['http'] = 'socks5://' + local_settings.proxy_socks5
        proxies['https'] = 'socks5://' + local_settings.proxy_socks5
        r = requests.get(url, proxies=proxies)
    except Exception as e:
        print(e)
        proxies['http'] = 'socks5h://' + local_settings.proxy_socks5
        proxies['https'] = 'socks5h://' + local_settings.proxy_socks5
        r = requests.get(url, proxies=proxies)

    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.table

    top_websites = []
    for tr in table.tbody.find_all('tr'):
        website = []
        for td in tr.find_all('td'):
            website.append(td.text.strip())
        if website:
            top_websites.append(website)
    for i in top_websites:
        site = i[0]
        domain_name = i[1]
        similarweb_ranking = i[2].split()[0]
        # semrush_visits = i[3] the column is removed in wikipedia page
        category = i[3]
        principal_country_territory = i[4]
        sql_statement = f"INSERT INTO top_websites (site, domain_name, similarweb_ranking, category, principal_country_territory) \
                                            VALUES ('{site}','{domain_name}','{similarweb_ranking}','{category}','{principal_country_territory}')"
        database.sql_execute(sql_statement)

if __name__ == "__main__":
    # import local_settings from parent directory
    import sys, os
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)
    import local_settings
    import database
    import datetime
    import requests
    from bs4 import BeautifulSoup
    url = 'https://en.wikipedia.org/wiki/List_of_most_visited_websites'

    main()