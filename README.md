# Mock Code Challenge - Coffee Shop (Object Relationships) - Compulsory
## Instructions
This assessment is designed to evaluate your understanding of Object Oriented Programming using Python.
- You are required to complete the tasks outlined below within the specified time frame.
- Ensure your code adheres to Python syntax and best practices.
- Write comments to explain your code where necessary.
- Create a well-written README file providing instructions on repository setup and running the application in the terminal.
- Create a new PRIVATE repository, and push your solutions to it.

  ## More Instructions
  Create a new folder for your project:
  
1 Create the relevant subfolders and files needed to kickstart your project

2 Create a virtual environment

3 Activate the virtual environment and install the relevant dependencies

# 🚀 You are now good to go, Focus on the deliverables below 🚀


For this assignment, we'll be working with a Coffee shop-style domain.

We have three models: Coffee, Customer, and Order.

For our purposes, a Coffee has many Orders, a Customer has many Orders, and an Order belongs to a Customer and to a Coffee.

Coffee - Customer is a many-to-many relationship.

Note: You should draw your domain on paper or on a whiteboard before you start coding. Remember to identify a single source of truth for your data.

## Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- - Object Relationships
- lists and list Methods

# Deliverables
Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

## Initializers and Properties
### Customer
- Customer __init__(self, name)
 - Customer is initialized with a name
- Customer property name
 - Returns customer's name
 - Names must be of type str
 - Names must be between 1 and 15 characters, inclusive
 - Should be able to change after the customer is instantiated
   
## Coffee
- Coffee __init__(self, name)
 - Coffee is initialized with a name
- Coffee property name
  - Returns the coffee's name
  - Names must be of type str
  - Names length must be greater or equal to 3 characters
  - Should not be able to change after the coffee is instantiated
## Order
- Order __init__(self, customer, coffee, price)
  - Order is initialized with a Customer instance, a Coffee instance, and a price
-Order property price
  - Returns the price for the order
  - Prices must be of type float
  - Price must be a number between 1.0 and 10.0, inclusive
  - Should not be able to change after the order is instantiated
  - hint: hasattr()
# Object Relationship Methods and Properties
## Order
- Order property customer
  - Returns the customer object for that order
  - Must be of type Customer
- Order property coffee
  - Returns the coffee object for that order
  - Must be of type Coffee

## Coffee
- Coffee orders()
  - Returns a list of all orders for that coffee
  - Orders must be of type Order
- Coffee customers()
  - Returns a unique list of all customers who have ordered a particular coffee.
  - Customers must be of type Customer
  - 
## Customer
- Customer orders()
  - Returns a list of all orders for that customer
  - Orders must be of type Order
- Customer coffees()
  - Returns a unique list of all coffees a customer has ordered
  - Coffees must be of type Coffee
# Aggregate and Association Methods
## Customer
- Customer create_order(coffee, price)
  - Receives a coffee object and a price number as arguments
  - Creates and returns a new Order instance and associates it with that customer and the coffee object provided.
## Coffee
- Coffee num_orders()
  - Returns the total number of times a coffee has been ordered
  - Returns 0 if the coffee has never been ordered
- Coffee average_price()
  - Returns the average price for a coffee based on its orders
  - Returns 0 if the coffee has never been ordered
  - Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
  - 
# Bonus: Aggregate and Association Method
- Customer classmethod most_aficionado(coffee)
  - Receives a coffee object argument
  - Returns the Customer instance that has spent the most money on the coffee instance provided as argument.
  - Returns None if there are no customers for the coffee instance provided.
  - hint: will need a way to remember all Customer objects
  - Uncomment lines 137-147 in the customer_test file
 
# System Requirements
-A Browser that can run JavaScript (Chrome, Firefox, etc) -Node 20+ -operating system (Windows 10+, Linux, etc) -RAM > 4GB -Disk space > 1GB

## Installation
To use this repo, follow the following steps:

### Alternative one
open your terminal on your computer clone the repo by running the following command: git clone 

[Instructions to configure any settings or environment variables if necessary]

Execute the application:

bash Copy code

AUTHOR The project contributed to and maintained by:
Terry Otieno

