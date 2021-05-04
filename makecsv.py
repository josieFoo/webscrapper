import csv

def save_to_file(tuples):
  file   = open("courses.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "link"])
  for t in tuples:
    writer.writerow(list(t.values()))
  return