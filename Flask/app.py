from flask import Flask

import time
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(1)
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '8080')))
