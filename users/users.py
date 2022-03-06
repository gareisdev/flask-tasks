from flask import Blueprint
import json
from os import path
from flask_restful import Resource, Api

users_bp = Blueprint("users_blueprint",__name__)

# Path to JSON files
path_db_user = path.realpath("database/users.json")
path_db_tasks = path.realpath("database/tasks.json")

api = Api(users_bp)


class UsersResource(Resource):

    def get(self):

        with open(path_db_user, "r") as file:
            users = json.load(file)

        dict_response = {
            "total_items": len(users),
            "data": users
        }

        return dict_response, 200

class UserResource(Resource):

    def get(self, id):

        with open(path_db_user, "r") as file:
            users = json.load(file)

        user = list(filter( lambda x: x.get("id") == id, users))

        if user:
            return user[0], 200

        return {}, 404


class UserTasksResource(Resource):
    def get(self, user_id):
        with open(path_db_tasks, "r") as file:
            tasks = json.load(file)

        user_tasks = list(filter( lambda x: x.get("user_id") == user_id, tasks))

        if user_tasks:

            dict_response = {
                "total_items": len(user_tasks),
                "data": user_tasks
            }

            return dict_response, 200

        return [], 404

api.add_resource(UsersResource, "/users")
api.add_resource(UserResource, "/users/<int:id>")
api.add_resource(UserTasksResource, "/users/<int:user_id>/tasks")