import json
import datetime
from pymongo import MongoClient
import pandas as pd

#  Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

#  Select database and collection
db = client["fleximart"]
col = db["products_catalog"]


# Query-->Basic Query
#  // Find all products in "Electronics" category with price less than 50000
# // Return only: name, price, stock
print("All products in \"Electronics\" category with price less than 50000")

q2 = col.find(
    {
        "category": "Electronics",
        "price": {"$lt": 50000}
    },
    {
        "_id": 0,
        "name": 1,
        "price": 1,
        "stock": 1
    }
)

#  Convert result to pandas DataFrame (table)
df = pd.DataFrame(list(q2))
#  Display table
print(df)




# Query -->Review Analysis
# // Find all products that have average rating >= 4.0
# // Use aggregation to calculate average from reviews array
print("Products with average rating >= 4.0")
pipeline3 = [
    {
        # Calculate average rating safely
        "$addFields": {
            "avg_rating": {
                "$avg": {
                    "$ifNull": ["$reviews.rating", []]
                }
            }
        }
    },
    {
        # Filter products with avg rating >= 4.0
        "$match": {
            "avg_rating": {"$gte": 4.0}
        }
    },
    {
        # Select required fields
        "$project": {
            "_id": 0,
            "product_id": 1,
            "name": 1,
            "category": 1,
            "avg_rating": {"$round": ["$avg_rating", 2]}
        }
    }
]

#  Run aggregation and convert to table
df = pd.DataFrame(list(col.aggregate(pipeline3)))
#  Display Table
print(df) 



# Query-->Update Operation  
# // Add a new review to product "ELEC001"
# // Review: {user: "U999", rating: 4, comment: "Good value", date: ISODate()}
print("Adding new review to product ELEC001")
new_review = {
    "user": "U999",
    "rating": 4,
    "comment": "Good value",
    "date": datetime.datetime.now()  # stored as BSON Date (ISODate)
}
#  Add review to product ELEC001
result = col.update_one(
    {"product_id": "ELEC001"},
    {"$push": {"reviews": new_review}}
)
#  Check update status
print("Matched:", result.matched_count)
print("Modified:", result.modified_count)




# Query-->Complex Aggregation 
# // Calculate average price by category
#// Return: category, avg_price, product_count
#// Sort by avg_price descending

print("Average price by category")
pipeline5 = [
    {
        # Group by category
        "$group": {
            "_id": "$category",
            "avg_price": {"$avg": "$price"},
            "product_count": {"$sum": 1}
        }
    },
    {
        # Format output
        "$project": {
            "_id": 0,
            "category": "$_id",
            "avg_price": {"$round": ["$avg_price", 2]},
            "product_count": 1
        }
    },
    {
        # Sort by average price (high to low)
        "$sort": {"avg_price": -1}
    }
]

#  Run aggregation and convert to table
df = pd.DataFrame(list(col.aggregate(pipeline5)))
#  Display table
print(df)