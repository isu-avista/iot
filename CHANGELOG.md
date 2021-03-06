# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Removed

## [v0.3.10](https://github.com/isu-avista/iot/releases/tag/v0.3.10) - 2021-03-12
### Added
* Added `qemu-user-static` package to travis.yml for building for arm architecture
* Added a method to `generate_configs.py` that will create the logs directory and log file if they don't exist

### Changed
* `docker_push` script now uses buildx to build docker images for arm architecture
* Made some syntactical changes to `install.sh` and apt install pip for docker-compose

### Removed
* Removed the call to `Process` in `app.py` that starts the default flask web server

## [v0.3.9](https://github.com/isu-avista/iot/releases/tag/v0.3.9) - 2021-02-19
### Added

### Changed
* Updated to include changes in avista-data and avista-base-server

### Removed
* Removed all code that interacted with the sensors and place it in the sensors module
* The server now only provides the ability to configure the system, and does not have anything to do with data collection

## [v0.3.8](https://github.com/isu-avista/iot/releases/tag/v0.3.8) - 2021-02-17
### Added

### Changed
* Updated to recent base-server

### Removed

## [v0.3.7](https://github.com/isu-avista/iot/releases/tag/v0.3.7) - 2021-02-16
### Added

### Changed
* Fixed the dockerfile, docker-compose spec, and the docker_push script to correctly produce the project in order to ensure it is installation ready.

### Removed

## [v0.3.6](https://github.com/isu-avista/iot/releases/tag/v0.3.6) - 2021-02-16
### Added

### Changed
* Minor fix to the docker_push script

### Removed

## [v0.3.5](https://github.com/isu-avista/iot/releases/tag/v0.3.5) - 2021-02-16
### Added

### Changed
* Added a line to the docker-compose to map the host port 5000 to the backend port 5000

### Removed

## [v0.3.4](https://github.com/isu-avista/iot/releases/tag/v0.3.4) - 2021-02-16

### Added
* script to build and push docker images

### Changed
* Updated requirements.txt
* Updated documentation

### Removed

## [v0.3.3](https://github.com/isu-avista/iot/releases/tag/v0.3.3) - 2021-02-15

### Added

### Changed
* Fixed minor error in install script

### Removed

## [v0.3.2](https://github.com/isu-avista/iot/releases/tag/v0.3.2) - 2021-02-15

### Added

### Changed
* Fixed minor errors in the systemd service specification, verified on RPi 4 to be correct
* Updated the requirements.txt file
* Fixed minor errors in the docker-compose.yml file
* Updated documentation

### Removed

## [v0.3.1](https://github.com/isu-avista/iot/releases/tag/v0.3.1) - 2021-02-14

### Added

### Changed
* Updated to most recent version of the base-server
* Improved the install script to correctly use curl
* Updated documentation

### Removed

## [v0.3.0](https://github.com/isu-avista/iot/releases/tag/v0.3.0) - 2021-02-14

### Added

* Added installation scripts
* Added systemd service
* Added a script to generate the configuration information during docker build

### Changed

* App.py to conform to the definition found in base-server
* Updated the Dockerfiles to build the images in order to have the correct bindings
* Updated the docker-compose.yml file to use the images from the docker-hub repo rather than local images

### Removed

* build.sh from the server as this was a useless file

## [v0.2.8](https://github.com/isu-avista/iot/releases/tag/v0.2.8) - 2021-02-11

### Added

### Changed
* Reverted server.py to the point that sensor sweep was added to it
* Updated app.py to reflect example_app.py from base-server

### Removed

## [0.2.7](https://github.com/isu-avista/iot/releases/tag/v0.2.7) - 2021-02-09

### Added
* Added `restart: always` to docker-compose.yml

### Changed
* Changed SensorSweep.run() to SensorSweep.start() inside server.py
* Switched avista modules in requirements.txt to use https instead of ssh

### Removed

## [0.2.6](https://github.com/isu-avista/iot/releases/tag/v0.2.6) - 2021-02-08

