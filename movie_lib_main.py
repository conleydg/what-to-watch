import csv
import math
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


# def remove_movie_if_user_has_rated(user_list, movie_list, user_id):
#     un_reviewed_movies = movie_list
#     for movie_number in (user_list[user_id].all_ratings_by_user):
#         un_reviewed_movies.remove[movie_numer - 1]
#     return un_reviewed_movies

def user_rating_normalized_list(user_id, movie_list, user_list):
    normalized_list = [0] * len(movie_list)
    index =0
    while index < len(movie_list):
        if index in user_list[user_id].all_ratings_by_user:
            (normalized_list[index]) = int(user_list[user_id].all_ratings_by_user[index])
        index += 1
    return normalized_list




def euclidean_distance(v, w):
    if len(v) is 0:
        return 0
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))

def normalized_dict_of_users(user_list, user_id, movie_list, user_list):






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


    # for user in user_list:
    #     print(user.user_id)

    # print(user_list[42].all_ratings_by_user[272])


    # print(movie_list[1])

    # top_twenty = (top_twenty_movies(movie_list))
    #
    #
    # print(top_twenty)

    # print(movie_list)
    #
    # for movie in movie_list:
    #     print(str(movie))

    #
    # top_twenty = Movie.print_top_twenty_movies(movie_list)
    # # print(len(top_twenty))
    # print(top_twenty[-20:-1])
    #
    #
    # print(len(movie_list))
    #
    # un_reviewed_movies = Movie.remove_movie_if_user_has_rated(user_list, movie_list, 17)
    #
    #
    # print(len(un_reviewed_movies))
    #
    # print(len(movie_list))
    #
    #
    # print(len(user_list[17].all_ratings_by_user))
    #
    # print(len(movie_list))
    #
    # top_twenty_not_reviewed = Movie.print_top_twenty_movies(un_reviewed_movies)
    #
    # print(top_twenty_not_reviewed[-20:-1])


    # print(user_list[0])
    # print(movie_list[0])

    #
    # print((user_list[17].all_ratings_by_user))

    #
    # print(user_list[180])
    # print(user_list[180].all_ratings_by_user[1295])
    #
    # user_one_normalized_ratings =user_rating_normalized_list(180, movie_list, user_list)

    v = user_rating_normalized_list(180, movie_list, user_list)
    w = user_rating_normalized_list(180, movie_list, user_list)

    distance = euclidean_distance(v, w)
    print(distance)


    #
    # two_user_normalized_list(1, 2, movie_list, user_list)












if __name__ == "__main__":
    main()
