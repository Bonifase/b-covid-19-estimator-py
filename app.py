import os
import logging
import time
import xml.etree.ElementTree as ET
from flask import Flask, request, jsonify, g, Response
from src.estimator import estimator
from src.generate_lines import get_logs_lines
from src.xml_generator import output, create_xml_tree

app = Flask(__name__)
logging.basicConfig(filename='request.txt', level=logging.INFO)


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
    result = estimator(data)

    if data_format == 'xml':
        tree_root = create_xml_tree(ET.Element("root"), result)
        output(tree_root)
        src = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 'estimate.xml'
        )
        file = open(src).read()
        return Response(
            file,
            mimetype="application/xml",
            content_type='text/xml; charset=utf-8')
    if data_format == 'json':
        return jsonify({'estimate': result})

    return jsonify({'estimate': result})


@app.route('/api/v1/on-covid-19/logs', methods=['GET'])
def get_logs():
    """
    Endpoint that returns logs in a text file.
    """
    data_logs = []
    with open('request.txt', 'rt') as f:
        data = f.readlines()
    for line in data:
        if 'root' in line and 'logs' not in line:
            data_logs.append(line[10:])

    with open('logs.txt', 'w') as filehandle:
        for list_item in data_logs:
            filehandle.write('%s\n' % list_item)
    log_file = "logs.txt"
    data = get_logs_lines(log_file, 100)

    return Response(data, mimetype='text/plain')


@app.after_request
def log_request_info(response):
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)
    status_as_integer = response.status_code
    logging.info("{method} {path} {status} {time}".format(
        method=request.method,
        path=request.path,
        status=status_as_integer,
        time=g.request_time()))
    return response


if __name__ == '__main__':
    app.run(debug=True)
