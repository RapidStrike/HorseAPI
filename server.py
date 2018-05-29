import time

from flask import Flask, request
from flask_restful import Resource, Api
from flask.json import jsonify

from src.resource import PonyResource


app = Flask(__name__)
api = Api(app)
db = PonyResource()
app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)


# ALL #
@api.resource('/episodes')
class Episodes(Resource):
    def get(self):
        return jsonify([ep.print() for ep in db.episodes])


@api.resource('/movies')
class Movies(Resource):
    def get(self):
        return jsonify([mov.print() for mov in db.movies])


@api.resource('/all')
class AllEpisodes(Resource):
    def get(self):
        return jsonify([value.print() for value in db.episodes + db.movies])


# SPECIFIC #
@api.resource('/newest')
class NewestEpisode(Resource):
    def get(self):
        new_ep = None
        curr_time = int(time.time())
        for ep in db.episodes:
            if int(ep.air_date) > curr_time:
                new_ep = ep
                break
        if new_ep:
            return jsonify(new_ep.print())
        else:
            return error_400('No new episode found. Hiatus?')


@api.resource('/season/<season>')
class SeasonFetch(Resource):
    def get(self, season):
        try:
            season_list = [ep.print() for ep in db.episodes if ep.season == int(season)]
        except ValueError:
            return error_400('Season must be a number.')
        if season_list:
            return jsonify(season_list)
        else:
            return error_400('Season does not exist.')


@api.resource('/season/<season>/episode/<episode>')
class EpisodeFetch(Resource):
    def get(self, season, episode):
        try:
            target_ep = next((ep.print() for ep in db.episodes if ep.season == int(season) and ep.episode == int(episode)), None)
        except ValueError:
            return error_400('Season and episode must be a number.')
        if target_ep:
            return jsonify(target_ep)
        else:
            return error_400('Episode does not exist.')


def error_400(error_msg):
    resp = jsonify({'error': error_msg})
    resp.status_code = 400
    return resp


if __name__ == '__main__':
    app.run(port='5000')

