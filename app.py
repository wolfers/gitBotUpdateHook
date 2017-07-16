from flask import Flask
import os
import subprocess

app = Flask(__name__)


class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

@app.route('/', methods=['POST', 'GET'])
def index():
    with cd('/home/pi/thombot_v2'):
        subprocess.run('sudo git pull', shell=True)
    subprocess.run('sudo systemctl restart discbot', shell=True)
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
