# PlanGrid DevOps

## Description

Flask application that returns a message depending on accept headers for a GET request

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 2.7
* __Version Control:__ Git 1.9.1
* __Package Management:__ Pip 1.5.4
* __Framework:__: Flask 1.0.2

## Install Environment

Installed the following before running application (if not already installed):

### Update Packages
```
$ sudo apt-get update
```

### Install Python and Pip
```
$ sudo apt-get install -y python python-pip
```

### Install Git
```
$ sudo apt-get install -y git
```

### Install Flask
```
$ sudo pip install flask
```


## To Use

### Clone Repo
```
$ sudo git clone https://github.com/kjowong/PG_DevOps_HW.git
```

### Start application 
```
$ python app/request_app.py
```

### Start the application (Debug log level)
```
$ python app/request_app.py debug
```

## Tests

### Run Unittest
```
$ python -m unittest -v tests.test_app
```

### Test Application with on commandline

Accept Header with content type value application/json
```
$ curl --header "Accept: application/json" http://0.0.0.0:5000/

# Expected Response:
{"message": "Good morning"}
```

No Accept Header
```
$ curl http://0.0.0.0:5000/

# Expected Response:
{"message": "Good morning"}
```
