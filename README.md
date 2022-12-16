
# products_backend_api

## Overview of API

This ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) API utilizes calls to a ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) database. It was the first project for an API after learning how to create them. The API has full CRUD functionality of products and reviews on those products(which was a bonus objective for this project).


## Get All Products

This endpoint returns a Response that has all the products objects.

	GET /

		--request GET
		--url http://127.0.0.1:8000/api/products/


## Get Product by ID

This endpoint returns a Response that is one product object. This will be 


| Parameter | Datatype | Description |
|	------------| -----------------| -------------|
|	id 		| 	int		|	The object which has the primary key of the entered ID |

	GET /{id}
		--request GET
		--url http://127.0.0.1:8000/api/products/id/



## Post Product

This endpoint returns a Response 201 created on a successful POST

	POST /
		--request POST
		--url http://127.0.0.1:8000/api/products/
	
	Body
		title string
		The name of the product, for example: 'HDMI Cord'


		description string
		A brief description of the product, for example: "HDMI tot HDMI cable"

		price float
		The USD cost of the product, for example: 17.95

		inventory_quantity int
		The amount of the product in stock, for example: 10

	JSON

		{
			"title": "HDMI Cord",
			"description": "HDMI to HDMI cable",
			"price": 17.99,
			"inventory_quantity": 10
		}


## Update Product

This endpoint changes a specific objects attribute fields.

| Parameter | Datatype | Description |
|	------------| -----------------| -------------|
|	id 		| 	int		|	The object which has the primary key of the entered ID |
	
	PUT /{id}
		--request PUT
		--url http://127.0.0.1:8000/api/products/id/
		

	Body
		title string
		The name of the product, for example: 'HDMI Cord'


		description string
		A brief description of the product, for example: "HDMI tot HDMI cable"

		price float
		The USD cost of the product, for example: 17.95

		inventory_quantity int
		The amount of the product in stock, for example: 10

	JSON
		{
			"title": "HDMI Cord",
			"description": "8ft HDMI to HDMI cable",
			"price": 20.00,
			"inventory_quantity": 6
		}

## Delete Product

This endpoint removes an object from the database and responds with a 204 NO CONTENT code


| Parameter | Datatype | Description |
|	------------| -----------------| -------------|
|	id 		| 	int		|	The object which has the primary key of the entered ID |
	
	DELETE /{id}
		--request DELETE
		--url http://127.0.0.1:8000/api/products/id/


## Installation Steps

- Create a new mySQL connection
- Run: CREATE DATABASE
- Download the zip file from GitHUb
- Open the unzipped folder in your IDE of choice, I use VSCode
- Run: pipenv install
- Run: pipenv shell
- Select the virutal envionmnet in the Python: Select Interpreter
- Create a local settings file
- Add a SECRET_KEY and DATABASES section
- Fill out the information for the database connection like name and password
- Assuming your database is set up, you should now be able to migrate
- I used and recommend Postman for the API calls



## Contact Me

See more of my repositories [here!](https://github.com/WallochMatt?tab=repositories)

Message me on [LinkedIn!](https://www.linkedin.com/in/matthew-walloch-931409250/)

Or shoot me an email!: matthewrwalloch@gmail.com



## User Stories

For those interested, below is the user stories for this project

A 'Products API backend', executable through Postman

As a developer, I want to make good, consistent commits.

As a developer, I want to create an Entity Relationship Diagram that will accurately show the necessary properties on the Product model

As a developer, I want to create a Product model
Property names must be in snake_case and match the following exactly!
	title - CharField
	description - CharField
	price - DecimalField
	inventory_quantity - IntegerField
 
As a developer, I want my API to serve content on the following url paths:
Paths must match these exactly!
	‘127.0.0.1:8000/api/products/' 
	‘127.0.0.1:8000/api/products/<int:pk>/’ 

As a developer, I want to build a REST web API in Django REST Framework, so that I can make HTTP requests interact with the data set.

As a developer, I want to create a GET endpoint that responds with a 200 success status code and all of the products within the Product table.

As a developer, I want to create a GET by id endpoint that does the following things: 
	Accepts a value from the request’s URL (The id of the product to retrieve).
	Returns a 200 status code. (Explicitly return this, not just allow it to default)
	Responds with the product in the database that has the id that was sent through the URL. 

As a developer, I want to create a POST endpoint that does the following things: 
	Accepts a body object from the request in the form of a Product model. 
	Adds the new product to the database. 
	Returns a 201 status code. 
	Responds with the newly created product object.

As a developer, I want to create a PUT endpoint that does the following things: 
	Accepts a value from the request’s URL (The id of the product to be updated). 
	Accepts a body object from the request in the form of a Product model. 
	Finds the product in the Product table and updates that product with the properties that were sent in the request’s body. 
	Returns a 200 status code.  (Explicitly return this, not just allow it to default)
	Responds with the newly updated product object. 

As a developer,  I want to create a DELETE endpoint that does the following things: 
	Accepts a value from the request’s URL. 
	Deletes the Product from the database.
	Returns a 204 status code (NO CONTENT).
 
I want to use Postman to make a POST, PUT, DELETE, and both GET requests (get by id and get all) request to my REST web API, save it to a collection, and then export it as a JSON from Postman.