from tkinter import *
from tkinter import ttk
from movie_lib_main import *

def calculate(*args):

    rating_list = create_rating_list()

    movie_ratings = create_movie_ratings_dict(rating_list)

    movie_list = create_movie_list(movie_ratings)

    all_ratings_by_user = create_all_ratings_by_user_dict(rating_list)

    user_list = create_user_list(all_ratings_by_user)

    user_input = int(user_id_input.get())


    normalized_dict_ratings = normalized_dict_of_users(user_list, movie_list)

    related_user_dict = find_similar_user(normalized_dict_ratings, user_input)

    most_related_user = (max(related_user_dict, key=lambda k: related_user_dict[k]))

    print(most_related_user)
    #
    # print(user_list[most_related_user - 1])

    # print(user_list[0])

    movie_suggestion_list = (return_movie_suggestion(user_input, most_related_user, user_list))

    for movie in movie_list:
        if movie.movie_id in movie_suggestion_list:
            print(movie.movie_title)




def show_pop(*args):
    rating_list = create_rating_list()

    movie_ratings = create_movie_ratings_dict(rating_list)

    movie_list = create_movie_list(movie_ratings)

    all_ratings_by_user = create_all_ratings_by_user_dict(rating_list)

    user_list = create_user_list(all_ratings_by_user)

    print(print_top_twenty_titles(movie_list))



def show_pop_not_rated(*args):
    rating_list = create_rating_list()

    movie_ratings = create_movie_ratings_dict(rating_list)

    movie_list = create_movie_list(movie_ratings)

    all_ratings_by_user = create_all_ratings_by_user_dict(rating_list)

    user_list = create_user_list(all_ratings_by_user)

    unrated_pop = print_top_twenty_titles_not_rated(movie_list, user_list, user_input_id)











    # try:
    #     value = float(feet.get())
    #     meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    # except ValueError:
    #     pass

root = Tk()
root.title("What to watch?")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

id_input = IntVar()
meters = StringVar()

user_id_input = (ttk.Entry(mainframe, width=7, textvariable=id_input))
user_id_input.grid(column=2, row=1, sticky=(W, E))



ttk.Label(mainframe, textvariable=meters).grid(column=3, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Find Movie", command=calculate).grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, textvariable=meters).grid(column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Show Popular Movies", command=show_pop).grid(column=3, row=2, sticky=W)

ttk.Label(mainframe, textvariable=meters).grid(column=3, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Show Popular Movies that you haven't rated", command=show_pop_not_rated).grid(column=3, row=3, sticky=W)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

user_id_input.focus()
root.bind('<Return>', calculate)

root.mainloop()
