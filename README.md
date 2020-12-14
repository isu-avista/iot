# avista-iot

## Project Description

The IoT component of an energy management decision support tool.

## Table of Contents

1. [Installation](#Installation)
2. [Usage](#Usage)
3. [Contributing](#Contributing)
4. [Credits](#Credits)
5. [License](#License)

## Installation

TBD...

## Usage


### Client

#### Project Setup

```
npm install
```

#### Compiles and hot-reloads for development

```bash
cd client
npm run serve
```

#### Compiles and minifies for production

```
cd client
npm run build
```

#### Lints and fixes files

```
cd client
npm run lint
```

### Server

To start the server (at least for now) execute the following commands from the project root directory:

```bash
cd server
python3 app
```

This will start the server on localhost port 5000


#### Testing the REST Endpoints

```
curl --header "Content-Type: application/json" --request POST --data '{"email":"admin@isu.edu","password":"admin"}' http://localhost:5000/api/login
```

```bash
$ curl http://localhost:5000/protected
{
  "msg": "Missing Authorization Header"
}

$ curl -H "Content-Type: application/json" -X POST \
  -d '{"username":"test","password":"test"}' http://localhost:5000/login
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwianRpIjoiZjhmNDlmMjUtNTQ4OS00NmRjLTkyOWUtZTU2Y2QxOGZhNzRlIiwidXNlcl9jbGFpbXMiOnt9LCJuYmYiOjE0NzQ0NzQ3OTEsImlhdCI6MTQ3NDQ3NDc5MSwiaWRlbnRpdHkiOiJ0ZXN0IiwiZXhwIjoxNDc0NDc1NjkxLCJ0eXBlIjoiYWNjZXNzIn0.vCy0Sec61i9prcGIRRCbG8e9NV6_wFH2ICFgUGCLKpc"
}

$ export ACCESS="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwianRpIjoiZjhmNDlmMjUtNTQ4OS00NmRjLTkyOWUtZTU2Y2QxOGZhNzRlIiwidXNlcl9jbGFpbXMiOnt9LCJuYmYiOjE0NzQ0NzQ3OTEsImlhdCI6MTQ3NDQ3NDc5MSwiaWRlbnRpdHkiOiJ0ZXN0IiwiZXhwIjoxNDc0NDc1NjkxLCJ0eXBlIjoiYWNjZXNzIn0.vCy0Sec61i9prcGIRRCbG8e9NV6_wFH2ICFgUGCLKpc"

$ curl -H "Authorization: Bearer $ACCESS" http://localhost:5000/protected
{
  "logged_in_as": "test"
}
```

## Configuration

### Server

#### Generating secret keys

```bash
python3 -c "import uuid; print(uuid.uuid4().hex)"
```

## Contributing

This is a private project supported by a grant from Avista Corporation. If you wish to work on this project, please contact either:

* [Dr. Paul Bodily](mailto:bodipaul@isu.edu), or
* [Isaac Griffith](mailto:grifisaa@isu.edu)

## Credits

This module was contributed to by:

* Isaac D. Griffith
* Andrew Christiansen


## License

Copyright (c) 2020 Idaho State University Empirical Software Engineering Laboratory

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
