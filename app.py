from core.core import create_app
from flask import jsonify



app = create_app()

@app.errorhandler(404)
def not_found(e):

    return jsonify(
        {
            "error": 404,
            "message": "The URL specified doesn't exist"
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)