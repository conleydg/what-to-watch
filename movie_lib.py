class Rating:
    def __init__(self, dictionary):
        self.user_id = dictionary['user_id']
        self.item_id = int(dictionary['item_id'])
        self.rating = dictionary['rating']
        self.timestamp = dictionary['timestamp']


    def __str__(self):
        return 'user_ID: ' + str(self.user_id) + ' movie_id: ' + str(self.movie_id) + ' rating: ' + str(self.rating) + ' timestamp: ' + str(self.timestamp)



class Movie():
    def __init__(self, dictionary, movie_ratings):
        self.movie_id = int(dictionary['movie_id'])
        self.movie_title = dictionary['movie_title']
        self.all_ratings = movie_ratings[self.movie_id]
        self.average_rating = sum(self.all_ratings)/len(self.all_ratings)


    def __str__(self):
        return 'movie_id: ' + str(self.movie_id) + ' movie_title ' + str(self.movie_title) + 'all_ratings ' + str(self.all_ratings)




class User:
    def __init__(self, dictionary):
        self.user_id = dictionary['user_id']
        self.age = dictionary['age']
        self.gender = dictionary['gender']
        self.occupation = dictionary['occupation']
        self.zip_code = dictionary['zip_code']
