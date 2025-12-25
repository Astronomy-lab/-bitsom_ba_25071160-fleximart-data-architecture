# etl_pipeline.py
# -----------------------------
# Import libraries
# -----------------------------
import pandas as pd
import numpy as np
import phonenumbers

# -----------------------------
# Function to Read CSV file
# -----------------------------
def read_raw_data(file_path):
    df = pd.read_csv(file_path)
    return df

# ---------------------------------
# Function to handle misssing values
# ---------------------------------
def handle_missing_val(df):
    missing_col = []
    for col in df.columns:
        missing = df[col].isna().sum()
        if missing > 0:
            missing_col.append(col+ "has" + str(missing) + "missing values")
            if df[col].dtype in ["int64", "float64"]:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
    return df, missing_col


# =================================================
# CUSTOMER DATA CLEANING
# =================================================
print("\n---- CUSTOMERs DATA ----")
cust_file = r"C:\Users\Lenovo\OneDrive\Documents\GitHub\customers_raw.csv"
df = read_raw_data(cust_file)
print(" Data Info")
df.info()

# Handle missing values
df, missing_report = handle_missing_val(df)

print("\nMissing Values Report:")
print(missing_report)

# Remove duplicate rows
df = df.drop_duplicates()

# Registration_date column
if "registration_date" in df.columns:

    df["registration_date"] = df["registration_date"].astype(str)
    df["registration_date"] = df["registration_date"].str.strip()

    df["registration_date"] = pd.to_datetime(
        df["registration_date"],
        format="mixed",
        errors="coerce"
    )

    df["registration_date"] = df["registration_date"].dt.strftime("%Y-%m-%d")


# Phone colmn
if "phone" in df.columns:

    phone_list = []

    for num in df["phone"]:
        try:
            phone = phonenumbers.parse(str(num), "IN")
            phone = phonenumbers.format_number(
                phone, phonenumbers.PhoneNumberFormat.E164
            )
            phone_list.append(phone)
        except:
            phone_list.append(np.nan)
    df["phone"] = phone_list


# Capitalize text columns
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str).str.title()


print("\nCleaned Customer Data:")
print(df.head())
print("Final Shape:", df.shape)


# =================================================
# PRODUCT DATA CLEANING
# =================================================
print("\n---- PRODUCTS DATA ----")
# Product file path
prod_file = r"C:\Users\Lenovo\OneDrive\Documents\GitHub\Product_raw.csv"

# Read product data
prod_df = read_raw_data(prod_file)

# Handle missing values
clean_prod_df, missing_prod_col = handle_missing_val(prod_df)
print("\nMissing Values Report:")
print(missing_prod_col)

# Remove duplicate rows
clean_prod_df = clean_prod_df.drop_duplicates()

# category column 
if "category" in clean_prod_df.columns:
    clean_prod_df["category"] = clean_prod_df["category"].astype(str).str.title()

print("\nCleaned Product Data:")
print(clean_prod_df.head())
print("Final Shape:", clean_prod_df.shape)


# =================================================
# SALES DATA CLEANING
# =================================================
print("\n----- SALES DATA ----")

# Sales file path
sales_file = r"C:\Users\Lenovo\OneDrive\Documents\GitHub\sales_raw.csv"

# Read sales data
sales_df = read_raw_data(sales_file)
print("Original Sales Shape:", sales_df.shape)

# Handle missing values
clean_sales_df, missing_sales_col = handle_missing_val(sales_df)
print("\nMissing Values Report:")
print(missing_sales_col)

# Remove duplicates data
clean_sales_df = clean_sales_df.drop_duplicates().copy()
print("After removing duplicates:", clean_sales_df.shape)

#  transaction_date column
if "transaction_date" in clean_sales_df.columns:
    clean_sales_df["transaction_date"] = clean_sales_df["transaction_date"].astype(str)
    clean_sales_df["transaction_date"] = clean_sales_df["transaction_date"].str.strip()
    clean_sales_df["transaction_date"] = pd.to_datetime(
        clean_sales_df["transaction_date"],
        format="mixed",
        errors="coerce"
    )
    clean_sales_df["transaction_date"] = clean_sales_df["transaction_date"].dt.strftime("%Y-%m-%d")

# Now final cleaned sales data
print("\nCleaned Sales Data:")
print(clean_sales_df.head())
print("Final Sales Shape:", clean_sales_df.shape)