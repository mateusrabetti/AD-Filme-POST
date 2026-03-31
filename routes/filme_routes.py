from flask import Blueprint, request
from controllers.filme_controllers import create_filme

filme_routes = Blueprint('filme_routes',__name__)

@filme_routes.route('/filme',methods=['POST'])
def filmes_post():
    filme_data = request.json
    return create_filme(request.json)