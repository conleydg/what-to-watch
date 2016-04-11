import tkinter as tk

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

def normalized_dict_of_users(user_list, movie_list):
    normalized_dict_ratings = {}
    user_id = 0
    for user in user_list:
        user_normalized = user_rating_normalized_list(user_id, movie_list, user_list)
        normalized_dict_ratings[user_id] = user_normalized
        user_id += 1
    return normalized_dict_ratings



def find_similar_user(normalized_dict_ratings, user_id):
    user_index = 0
    highest_similar_user = {}
    v = normalized_dict_ratings[(user_id)]
    for user in normalized_dict_ratings:
        w = normalized_dict_ratings[user]
        euc_relationship = euclidean_distance(v, w)
        highest_similar_user[user_index] = euc_relationship
        user_index += 1
        print(user_index, euc_relationship)
    highest_similar_user[user_id] -= 1
    return highest_similar_user


def return_movie_suggestion(user_id, most_related_user, user_list):
    unique_movies = []
    for movie in user_list[most_related_user - 1].all_ratings_by_user:
        if movie not in user_list[int(user_id) - 1].all_ratings_by_user and int(user_list[most_related_user - 1].all_ratings_by_user[movie]) > 3:
            unique_movies.append(movie)
    return unique_movies

def create_movie_ratings_dict(rating_list):
    movie_ratings = {}
    for movie in rating_list:
        if movie.item_id in movie_ratings:
            (movie_ratings[movie.item_id]).append(int(movie.rating))
        else:
            movie_ratings[movie.item_id] = [int(movie.rating)]
    return movie_ratings

def create_all_ratings_by_user_dict(rating_list):
    all_ratings_by_user = {}
    for rating in rating_list:
        if rating.user_id in all_ratings_by_user:
            all_ratings_by_user[rating.user_id][rating.item_id] = rating.rating
        else:
            all_ratings_by_user[rating.user_id]= {rating.item_id: rating.rating}
    return all_ratings_by_user

def print_top_twenty_titles(movie_list,):
    movies_sorted_by_avg_rating = Movie.print_top_twenty_movies(movie_list)
    for movie in movies_sorted_by_avg_rating:
        print(movie_list[movie['movie_id']].movie_title)

def print_top_twenty_titles_not_rated(movie_list, user_list, user_id):
    unreviewed_movies = Movie.remove_movie_if_user_has_rated(movie_list, user_list, user_id)
    movies_sorted_by_avg_rating = Movie.print_top_twenty_movies(unreviewed_movies)
    for movie in movies_sorted_by_avg_rating:
        print(movie_list[movie['movie_id']].movie_title)




def main():

    rating_list = create_rating_list()

    movie_ratings = create_movie_ratings_dict(rating_list)

    movie_list = create_movie_list(movie_ratings)

    all_ratings_by_user = create_all_ratings_by_user_dict(rating_list)

    user_list = create_user_list(all_ratings_by_user)

    # unrated_pop = print_top_twenty_titles_not_rated(movie_list, user_list, 17)



    # print(print_top_twenty_titles(movie_list))




    # normalized_dict_ratings = normalized_dict_of_users(user_list, movie_list)
    #
    # related_user_dict = find_similar_user(normalized_dict_ratings, 97)
    #
    # most_related_user = (max(related_user_dict, key=lambda k: related_user_dict[k]))
    #
    # print(most_related_user)
    #
    # print(user_list[most_related_user - 1])
    #
    # print(user_list[0])
    #
    # movie_suggestion_list = (return_movie_suggestion(97, most_related_user, user_list))
    #
    # for movie in movie_list:
    #     if movie.movie_id in movie_suggestion_list:
    #         print(movie.movie_title)










if __name__ == "__main__":
    main()
