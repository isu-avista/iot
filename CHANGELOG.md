# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

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
