
Event Planner CRUD API
This is a simple Flask-based CRUD API for managing venue information in an event planner application. It allows users to perform basic operations such as adding, retrieving, updating, and deleting venue records.

----->Requirements
To run this application, you need to have the following:

*Python
*Flask
*Flask-MySQLdb
*MySQL Server


----->Installation

Clone the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Configure the MySQL connection settings in the api.py file.
Create a MySQL database named mydb.
Run the Flask application using the command python api.py.
The API will be accessible at http://localhost:5000/.


----->Endpoints

The API provides the following endpoints:
GET /: Displays the available operations.
POST /add: Adds a new venue record.
GET /retrieve: Retrieves all venue records.
GET /retrieve/<id>: Retrieves a specific venue record by ID.
PUT /update/<id>: Updates a specific venue record by ID.
DELETE /delete/<id>: Deletes a specific venue record by ID.
The responses can be returned in either JSON or XML format by specifying the format query parameter.

Usage
You can interact with the API using the provided command-line interface (CLI) script api_cli.bat. It allows you to easily perform operations by entering the required inputs.

Run the api_cli.bat script.
Follow the instructions in the CLI to perform various CRUD operations.
You can choose to retrieve the data in either JSON or XML format.