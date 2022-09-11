"""
webscraper v0.1
"""
import os
import time
import traceback
import urllib.request

import bs4

import modules.database_loader

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
            data.append(int(cols[0].split('/')[0]))
    return data
    #print(data)

def load_matchday(year:int, mday:int):
    """
    loads the requested matchday on worldfootball.net
    """
    # get the data
    if not os.path.exists(f"database/wfb/bundesliga_{year}_{mday}.csv"):
        print("Scraping", year, mday)
        time.sleep(0.2)
        soup = None
        wfb_url = ("https://www.worldfootball.net/schedule/"
                  f"bundesliga-{year}-{year+1}-spieltag/{mday}/")
        req = urllib.request.Request(
            url = wfb_url,
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
        modules.database_loader.write_database(data, f"wfb/bundesliga_{year}_{mday}.csv", False)
    else:
        data = modules.database_loader.load_database(f"wfb/bundesliga_{year}_{mday}.csv", False)
    # load the data
    th_ta_gh_ga_y_md = []
    for game in data:
        team_h = game[2]
        team_a = game[4]
        result_tmp = game[5].split(' ')[0]
        result_h = result_tmp.split(':')[0]
        result_a = result_tmp.split(':')[1]
        th_ta_gh_ga_y_md.append([team_h, team_a, result_h, result_a, year, mday])
    return th_ta_gh_ga_y_md
