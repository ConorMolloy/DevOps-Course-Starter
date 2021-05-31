"""create_app function that specifies the routes of the app"""
from flask import Flask, render_template, request, redirect
from app.viewmodel import ViewModel
from app.flask_config import Config
from app.client_interface import ClientInterface

def create_app(client: ClientInterface, config: Config):
    """
    Args:
        client (ClientInterface):
            The interface a client must conform to for the app to work as expected
        config (Config): Config class with environment  variables initialised
    """
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/', methods=['GET'])
    def index():
        """
        Returns:
            HTML template: Returns index.html populated with a ViewModel
        """
        view_model = ViewModel(client.get_items())
        return render_template('index.html', view_model=view_model)


    @app.route('/', methods=['POST'])
    def post_item():
        """
        Accepts an incoming item, saves the item and redirects to index()
        """
        client.add_item(request.form.get('item'))
        return redirect('/')


    @app.route('/update/<item_id>', methods=['POST'])
    def mark_complete(item_id):
        """
        Accepts an incoming id, marks the item as complete and redirects to index()

        Args:
            id (str): id of the item that is to be marked as complete
        """
        client.mark_complete(item_id)

        return redirect('/')


    @app.route('/delete/<item_id>', methods=['GET'])
    def delete_item(item_id):
        """
        Accepts an incoming id, deletes the item and redirects to index()

        Args:
            id (str): id of the item that is to be deleted
        """
        client.delete_item_by_id(item_id)
        return redirect('/')

    return app
