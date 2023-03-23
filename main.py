import datetime

from data import db_session
import news_api
from flask import Flask
from data.jobs import Job
from data.users import User
from flask import jsonify
from flask import make_response
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    job = Job()
    job.id = 1
    job.name = "Пользователь 1"
    job.job = "субботник"
    job.work_size = 6
    job.collaborators = ""
    job.is_finished = False
    job.start_date = datetime.datetime.now()
    job.end_date = datetime.datetime.now()
    db_sess.add(job)
    db_sess.commit()
    user = User()
    user.name = "Пользователь 1"
    user.surname = "surname 1"
    user.age = 199
    user.about = "биография пользователя 1"
    user.position = "123"
    user.speciality = "qwdasc"
    user.address = "asdcx"
    db_sess.add(user)
    db_sess.commit()
    app.register_blueprint(news_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
