from flask import Flask
app = Flask(__name__)

app.config.from_object('flask_default_config')
app.config.from_object('flask_config')

import pythonserver.views
