"""Entry point for Flask"""
from flask_login import LoginManager
from pymongo import MongoClient
from app.create_app import create_app
from app.flask_config import DatabaseConfig, AuthConfig, FlaskConfig
from app.atlas_client import AtlasClient

database_config = DatabaseConfig()
auth_config = AuthConfig()
flask_config = FlaskConfig()
mongo_client = MongoClient(database_config.db_url)
atlas_client = AtlasClient(database_config, mongo_client)
login_manager = LoginManager()

app = create_app(atlas_client, auth_config, flask_config, login_manager)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
