# Noted-FastAPI


## How to run the code
- Create a ```DATABASE_URL``` variable in a ```.env``` file. This must be a Postgresql database URI.
- Install all project requirements from the ```requirements.txt``` file using ```pip install -r requirements.txt```
- Create the database by running ``` python create_db ```
- Finally run your server with ```uvicorn main:app``

## Run the Application
-Run the FastAPI application using uvicorn:


-uvicorn main:app --reload
-This will start the application and provide interactive documentation at http://127.0.0.1:8000/docs.`


