"""
webscraper v0.1
"""
import traceback
import urllib.request

import bs4

def load_range():
    """
    loads the available range of years on worldfootball.net
    """
    soup = None
    req = urllib.request.Request(
        url="https://www.worldfootball.net/history/bundesliga/",
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        soup = bs4.BeautifulSoup(urllib.request.urlopen(req).read(), "html.parser")
    except Exception as exc:
        print(traceback.format_exc())
        raise exc
    if soup is None:
        raise RuntimeError("could not load X")
    data = []
    table = soup.find('table', attrs={'class':'standard_tabelle'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if len(cols) > 0:
            data.append(cols[0].split('/')[0])
    return data
    #print(data)

def load_matchday(year:int, matchday:int):
    """
    loads the requested matchday
    """
    soup = None
    req = urllib.request.Request(
        url = "https://www.worldfootball.net/schedule/bundesliga-" \
            + str(year) + "-" + str(year+1) + "-spieltag/" + str(matchday) + "/",
        headers = {'User-Agent': 'Mozilla/5.0'})
    try:
        soup = bs4.BeautifulSoup(urllib.request.urlopen(req).read(), "html.parser")
    except Exception as exc:
        print(traceback.format_exc())
        raise exc
    if soup is None:
        raise RuntimeError("could not load X")
    data = []
    table = soup.find('table', attrs={'class':'standard_tabelle'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
    # date = data[0][0]
    th_ta_gh_ga_y_md = []
    for game in data:
        team_h = game[2]
        team_a = game[4]
        result_tmp = game[5].split(' ')[0]
        result_h = result_tmp.split(':')[0]
        result_a = result_tmp.split(':')[0]
        th_ta_gh_ga_y_md.append([team_h, team_a, result_h, result_a, year, matchday])
    #for x in th_ta_gh_ga_y_md:
    #    print(x[0], x[1], x[2], x[3], year, matchday, sep='\t')
    return th_ta_gh_ga_y_md
