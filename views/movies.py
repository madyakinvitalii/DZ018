from flask import request
from flask_restx import Resource, Namespace

from container import movie_service, movie_dao
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id:
            movies_by_director = movie_service.get_all_by_director(director_id)
            return movies_schema.dumps(movies_by_director), 200
        elif genre_id:
            movies_by_genre = movie_service.get_all_by_genre(genre_id)
            return movies_schema.dumps(movies_by_genre), 200
        elif year:
            movies_by_year = movie_service.get_all_by_year(year)
            return movies_schema.dumps(movies_by_year), 200
        else:
            all_movies = movie_service.get_all()
            return movies_schema.dumps(all_movies), 200

    def post(self):
        req_json = request.json
        movie_dao.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_service.update(req_json)

        return "", 204

    def patch(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)

        return "", 204
