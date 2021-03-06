![Python package](https://github.com/lhotakj/flask-demo/workflows/Python%20package/badge.svg?event=push)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lhotakj_flask-demo&metric=alert_status)](https://sonarcloud.io/dashboard?id=lhotakj_flask-demo)

# MVC Flask demo hosted on heroku

A simple demo MVC flask, for handling Slack commands and events and provide a simplified admin consoled to manage AWS instances (skeleton only, no boto3 code) with sample graphs.

_Third party libraries_:
* jQuery v3.4.1 (https://jquery.org) - local copy
* Bootstrap v4.4.1 (https://getbootstrap.com/) - local copy 
* DataTables v1.10.20 (https://datatables.net) - local copy
* Popper v2 (https://popper.js.org/) - local copy
* Chart v2.5 (https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js)

## Running the app
There are three ways of running the app, it defaults run on port `5000`. Feel free to change it in `./app/config/Configuration.py`, but then you need to update also all the shells!

### 1) Debug app: 
```
python3 -m pip install -r requirements.txt
./debug.sh
```

### 2) Run the app with gunicorn 
```
python3 -m pip install -r requirements.txt
./run.sh
```
### 3) Run the app in Docker
```
cd docker
./docker_build.sh
./docker_run.sh
```

In all three ways the app becomes available on `http://127.0.0.1:5000`

To stop and remove container run
```
cd docker
./docker_stop.sh
```

The demo is deployed on Heroku: https://jarda-demo.herokuapp.com/

Admin console: https://dashboard.heroku.com/apps/jarda-demo

todo: https://www.codeply.com/go/3l6UhaQEhq
