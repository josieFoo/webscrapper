from scrapper import make_tuples_of_courses
from makecsv import save_to_file

list_of_all_tuples = make_tuples_of_courses()

save_to_file(list_of_all_tuples)