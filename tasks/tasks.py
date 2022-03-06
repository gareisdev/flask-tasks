from flask import Blueprint
from flask import request
import json
from os import path
from flask_restful import Resource, Api



tasks_bp = Blueprint("tasks_blueprint",__name__)
path_db_tasks = path.realpath("database/tasks.json")


api = Api(tasks_bp)

class TasksResource(Resource):

    def get(self):

        with open(path_db_tasks, "r") as file:
            tasks = json.load(file)

        args = request.args

        if args.get("completed"):
            if args.get("completed").lower() == "true":
                tasks = list(filter( lambda x: x.get("completed") == True, tasks))
            else:
                tasks = list(filter( lambda x: x.get("completed") == False, tasks))
            
        if args.get("title"):
            tasks = list(filter( lambda x: args.get("title") in x.get("completed"), tasks))


        dict_response = {
            "total_items": len(tasks),
            "data": tasks
        }

        return dict_response, 200


class TaskResource(Resource):

    def get(self, id):
        with open(path_db_tasks, "r") as file:
            tasks = json.load(file)
        
        task = list(filter( lambda x: x.get("id") == id, tasks))

        if task:
            return task, 200
        else:
            return {}, 404



class TasksInfoResource(Resource):

    def get(self):

        with open(path_db_tasks, "r") as file:
            tasks = json.load(file)


        total = len(tasks)
        count_completed = len(list(filter( lambda x: x.get("completed") == True, tasks)))
        count_no_completed = len(list(filter( lambda x: x.get("completed") == False, tasks)))

        dict_response = {
            "total": total,
            "completed": count_completed,
            "no_completed": count_no_completed
        }

        return dict_response, 200

api.add_resource(TasksResource, "/tasks")
api.add_resource(TaskResource, "/tasks/<int:id>")
api.add_resource(TasksInfoResource, "/tasks/info")
