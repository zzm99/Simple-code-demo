from requests_html import HTMLSession

session = HTMLSession()

links = ['https://movie.douban.com/subject/1292052/', 'https://movie.douban.com/subject/1962665/', 'https://movie.douban.com/subject/26752088/']

for link in links:
    r = session.get(link)
    title = r.html.find('#content > h1 > span:nth-child(1)', first=True)
    year = r.html.find('#content > h1 > span.year', first=True)
    print(title.text, year.text)



###############################################
    
    

import csv

file = open('movies.csv', 'w', newline='')
csvwriter = csv.writer(file)

# 写入标题行
csvwriter.writerow(['名称', '年份'])
# 写入数据
csvwriter.writerow(['A', '1992'])
csvwriter.writerow(['B', '1998'])
csvwriter.writerow(['C', '2010'])
file.close()



###############################################



from requests_html import HTMLSession
import csv

session = HTMLSession()

file = open('movies.csv', 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(['名称', '年份'])

links = ['https://movie.douban.com/subject/1292052/', 'https://movie.douban.com/subject/26752088/', 'https://movie.douban.com/subject/1962665/']

for link in links:
    r = session.get(link)
    title = r.html.find('#content > h1 > span:nth-child(1)', first=True)
    year = r.html.find('#content > h1 > span.year', first=True)
    csvwriter.writerow([title.text, year.text])

file.close()