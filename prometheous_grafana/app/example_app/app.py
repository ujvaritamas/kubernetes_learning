import os
import json
import logging
from flask import Flask, jsonify, Response

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)  # Set log level as desired

#example for prometheus
metrics_data = {
    'metric_example0_cntr': 0,
    'metric_example1_const': 20,
    'metric_example2_cntr_root': 0
    }


@app.route('/')
def read_env_vars():
    try:
        #increment metric
        metrics_data['metric_example2_cntr_root'] += 1

        env_details = {}

        for name, value in os.environ.items():
            app.logger.info("{0}: {1}".format(name, value))
            print("{0}: {1}".format(name, value))
            env_details[name] = value

        json_object = json.dumps(env_details, indent = 4)

        return jsonify(json.loads(json_object)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/counter')
def increment_counter():
    try:
        app.logger.info("/counter endpoint called")
        metrics_data['metric_example0_cntr'] += 1

        return str(metrics_data['metric_example0_cntr']), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/metrics')
def metrics():
    # Assuming metrics_data is a dictionary containing your metrics
    metrics_text = ""
    for metric_name, metric_value in metrics_data.items():
        metrics_text += f"{metric_name} {metric_value}\n"

    return Response(metrics_text, mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)