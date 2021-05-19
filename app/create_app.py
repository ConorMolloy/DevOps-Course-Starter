from flask import Flask, render_template, request, redirect
from app.viewmodel import ViewModel
from app.atlas_client import AtlasClient
from app.flask_config import Config
from pymongo.database import Database

def create_app(client: AtlasClient, config: Config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/', methods=['GET'])
    def index():
        view_model = ViewModel(client.get_items())
        return render_template('index.html', view_model=view_model)


    @app.route('/', methods=['POST'])
    def post_item():
        client.add_item(request.form.get('item'))
        return redirect('/')


    @app.route('/update/<id>', methods=['POST'])
    def mark_complete(id):
        client.mark_complete(id)

        return redirect('/')


    @app.route('/delete/<id>', methods=['GET'])
    def delete_item(id):
        client.delete_item_by_id(id)
        return redirect('/')    

    return app
