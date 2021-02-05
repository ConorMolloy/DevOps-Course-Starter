from flask import Flask, render_template, request, redirect
from trello_client import Routes
from viewmodel import ViewModel

def create_app():
    routes = Routes()
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/', methods=['GET'])
    def index():
        sorted_items = sorted(routes.get_items(), key=lambda item: item.status, reverse=True)
        view_model = ViewModel(sorted_items)
        return render_template('index.html', view_model=view_model)


    @app.route('/', methods=['POST'])
    def post_item():
        routes.add_item(request.form.get('item'))
        return redirect('/')


    @app.route('/update/<id>', methods=['POST'])
    def mark_complete(id):
        routes.mark_complete(id)

        return redirect('/')


    @app.route('/delete/<id>', methods=['GET'])
    def delete_item(id):
        routes.delete_item_by_id(id)
        return redirect('/')    

    return app
