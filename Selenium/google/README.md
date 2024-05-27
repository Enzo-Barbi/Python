## Overview

This repository contains a simple Flask API that retrieves data based on given parameters. 

## Requirements

- Python 3.11
- Flask
- Selenium

## Running the Application
To run the Flask application, execute:

```bash
python3.11 app.py

```

## Endpoints
POST /google
This endpoint retrieves data based on the provided JSON payload.

### Request
Method: POST
URL: http://127.0.0.1:5000/google
Body:
```json
[
  {
    "values": ["python"],
    "attribute": "linguagem",
    "operator": "equal"
  },
  {
    "values": ["Enzo Barbi"],
    "attribute": "nome",
    "operator": "equal"
  }
]
```
Response
Success: 200 OK
Content: JSON data based on the provided parameters
   
# Testing with Postman
1 -Open Postman.
2 - Create a new POST request.
3 - Set the request URL to http://127.0.0.1:5000/google.
4 - Click on the 'Body' tab, select 'raw', and then set the format to 'JSON'.
5 - Paste the JSON into the body:
6 - Click 'Send' to execute the request.

