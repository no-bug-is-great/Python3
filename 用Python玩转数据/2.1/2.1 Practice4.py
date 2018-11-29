# 2.1 Practice

#4
# 请爬取网页（http://www.volleyball.world/en/vnl/women/results-and-ranking/round1）上的数据
#（包括TEAMS and TOTAL, WON, LOST of MATCHES）

import re
import requests

def crawler(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestsException as err:
        return err
    r.encoding = r.apparent_encoding
    pattern = re.compile('<figure class="team">\s+<a id=.*?Link1_.*?" href="/en/vnl/women/teams/.*?"><img id=.*?/></a>\s+<figcaption><a id=.*? href="/en/vnl/women/teams/.*?">(.*?)<\/a><\/figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>',
                           flags = re.M)
    p = re.findall(pattern, r.text)
    return p

if __name__ == "__main__":
    url = 'http://www.volleyball.world/en/vnl/women/results-and-ranking/round1'
    result = crawler(url)
    print(result)
