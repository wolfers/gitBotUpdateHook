from flask import Flask
from sh import git, cd
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    cd('/home/pi/thombot_v2')
    git.pull()
    subprocess.run('sudo systemctl restart discbot', shell=True)
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
