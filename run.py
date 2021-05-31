"""Entry point for Flask"""
import pymongo
from app.create_app import create_app
from app.flask_config import Config
from app.atlas_client import AtlasClient

app_config = Config()
client = pymongo.MongoClient(app_config.db_url)
db = client[app_config.db_name]
atlas_client = AtlasClient(db, app_config)

app = create_app(atlas_client, app_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
