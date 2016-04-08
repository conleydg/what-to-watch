import unittest

from movie_lib import *
from movie_lib_main import *


rating_instance = Rating({'user_id' : '123', 'item_id' : '456', 'rating' : 'awesomeness'})
movie_instance = Movie({'movie_id' : '123', 'movie_title' : 'Gone With The Wind'}, {123: [5, 1]})
user_instance = User({'user_id' : '1', 'age': '27', 'gender' : 'Male', 'occupation' : 'TIY Student', 'zip_code' : '27707'}, {1 : {57 : 5, 102: 3}})
# user_list =
# movie_list =

class MovieClass(unittest.TestCase):

    def test_rating_class(self):
        self.assertEqual(rating_instance.user_id, 123)
        self.assertEqual(rating_instance.item_id, 456)
        self.assertEqual(rating_instance.rating, 'awesomeness')
        self.assertNotEqual(rating_instance.user_id, '37')


    def test_movie_class(self):
        self.assertEqual(movie_instance.movie_id, 123)
        self.assertEqual(movie_instance.movie_title, 'Gone With The Wind')
        self.assertNotEqual(movie_instance.movie_id, 456)
        self.assertEqual(movie_instance.all_ratings, [5, 1])
        self.assertEqual(movie_instance.average_rating, '3.00')

    def test_user_class(self):
        self.assertEqual(user_instance.user_id, 1)
        self.assertEqual(user_instance.age, '27')
        self.assertEqual(user_instance.gender, 'Male')
        self.assertEqual(user_instance.occupation, 'TIY Student')
        self.assertEqual(user_instance.zip_code, '27707')
        self.assertNotEqual(user_instance.zip_code, '2777')
        self.assertEqual(user_instance.all_ratings_by_user, ({57 : 5, 102: 3}))


    # def test_remove_movies_already_rated_by_user(self):
    #     self.assertEqual(remove_movie_if_user_has_rated(user_list, movie_list, 15))











if __name__ == '__main__':
    unittest.main()
