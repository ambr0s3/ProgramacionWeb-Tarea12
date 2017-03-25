from flask import request, Blueprint
from movier.data.models import db, Movie, Review
import urllib.request
import os

main = Blueprint('main', __name__, template_folder='templates')

@main.route('movies', methods=["POST"])
def movie_handler():
  if request.method == 'POST':
    data = request.form.to_dict();
    print(data)
    if Movie.query.filter_by(name=data["title"]).first() == None:
      if 'poster' in data:
        posterUrl = "http://image.tmdb.org/t/p/w150" + data["poster"]
        localUrl = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/client/static/images/posters/" + data["id"] + ".jpg"
        urllib.request.urlretrieve(posterUrl, localUrl)
        movie = Movie(data["id"], data["title"], data["description"], data["poster"]);
      else:
        movie = Movie(data["id"], data["title"], data["description"], None);
      db.session.add(movie)
      db.session.commit()
      return "SAVED!"
    else:
      return "EXISTS!"

@main.route('reviews', methods=["POST"])
def review_handler():
    if request.method == 'POST':
      data = jsonify(request.form);
    if "movie_name" and "description" and "poster" and "score" and "review" and "user" and "device_id" not in data:
     abort(404, 'HTTP 404 Not Found')
     return "SUCCESS!"
