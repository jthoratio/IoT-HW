# IoT Communication HW

## Environment 
- Ubuntu 20.04.3 on Oracle VirtualBox 6.1
## How to Run
- Install project dependencies
```bash
# Install protobuf compiler
$ sudo apt install protobuf-compiler

# Install buildtools
$ sudo apt install build-essential make

# Install packages
$ pip3 install -r requirements.txt
```
- Compile protobuf schema to python wrapper
```bash
$ make
```
- Run the eclipse mosquitto docker container
```bash
$ cd src/
$ sudo docker run -d -it -p 1883:1883 -v $(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```
- Start the fibonacci service
```bash
$ cd src/
$ python3 fib.py --ip 0.0.0.0 --port 8080
```
- Start the log service
```bash
$ cd src/
$ python3 log.py --ip 0.0.0.0 --port 8081
```
- Migrate databases
```bash
$ cd src/
$ python3 manage.py migrate
```
- Start the backend server
```bash
$ cd src/
$ python3 manage.py runserver 0.0.0.0:8000
```
## Send Request
- Request order N of fibonacci sequence
```bash
$ curl -X POST http://localhost:8000/rest/fibonacci -d '{"order":N}'
```
- Request history of requests
```bash
$ curl http://localhost:8000/rest/logs
```
## Tutorial
- https://youtu.be/K3EYvtjOWIE
## Tutorial Video
- https://youtu.be/K3EYvtjOWIE

