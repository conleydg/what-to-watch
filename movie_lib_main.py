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



def create_user_list(rating_list):
    with open('u_user.csv') as f:
        reader = csv.DictReader(f, fieldnames = ['user_id', 'age', 'gender', 'occupation', 'zip_code'], delimiter='|')
        user_list = []
        for row in reader:
            user_list.append(User(row, rating_list))
    return user_list


def top_twenty_movies(movie_list):
    newlist = sorted(movie_list, key=lambda k: k('average_rating'))
    return newlist




def main():

    rating_list = create_rating_list()



    movie_ratings = {}

    for movie in rating_list:
        if movie.item_id in movie_ratings:
            (movie_ratings[movie.item_id]).append(int(movie.rating))
        else:
            movie_ratings[movie.item_id] = [int(movie.rating)]


    movie_list = create_movie_list(movie_ratings)

    all_ratings_for_user = {}



    all_ratings_by_user = {}
    for rating in rating_list:
        if rating.user_id in all_ratings_by_user:
            all_ratings_by_user[rating.user_id][rating.item_id] = rating.rating
        else:
            all_ratings_by_user[rating.user_id]= {rating.item_id: rating.rating}



    user_list = create_user_list(all_ratings_by_user)

    # top_twenty = (top_twenty_movies(movie_list))
    #
    #
    # print(top_twenty)

    # print(movie_list)
    #
    # for movie in movie_list:
    #     print(str(movie))


    top_twenty = Movie.print_top_twenty_movies(movie_list)
    print(len(top_twenty))
    print(top_twenty[-20:-1])

    #
    # for movie in movie_list:
    #     print(movie.average_rating)



























if __name__ == "__main__":
    main()
