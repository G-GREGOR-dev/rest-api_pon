import flask
from flask import jsonify
from flask import make_response
from data import db_session
from data.jobs import Job
from flask import request


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_correct_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'Jobs': jobs.to_dict(only=('team_leader', 'id', 'job', 'work_size', 'collaborators', 'is_finished', 'start_date', 'end_date'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'id', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    proverka = db_sess.query(Job).get(request.json['id'])
    if proverka:
        return jsonify({'error': 'Id already exists'})
    else:
        job = Job()
        job.team_leader = request.json['team_leader']
        job.id = request.json['id']
        job.job = request.json['job']
        job.work_size = request.json['work_size']
        job.collaborators = request.json['collaborators']
        job.is_finished = request.json['is_finished']
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs')
def get_all_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                'team_leader', 'id', 'job', 'work_size', 'collaborators', 'is_finished', 'start_date', 'end_date'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:news_id>', methods=['DELETE'])
def delete_job(news_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).get(news_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs', methods=['PUT'])
def edit_job():
    db_sess = db_session.create_session()
    job = db_sess.query(Job).get(request.json['id'])
    if not job:
        return jsonify({'error': 'Not found'})
    job_for_me = Job()
    job_for_me.team_leader = job.team_leader
    job_for_me.id = job.id
    job_for_me.job = job.job
    job_for_me.work_size = job.work_size
    job_for_me.collaborators = job.collaborators
    job_for_me.is_finished = job.is_finished
    job_for_me.start_date = job.start_date
    job_for_me.end_date = job.end_date
    db_sess.delete(job)
    db_sess.commit()
    for key, volue in request.json.items():
        setattr(job_for_me, key, volue)
    db_sess.add(job_for_me)
    db_sess.commit()
    return jsonify({'success': 'OK'})
