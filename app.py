from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
from config import Config
from utils.database import init_db, get_db
from utils.mock_data import generate_mock_data
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize database
    init_db()

    # Register blueprints
    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    from routes.api import api_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/setup-demo')
    def setup_demo():
        """Generate mock data for demo purposes"""
        try:
            generate_mock_data()
            return jsonify({"message": "Demo data generated successfully!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)