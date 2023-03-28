from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDAO(db)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db)
genre_service = GenreService(genre_dao)