### Added

### Changed
* IoTServer._app has been updated to IoTServer.application to match base-server

### Removed

## [0.2.5](https://github.com/isu-avista/iot/releases/tag/v0.2.5) - 2021-02-08

### Added
* Added the options parameter to IoTServer's constructor for gunicorn options in app.py

### Changed

### Removed

## [0.2.4](https://github.com/isu-avista/iot/releases/tag/v0.2.4) - 2021-02-07

### Added

### Changed

### Removed
* The steps for including an ssh key to build docker images has been removed as the repositories are public

## [0.2.3](https://github.com/isu-avista/iot/releases/tag/v0.2.3) - 2021-02-07

### Added
* Added image options for docker-compose.yml to define the images to be pushed to dockerhub

### Changed

### Removed

## [0.2.2](https://github.com/isu-avista/iot/releases/tag/v0.2.2) - 2021-02-07

### Added

### Changed
* Both the frontend and backend services defined in docker-compose.yml are now using network_mode: host
* Replaced the ip addresses in flask.yml and paths.js with localhost, they no longer rely on a local ip address

### Removed

## [0.2.1](https://github.com/isu-avista/iot/releases/tag/v0.2.1) - 2021-02-06

### Added

### Changed
* Updated axios to 0.21.1 due to a security vulnerability 

### Removed

## [0.2.0](https://github.com/isu-avista/iot/releases/tag/v0.2.0) - 2021-02-06

### Added
* Added gunicorn options dictionary to app.py it is passed to IoTServer

### Changed
* Changed entrypoint in docker-compose from an explicit gunicorn call to running app.py
* SensorSweep is now started between the initialization, and the start of IoTServer

### Removed

## [0.1.6](https://github.com/isu-avista/iot/releases/tag/v0.1.6) - 2021-02-01

### Added

### Changed
* Updated some calls to ProcessorManager that weren't changed to SensorSweep
* Updated docker files and requirements to run properly on a raspberry pi
* Changed docker network mode to `host` so the client can be accessed from local network  
* Changed database connection string to postgres
* Updated the readme with installation instructions

### Removed

## [0.1.5](https://github.com/isu-avista/iot/releases/tag/v0.1.5) - 2021-01-11

### Added
- Added psycopg2-binary to server `requirements.txt` in preparation for switching to postgres

### Changed
- Fixed version numbers in documentation

### Removed

## [0.1.4](https://github.com/isu-avista/iot/releases/tag/v0.1.4) - 2021-01-03

### Added
* Incorporated process manager into IoTServer

### Changed
* Update get_data and get_data_since routes
* Sensor routes automatically update the list of processors in the process manager
* Fixed pinout duplication bug when updating a sensor
* Update profile view
* Moved all api paths within the client to paths.js and updated their references

### Removed

## [0.1.3](https://github.com/isu-avista/iot/releases/tag/v0.1.3) - 2020-12-15

### Added

### Changed
* Fixed setup_endpoints to actually call the super class
* Fixed sensor ui add sensor modal dialog to correctly add the module and class

### Removed

## [0.1.2](https://github.com/isu-avista/iot/releases/tag/v0.1.2) - 2020-12-15

### Added

### Changed
* removed redundant calls to init in order to improve function and testing

### Removed

## [0.1.0](https://github.com/isu-avista/iot/releases/tag/v0.1.0) - 2020-12-14

### Added
- Setup the initial project structure
- Added the server components to setup the server and configure it
- Added the server routes
- Added server authentication via jwt
- Added the client components
- Added client side authentication for all client routes and between client and server via jwt
- Added sphinx documentation to the project
- Added script to generate github page documentation for the code
- Updated the readme
- Documented the system
- Started testing all the python code (not yet complete)
- Have yet to start testing on the Client side
- Updated project to use the most recent versions of the following modules
  * avista-data
  * avista-base-server
  * avista-sensors

### Changed
- Nothing

### Removed
- Nothing
