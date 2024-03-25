import os
import json
import logging
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)  # Set log level as desired


@app.route('/')
def read_file():
    try:

        env_details = {}

        for name, value in os.environ.items():
            app.logger.info("{0}: {1}".format(name, value))
            print("{0}: {1}".format(name, value))
            env_details[name] = value

        json_object = json.dumps(env_details, indent = 4)

        return jsonify(json.loads(json_object)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)