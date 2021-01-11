from flask import Flask, render_template, request, redirect, url_for
import trello_client as session
from viewmodel import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/', methods=['GET'])
    def index():
        sorted_items = sorted(session.get_items(), key=lambda item: item.status, reverse=True)
        view_model = ViewModel(sorted_items)
        return render_template('index.html', view_model=view_model)


    @app.route('/', methods=['POST'])
    def post_item():
        session.add_item(request.form.get('item'))
        return redirect('/')


    @app.route('/update/<id>', methods=['POST'])
    def mark_complete(id):
        session.mark_complete(id)

        return redirect('/')


    @app.route('/delete/<id>', methods=['GET'])
    def delete_item(id):
        session.delete_item_by_id(id)
        return redirect('/')    

    if __name__ == '__main__':
        app.run()

    return app
