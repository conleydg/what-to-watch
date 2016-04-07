import csv
from movie_lib import *

def create_rating_list():
    with open('u_data.csv') as f:
        reader = csv.DictReader(f, fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'], delimiter='\t')
        rating_list = []
        for row in reader:
            rating_list.append(Rating(row))
    return rating_list



def create_movie_list(movie_ratings):
    with open('u_item.csv', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames = ['movie_id', 'movie_title', 'release date', 'video release date'
                   'unknown', 'Action', 'Adventure', 'Animation',
                 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy'
                 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                 'Thriller', 'War', 'Western'], delimiter='|')
        movie_list = []
        for row in reader:
            movie_list.append(Movie(row, movie_ratings))
    return movie_list




with open('u_user.csv') as f:
    reader = csv.DictReader(f, fieldnames = ['user_id', 'age', 'gender', 'occupation', 'zip_code'], delimiter='|')
    user_list = []
    for row in reader:
        user_list.append(User(row))


def find_all_ratings_for_movie_by_id(rating_list, movie_id):
    for movie in rating_list:
        if movie.movie_id == movie_id:
            print(movie.rating)



def main():

    rating_list = create_rating_list()

    movie_ratings = {}

    for movie in rating_list:
        if movie.item_id in movie_ratings:
            (movie_ratings[movie.item_id]).append(int(movie.rating))
        else:
            movie_ratings[movie.item_id] = [int(movie.rating)]


    movie_list = create_movie_list(movie_ratings)

    for movie in movie_list:
        print(str(movie))

    print(movie_list[17].all_ratings)

    print(sum(movie_list[17].all_ratings))

    print(movie_list[17].average_rating)





























if __name__ == "__main__":
    main()
