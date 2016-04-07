import unittest

from movie_lib import *
from movie_lib_main import *


rating_instance = Rating({'user_id' : '123', 'movie_id' : '456', 'rating' : 'awesomeness', 'timestamp' : '3:30'})
movie_instance = Movie({'movie_id' : '123', 'movie_title' : 'Gone With The Wind'})
user_instance = User({'user_id' : '1', 'age': '27', 'gender' : 'Male', 'occupation' : 'TIY Student', 'zip_code' : '27707'})


class MovieClass(unittest.TestCase):

    def test_rating_class(self):
        self.assertEqual(rating_instance.user_id, '123')
        self.assertEqual(rating_instance.movie_id, '456')
        self.assertEqual(rating_instance.rating, 'awesomeness')
        self.assertEqual(rating_instance.timestamp, '3:30')
        self.assertNotEqual(rating_instance.user_id, '37')


    def test_movie_class(self):
        self.assertEqual(movie_instance.movie_id, '123')
        self.assertEqual(movie_instance.movie_title, 'Gone With The Wind')
        self.assertNotEqual(movie_instance.movie_id, '456')

    def test_user_class(self):
        self.assertEqual(user_instance.user_id, '1')
        self.assertEqual(user_instance.age, '27')
        self.assertEqual(user_instance.gender, 'Male')
        self.assertEqual(user_instance.occupation, 'TIY Student')
        self.assertEqual(user_instance.zip_code, '27707')
        self.assertNotEqual(user_instance.zip_code, '2777')


    # 
    # def test_find_all_ratings_for_movie_by_id(self):
    #     self.assertEqual(find_all_ratings_for_movie_by_id












if __name__ == '__main__':
    unittest.main()
