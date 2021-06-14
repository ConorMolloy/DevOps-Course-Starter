"""create_app function that specifies the routes of the app"""
from uuid import uuid4
from flask import Flask, render_template, request, redirect, session, abort
from flask_login import LoginManager, login_required, login_user, current_user
from oauthlib.oauth2 import WebApplicationClient
import requests
from app.viewmodel import ViewModel
from app.flask_config import FlaskConfig, AuthConfig
from app.client_interface import ClientInterface
from app.user import User
from app.auth_utils import authorized_for
from app.role import Role

def create_app(
                client: ClientInterface,
                auth_config: AuthConfig,
                flask_config: FlaskConfig,
                login_manager: LoginManager
                ):
    """
    Args:
        client (ClientInterface):
            The interface a client must conform to for the app to work as expected
        config (Config): Config class with environment  variables initialised
    """
    app = Flask(__name__)
    app.config.from_object(flask_config)

    login_manager.init_app(app)

    web_application_client = WebApplicationClient(auth_config.client_id)

    @login_manager.unauthorized_handler
    def unauthenticated():
        session['state'] = uuid4()
        return redirect(web_application_client.prepare_request_uri(
            'https://github.com/login/oauth/authorize', state=session['state'])
            )

    @app.route('/login')
    def login_callback():
        auth_code = request.args.get('code')
        state = request.args.get('state')
        if str(session['state']) != state:
            abort(401)
        url, _, body = web_application_client.prepare_token_request(
            'https://github.com/login/oauth/access_token',
            client_id=auth_config.client_id,
            client_secret=auth_config.client_secret,
            code=auth_code,
            state=state)

        token_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        token_response = requests.post(
            url,
            headers=token_headers,
            data=body,
            auth=(
                auth_config.client_id,
                auth_config.client_secret
            ),
        )

        web_application_client.parse_request_body_response(token_response.content)

        uri, headers, _ = web_application_client.add_token('https://api.github.com/user')

        userinfo_response = requests.get(uri, headers=headers)

        user_id = userinfo_response.json()['login']
        login_user(User(user_id))

        return redirect('/')

    @login_manager.user_loader
    def load_user(user_id):
        if user_id == auth_config.writer_user:
            return User(user_id, role=Role.WRITER.value)
        return User(user_id)

    @app.route('/')
    @login_required
    def index():
        """
        Returns:
            HTML template: Returns index.html populated with a ViewModel
        """
        view_model = ViewModel(client.get_items(), current_user)
        return render_template('index.html', view_model=view_model)


    @app.route('/', methods=['POST'])
    @login_required
    @authorized_for('writer')
    def post_item():
        """
        Accepts an incoming item, saves the item and redirects to index()
        """
        client.add_item(request.form.get('item'))
        return redirect('/')


    @app.route('/update/<item_id>', methods=['POST'])
    @login_required
    @authorized_for('writer')
    def mark_complete(item_id):
        """
        Accepts an incoming id, marks the item as complete and redirects to index()

        Args:
            id (str): id of the item that is to be marked as complete
        """
        client.mark_complete(item_id)

        return redirect('/')


    @app.route('/delete/<item_id>', methods=['GET'])
    @login_required
    @authorized_for('writer')
    def delete_item(item_id):
        """
        Accepts an incoming id, deletes the item and redirects to index()

        Args:
            id (str): id of the item that is to be deleted
        """
        client.delete_item_by_id(item_id)
        return redirect('/')

    return app
