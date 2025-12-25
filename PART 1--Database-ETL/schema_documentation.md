Relationship Description (Text Format)
ENTITY:- customers

Purpose:-
It contains personal details about each customer who deals with the company.

Characterization--
customer_id: A unique identifier for each customer. (Primary Key)
first_name: Customer’s first name.
last_name: Customer’s last name.
email: Customer’s email address for contact.
phone: The customer’s phone number.
city: City where the customer resides.
registration_date: Date of registration of the customer in the system.

Relationships: There can be many orders for one customer (M:1 relationship with the orders table). Customers can also be connected to the customer support issues or reviews based on the existing extensions of the system.



2.Normalization Explanation
The customers table is designed to be in Third Normal Form (3NF).
Functional Dependencies:
customer_id → first_name, last_name, email, phone, city, registration_date.
customer_id is PRIMARY KEY

WHY IT IS 3NF:--
1.The table is already in 1NF, as all attributes are atomic, with no repeating groups.
2.It satisfies 2NF as all the non-key attributes are fully functionally dependent on the primary key (customer_id), and there are no partial dependencies.
3.It is 3NF since all the attributes are not only dependent on the primary key but are also independent of each other, with no transitive dependencies. For example, the city depends on customer_id and not on email or first_name.

Anomaly Avoidance:
Update Anomaly: In cases where a consumer alters their contact number and/or email address, they have to be updated in only one row.
Insert Anomaly: It was also possible to insert a new customer without inserting an order.
Delete Anomaly: In delete anomaly, the deletion of orders does not delete the personal details of the customer because the orders are stored in a different table and are associated with a customer ID.


Explain how the design avoids update, insert, and delete anomalies--
Such an organizational design allows for consistent, efficient, and safe operations, since it eradicates redundancy and inconsistencies in the system’s databases.



3.Sample Data Representation---

Cleaned Customer Data:
 customer_id first_name last_name  ...          phone       city registration_date
0        C001      Rahul    Sharma  ...  +919876543210  Bangalore        2023-01-15
1        C002      Priya     Patel  ...  +919988776655     Mumbai        2023-02-20
2        C003       Amit     Kumar  ...  +919765432109      Delhi        2023-03-10
3        C004      Sneha     Reddy  ...  +919123456789  Hyderabad        2023-04-15
4        C005     Vikram     Singh  ...  +919988112233    Chennai        2023-05-22

Cleaned Product Data:
  product_id        product_name     category    price  stock_quantity
0       P001  Samsung Galaxy S21  Electronics  45999.0           150.0
1       P002  Nike Running Shoes      Fashion   3499.0            80.0
2       P003   Apple MacBook Pro  Electronics   2999.0            45.0
3       P004        Levi's Jeans      Fashion   2999.0           120.0
4       P005     Sony Headphones  Electronics   1999.0           200.0

Cleaned Product Data:
  product_id        product_name     category    price  stock_quantity
0       P001  Samsung Galaxy S21  Electronics  45999.0           150.0
1       P002  Nike Running Shoes      Fashion   3499.0            80.0
2       P003   Apple MacBook Pro  Electronics   2999.0            45.0
3       P004        Levi's Jeans      Fashion   2999.0           120.0
4       P005     Sony Headphones  Electronics   1999.0           200.0