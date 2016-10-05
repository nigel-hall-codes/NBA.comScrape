from selenium import webdriver
import touchtimedb


url = 'http://stats.nba.com/defensivehub/#!/oppshooting/team/?sort=Above%20the%20Break%203%20FGA&dir=1&Season=2015-16&SeasonType=Regular%20Season&DistanceRange=By%20Zone'
driver = webdriver.Chrome("/Users/Hallshit/Downloads/chromedriver")
driver.get(url)

currentrow = 61
numberofteams = 30
stats = []
categories = ['team', 'restM', 'restA', 'restP', 'painM', 'painA','painP', 'midrM', 'midrA', 'midrP', 'leftM','leftA', 'leftP',
              'righM', 'righA', 'righP', 'abovM', 'abovA', 'abovP']
teamdict = {}
teams = []


for x in range(0,numberofteams):
    row = driver.find_element_by_xpath(
        '//*[@id="main-container"]/div/div/div[3]/div/div/div/div[2]/div[5]/div/table/tbody/tr[{}]'.format(x + 61))
    statsd = row.find_elements_by_class_name('ng-binding')
    for stat in statsd:
        stats.append(stat.text)
currteam = 0
for x in range(0, numberofteams):
    for y, c in enumerate(categories):
        teamdict[c] = stats[y + currteam]

    currteam += 19
    teams.append(teamdict)
    teamdict = {}

for team in teams:
    touchtimedb.DefensiveZoneChart.create(**team)



driver.close()




