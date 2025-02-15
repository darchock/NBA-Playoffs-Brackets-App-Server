### Itamar ENV ###

1. In order to work in virual env run:
        # To use virtual env in a new terminal (which should already contain all packets):
                source venv/bin/activate  # macOS/Linux
2. To run the server and client:
        # In client:
                npm start
        # In server:
                python3 main.py
3. Connect to database:
        # make sure MySQL local version is 8.x.x and not 9.x.x which doesn't support rds (mysql --version)
        mysql -h database-nba-playoff-prediction.cjsgac0qm87k.us-east-2.rds.amazonaws.com -u admin -p


# First time env ramp up:
1. To initialize the virtual env:
                python3 -m venv venv
2. Expected outputs for versions in the vitural env:
        python3 --version:
                Python 3.13.2
        pip --version
                pip 25.0 from /Users/itamaral/Documents/euro2025/EURO-PREDICTIONS/app/venv/lib/python3.13/site-packages/pip (python 3.13)
3. For first time setup in the virtual env I ran:
        pip install flask
        pip install flask_cors
        npm install react-scripts (run inside of client repo)
