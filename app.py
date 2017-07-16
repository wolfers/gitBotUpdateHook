from flask import Flask
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    with os.chdir('/home/pi/thombot_v2'):
        subprocess.run('git pull', shell=True)
    subprocess.run('sudo systemctl restart discbot', shell=True)
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
