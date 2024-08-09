# app/routes.py
from flask import Blueprint, request, jsonify
from app.models import db, Post

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.serialize() for post in posts])


@api_blueprint.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.serialize())


@api_blueprint.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(userId=data['userId'], title=data['title'], body=data['body'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.serialize()), 201


@api_blueprint.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    post = Post.query.get_or_404(id)
    post.title = data['title']
    post.body = data['body']
    db.session.commit()
    return jsonify(post.serialize())


@api_blueprint.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return '', 204


# Add serialization method to Post model
def serialize(self):
    return {
        'userId': self.userId,
        'id': self.id,
        'title': self.title,
        'body': self.body
    }


Post.serialize = serialize
