import media
import webbrowser
import fresh_tomatoes

movies = [
    {'title': '',
     'plot': '',
     },
    {},
]

movies = [media.Movie(**m) for m in movies]
    
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys who come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

three_idiots = media.Movie("3 Idiots",
                     "A creative goof in an engineering college changes his friends' lives forever.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg",
                     "https://youtu.be/K0eDlFX9GMc?t=16s")
#webbrowser.open(three_idiots.trailer_youtube_url)

castle_in_the_sky = media.Movie("Castle in the Sky",
                     "A young girl who has access to powerful technology is hunted by air pirates.",
                     "https://images-na.ssl-images-amazon.com/images/I/51281TEF3GL._SY445_.jpg",
                     "https://www.youtube.com/watch?v=McM0_YHDm5A")

seven_samurai = media.Movie("Seven Samurai",
                     "A village threatened by bandits gets help from a rag-tag group of samurai.",
                     "https://pics.filmaffinity.com/Seven_Samurai-779845843-large.jpg",
                     "https://www.youtube.com/watch?v=7mw6LyyoeGE")

terminator_2 = media.Movie("Terminator 2",
                     "An time-treavelling android tries to protect the future of humanity.",
                     "https://posterspy.com/wp-content/uploads/2015/08/t2.png",
                     "https://www.youtube.com/watch?v=lwSysg9o7wE")

pan_labyrinth = media.Movie("Pan's Labyrinth",
                     "A young girl explores a fantastical world while the conflicts of civil war rip apart her reality.",
                     "http://www.impawards.com/2006/posters/pans_labyrinth_ver6.jpg",
                     "https://www.youtube.com/watch?v=EqYiSlkvRuw")

jaanetu = media.Movie("Jaane Tu... Ya Jaane Na",
                     "A young girl explores a fantastical world while the conflicts of civil war rip apart her reality.",
                     "https://i.jeded.com/i/jaane-tu-ya-jaane-na.35749.jpg",
                     "https://www.youtube.com/watch?v=NYqqFeLzRiI")

movies = [toy_story, avatar, three_idiots, castle_in_the_sky, seven_samurai, terminator_2, pan_labyrinth, jaanetu]
fresh_tomatoes.open_movies_page(movies)


