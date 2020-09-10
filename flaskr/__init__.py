from flask import Flask, render_template, send_file, current_app as app
import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/portfolio')
    def portfolio():
        return render_template('portfolio.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/game_of_life')
    def game_of_life():
        return render_template('game-of-life.html')

    @app.route('/net_quest')
    def net_quest():
        return render_template('net-quest.html')

    @app.route('/credits')
    def credits():
        return render_template('credits.html')

    return app



