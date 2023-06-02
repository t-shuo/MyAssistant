
def main(n):
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
        print(i)

if __name__ == "__main__":
    # import local_settings from parent directory
    import sys, os
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)
    import local_settings

    import requests
    from bs4 import BeautifulSoup
    url = 'https://en.wikipedia.org/wiki/List_of_most_visited_websites'

    main(10)