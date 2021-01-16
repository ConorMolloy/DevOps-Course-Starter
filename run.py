from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')