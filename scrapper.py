import requests
from bs4 import BeautifulSoup

# Homepage, where our course list is
URL_REQUEST = requests.get(
  'https://www.buchsys.de/fu-berlin/angebote/aktueller_zeitraum/index.html'
  )

# Making Relation: SPORT(title, link)
def make_tuples_of_courses():
  buchsys_soup = BeautifulSoup(URL_REQUEST.text, "html.parser")
  courses      = buchsys_soup.find_all("dd")
  tuples       = []
  for course in courses[:-1]:
    table          = {}
    course_title   = course.find("a").string
    course_html    = course.find("a")["href"]
    course_url     = f"https://www.buchsys.de/fu-berlin/angebote/aktueller_zeitraum/{course_html}"
    table['title'] = course_title
    table['link']  = course_url
    tuples.append(table)
  return tuples


# delete test function after tests!


