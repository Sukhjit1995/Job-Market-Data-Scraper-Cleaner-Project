**Job Market Data Analysis – UK Data Analyst Roles**
Project Overview

This project extracts live job listing data from the Adzuna API for Data Analyst roles in the UK and transforms it into a structured, analysis-ready dataset.

The objective was to simulate a real-world data workflow: retrieving raw JSON data from an external API, cleaning and validating the dataset, and producing a reliable CSV file suitable for further analysis or reporting in tools such as Excel or Power BI.

The project focuses on data quality, validation, and reproducibility rather than just visualisation.

Technologies Used:

- Python

- Pandas

- Requests

- Python-dotenv

- JSON

- Adzuna Job Search API

**Data Pipeline Overview**
1. **Data Extraction**

- Connected to the Adzuna API using secure environment variables.

- Retrieved job listings filtered by: Keyword: "data analyst"
                                     Location: London (UK)

- Saved the raw API response as raw_jobs.json.

- Implemented basic error handling for API response status.

2. **Data Transformation**

- Loaded raw JSON into Python.

- Used pandas.json_normalize() to flatten nested structures.

- Selected relevant fields:

- Job Title

- Location

- Salary (min, max)

- Company

- Date Posted

- Calculated average salary from minimum and maximum salary.

3. **Data Cleaning & Validation**

- The dataset was cleaned to ensure reliability and consistency:

- Removed rows where salary values were zero or invalid.

- Ensured minimum salary was not greater than maximum salary.

- Converted salary fields to numeric types.

- Converted date field to datetime format.

- Handled missing company values.

- Removed duplicate job listings.

- Standardised location data and extracted region.

- Removed unrealistic salary outliers using statistical filtering.

- Implemented validation checks using assertions to ensure:

- No negative salaries

- No unrealistic salary ranges



**A cleaned dataset was exported as cleaned_jobs.csv.**

Key Data Quality Considerations:

- Raw data was preserved separately from cleaned data.

- Environment variables were used to protect API credentials.

- Folder creation was automated to ensure reproducibility.

- Missing value analysis was performed prior to cleaning.

- Validation rules were applied before final export.

Here is the project being run in Pycharm:
<img width="1572" height="1355" alt="image" src="https://github.com/user-attachments/assets/e4d047cb-d281-4b3b-a89b-808eb91a7f06" />

And the end product in Excel: 
<img width="2118" height="920" alt="image" src="https://github.com/user-attachments/assets/26e11b1f-0ec8-4304-8ca1-dd8b6347514b" />




