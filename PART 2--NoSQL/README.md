Part 2: NoSQL Database Analysis – FlexiMart
____ Overview____

FlexiMart plans to expand its product catalog with highly diverse products.
This project analyzes whether MongoDB (NoSQL) is suitable for this requirement and demonstrates basic MongoDB operations using sample product data.

 Task 2.1: NoSQL Justification Report 

This section explains why MongoDB is more suitable than a traditional relational database for managing a flexible product catalog.

Section A: Limitations of RDBMS
Section B: NoSQL Benefits
Section C: Trade-offs

Task 2.2: MongoDB Implementation 
This section demonstrates basic MongoDB operations using a sample product catalog.


--> Provided Sample Data
The file products_catalog.json contains product data with different categories and attributes.
Example structure:
product_id
name
category
price
stock
specifications
reviews (array of review documents)

---> MongoDB Operations Implemented
All MongoDB operations are implemented in the file mongodb_operations.js.


Operation 1: Load Data 
Import the provided JSON file into the products collection.


Operation 2: Basic Query 
Retrieve all products from the Electronics category.
Filter products with price less than 50000.
Display only product name, price, and stock.


Operation 3: Review Analysis 
Calculate the average rating for each product.
Use aggregation to process the reviews array.
Display products with average rating greater than or equal to 4.0.


Operation 4: Update Operation 
Add a new review to the product with product ID ELEC001.
Store review details including user, rating, comment, and date.


Operation 5: Complex Aggregation 
Calculate the average price of products by category.
Display category name, average price, and product count.
Sort the results by average price in descending order.