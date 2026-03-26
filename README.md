# Real Estate Data Pipeline: Cleaning, Transformation, and Loading with Python & MySQL
Project Overview

This project consists of building an end-to-end data pipeline to process raw real estate data (flats dataset). The pipeline ingests messy data from a CSV file, performs data cleaning and standardization, and loads the final structured dataset into a MySQL database for further analysis.

The goal of this project is to simulate a real-world data engineering workflow, focusing on data quality, transformation logic, and pipeline design.

#Techonologies applied
Python(Pandas,Numpy)
MySQL

#Pipeline Architecture

The pipeline follows a structured ETL (Extract, Transform, Load) approach:

#Extract
Load raw CSV data using pandas
Handle encoding and parsing issues
#Transform
Clean and standardize numerical fields (area, price)
Handle missing and inconsistent values
Normalize price units (Lac, Cr) into a single scale
#Create derived columns:
clean_square_feet
price_to_cr
price_absolute
price_per_sqft_cleaned
#Load
Store the cleaned dataset into a MySQL table
Ensure the dataset is structured and ready for analysis.

#Data Cleaning & Transformation

The dataset contained several real-world data quality issues, which were addressed in this pipeline:

#Inconsistent formats: Extracted numeric values from text fields (e.g., "1200 sqft" → 1200)
#Mixed units in price: Standardized values from different units such as Lac and Crore
#Missing values: Handled nulls appropriately depending on the importance of the column
#Unstructured text fields: Ignored or excluded non-analytical columns (those one with long descriptions)
Data Cleaning & Transformation
#Unit normalization: Converted all price values into a consistent unit (Crores) and also into absolute numeric values
#Derived metrics: Calculated price_per_sqft_cleaned using standardized values for accurate analysis.
Final Dataset

#The final dataset includes only relevant and structured columns:

property_name
clean_square_feet
price_to_cr
price_absolute
price_per_sqft_cleaned
status
facing

This dataset is optimized for analytical use and can be easily consumed by analysts or downstream systems.

#Author

Ginna Ospino
Industrial Engineer | Data Enthusiast | Aspiring Data Engineer

