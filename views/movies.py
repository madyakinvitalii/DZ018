from flask import request
from flask_restx import Resource, Namespace

from container import movie_service, movie_dao
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

Movie_schema = MovieSchema()
Movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        print('1')
        all_movies = movie_service.get_all()
        return Movies_schema.dumps(all_movies), 200

    def post(self):
        req_json = request.json
        movie_dao.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return Movie_schema.dump(movie), 200

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