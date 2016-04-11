class Rating:
    def __init__(self, dictionary):
        self.user_id = int(dictionary['user_id'])
        self.item_id = int(dictionary['item_id'])
        self.rating = dictionary['rating']
        # self.timestamp = dictionary['timestamp']


    def __str__(self):
        return 'user_ID: ' + str(self.user_id) + ' item_id: ' + str(self.item_id) + ' rating: ' + str(self.rating)  #' timestamp: ' + str(self.timestamp)



class Movie():
    def __init__(self, dictionary, movie_ratings):
        self.movie_id = int(dictionary['movie_id'])
        self.movie_title = dictionary['movie_title']
        self.all_ratings = movie_ratings[self.movie_id]
        self.average_rating = '%.2f' %(sum(self.all_ratings)/len(self.all_ratings))


    def __str__(self):
        return 'movie_id: ' + str(self.movie_id) + ' movie_title: ' + str(self.movie_title) + ' all_ratings: ' + str(self.all_ratings) + ' average_rating: ' + str(self.average_rating)

    @staticmethod
    def print_top_twenty_movies(movie_list):
        new_list = []
        for movie in movie_list:
            if len(movie.all_ratings) > 5:
                new_list.append({'average rating':movie.average_rating, 'movie_id': movie.movie_id})
        new_list = sorted(new_list, key=lambda k: k['average rating'])
        return new_list[-20:]


    @staticmethod
    def remove_movie_if_user_has_rated(movie_list, user_list, user_id):
        un_reviewed_movies = []
        for movie in movie_list:
            if movie.movie_id not in (user_list[(user_id)].all_ratings_by_user):
                un_reviewed_movies.append(movie)
        return un_reviewed_movies


class User:
    def __init__(self, dictionary, all_ratings_by_user):
        self.user_id = int(dictionary['user_id'])
        self.age = dictionary['age']
        self.gender = dictionary['gender']
        self.occupation = dictionary['occupation']
        self.zip_code = dictionary['zip_code']
        self.all_ratings_by_user = all_ratings_by_user[int(dictionary['user_id'])]


    # def all_ratings_by_user(self, dictinary, rating_list):
    #     all_ratings_by_user = []
    #     for rating in rating_list:
    #         if self.user_id == raiting_list.user_id:
    #             all_ratings_by_user.append({rating_list.movie_id: rating_list.user_id})
    #     return self.all_ratings_by_user



    def __str__(self):
        return ' user_id ' + str(self.user_id) + ' age ' + str(self.age) + ' gender ' + str(self.gender) + ' occupation ' + str(self.occupation) + ' zip_code ' + str(self.zip_code) + ' user ratings: ' + str(self.all_ratings_by_user)
