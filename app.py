import logging
import time
import xml.etree.ElementTree as ET
from flask import Flask, request, jsonify, g, Response
from src.estimator import estimator
from src.validate_user_input import (
    get_region_data,
    validate_input_data,
    validate_input_type
)
from src.xml_generator import create_xml_tree, prettify

app = Flask(__name__)
logging.basicConfig(filename='api_logs.txt', level=logging.INFO)


@app.before_request
def get_time():
    g.start = time.time()


@app.route(
    '/api/v1/on-covid-19', methods=['GET', 'POST'], defaults={
        'data_format': None})
@app.route('/api/v1/on-covid-19/<data_format>', methods=['GET', 'POST'])
def get_estimation(data_format):
    """
    Endpoint that can take the input data and
    return the estimation for it.
    It returns a json format as default or xml format
    if provided as part of the url.
    """
    data = request.get_json()
    region_data = get_region_data(data)
    try:
        cleaned_data = validate_input_data(region_data)
    except AssertionError as err:
        return jsonify({'error': err.args[0]}), 409

    try:
        validate_input_type(cleaned_data)
    except AssertionError as err:
        return jsonify({'error': err.args[0]}), 409

    result = estimator(cleaned_data)
    if data_format not in ['xml', 'json', None]:
        return jsonify({
            'message': 'Wrong data format. Check your URL'}), 400

    if data_format == 'xml':
        xml_file = prettify(create_xml_tree(ET.Element('root'), result))
        return Response(
            xml_file,
            mimetype='text/xml',
            content_type='application/xml')

    if data_format == 'json':
        return jsonify(result), 200

    return jsonify(result), 200


@app.route('/api/v1/on-covid-19/logs', methods=['GET', 'POST'])
def get_logs():
    """
    Endpoint that returns logs in a text file.
    """
    if request.method != 'GET':
        return jsonify({'error': 'Method not arrowed'}), 405

    data_logs = []
    with open('api_logs.txt', 'rt') as f:
        data = f.readlines()
    for line in data:
        if 'root' in line and '404' not in line:
            data_logs.append(line[10:] + '\n')

    return Response(
        ''.join(data_logs),
        mimetype='text/plain',
        )


@app.after_request
def log_request_info(response):
    """Produces the app logs after response is made"""

    elapsed_time = int((time.time() - g.start)*1000)
    status_code = response.status.split()[0]
    logging.info(
        f"{request.method}\t\t{request.path}\t\t{status_code}\t\t{str(elapsed_time).zfill(2)}ms"  # noqa
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
