from flask import Flask, request, jsonify
from src.estimator import estimator

app = Flask(__name__)


@app.route('/api/v1/on-covid-19', methods=['GET'], defaults={'data_format': 'json'})
@app.route('/api/v1/on-covid-19/<data_format>', methods=['GET'])
def get_estimation(data_format):
    """
    Endpoint that can take the input data and
    return the estimation for it.
    """
    data = request.get_json()
    result = estimator(data)
    return jsonify({'estimate': result})


if __name__ == '__main__':
    app.run(debug=True)
