from flask import Flask
from sh import systemctl, git, cd

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    cd('/home/pi/thombot_v2')
    git.pull()
    systemctl('restart', 'discbot')
#    call('sudo systemctl restart discbot', shell=True)
    return 'Success'

if __name__ == '__main__':
    app.run()
