## 1. Overview ##

file = open("movie_metadata.csv")
metadata = file.read()
metadata = metadata.split("\n")
movie_data = []
#print(metadata)
for movie in metadata:
    movie_data.append(movie.split(','))
    
    
movie_data[:5]

## 3. Writing Our Own Functions ##

movie_names = []
def filter_movies(movie_data):
    for row in movie_data:
        movie_names.append(row[0])
    return movie_names[:5]
    
print(filter_movies(movie_data))

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

wonder_woman_usa = 'USA' in wonder_woman

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]


def index_equals_str(lst, ind, val):
    wonder_woman_in_color = val in lst[ind]
    print(wonder_woman_in_color)
    
index_equals_str(ind=2, lst=wonder_woman, val='Color')

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt


def feature_counter(input_lst, loc, input_str, header_row=False):
    num_of_us_movies = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for row in input_lst:
        if row[loc] == input_str:
            num_of_us_movies = num_of_us_movies + 1
    return num_of_us_movies
    
num_of_us_movies = feature_counter(movie_data, 6, "USA", True)

## 7. Calling a Function inside another Function ##

summary = {}

def feature_counter(input_lst, header_row = False):
    final_data = {}
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    num_color_films = 0
    num_films_in_english = 0
    num_japan_films = 0
    for row in input_lst:
        if row[2] == "Color":
            num_color_films += 1
        if row[5] == "English":
            num_films_in_english += 1
        if row[6] == "Japan":
            num_japan_films += 1
    final_data = {"color_films":num_color_films,
                  "films_in_english":num_films_in_english,
                  "japan_films": num_japan_films
                 }
    return final_data

def summary_statistics(input_lst):
    return feature_counter(movie_data, True)
    
summary = summary_statistics(movie_data)