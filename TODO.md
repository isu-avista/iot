# Things todo to improve the project

## Server Side

* Testing of all routes needs to be completed (though some are complete)
* Need to integrate the use of the avista-sensor sensor processor manager into the process (this should be done in the start() and stop() methods of IoTServer)
* When a new sensor is added it needs to inform the SensorProcessorManager of the event, so that the new sensor can be added (similar approaches for sensor updates and removals)
* Sensor data methods need to be attached to a route
* API Keys is not right, and probably will need to be removed (but not quite yet)
* Need to shift from sqlite to mariadb or mysql
* Need to begin the process of defining deployment
* Need to get travis ci running
* Tests should be at 100% Unit Coverage
* Need to integration test
* Need to component test
* Need to define a process by which old data (that which has already been sent to the portal (and confirmed)) is deleted from the database (to save space)
* Need a method to allow the portal to connect and update server information and set users (other than admin). Thus, it needs to have admin capabilities on the IoT device
* Need to shift Status data from static to dynamic, thus we need a means to gain the following information:
  - Internet connectivity status
  - RPi Power status
  - Sensor connectivity status
  - Server (portal) connectivity status

## Client Side

* The whole thing needs to be tested
* I don't quite like the Profile page at this time, it needs to be improved (and a design needs to be created)
* I would like a different chart (probably a streaming one)
* Sensors Configuration
  - There is a weird bug with the Edit/Add panel for Pins for some reason it is not correctly dealing with the data, I am sure that this can be easily remedied
* Need to add in the capability to update changes to db and system configuration
  - Need to provide default fields for SQLite, MariaDB, PostgreSQL, and MySQL at a minimum (should not be too difficult) and we need to use a dropdown for setting that config in the edit dialog.

