from app.create_app import create_app
from app.flask_config import Config
import pymongo

app_config = Config()
client = pymongo.MongoClient(f"{app_config.db_url}")
db = client[f'{app_config.db_name}']
collection = db[F'{app_config.todo_collection_name}']

app = create_app(db, app_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0')