# RateGain Blog Scraper
## Our Solution
1. Tools and Libraries:
- Utilized Python for scripting.
- Used the Requests library for HTTP requests.
- Employed Beautiful Soup for parsing HTML content.
- Chose Pandas for data processing 
2. Coding Approach:
- The code is written keeping pagination in mind
- Used Requests to fetch the HTML content of each page.
- Used Beautifulsoup to parse the HTML content.
- Extracted blog titles, dates, likes, image URLs, and  also extra field called blogUrl  is also extracted for the user to directly access the blog and cross check the data using it
- Implemented error handling for HTTP requests and parsing errors.
- The extracted data is stored in the user preferred format
- Implemented error handling mechanisms for various scenarios (HTTP errors, parsing errors, missing data).
3. Options for Data Storage:
- Provided multiple options to save the extracted data: CSV, Excel, JSON, HDF, SQL, or pickle formats.
- User can also choose if they want to keep the null values are not

## File Overview
This Python script `(main.py)` is designed to scrape data from a web source with customizable options for saving the scraped data. It provides flexibility in defining the save type, file name, number of pages to iterate, and handling null values during the scraping process.

## Usage
To run the script, execute the following command in your terminal:

`python main.py`

## Command-line Options
The script supports the following command-line options:

- -h, --help: Show help message and exit.
- -s SAVETYPE, --saveType SAVETYPE: Change save type for your data. Available save options include csv, json, sql, pickle. Default save type is csv.
- -f FILENAME, --fileName FILENAME: Change file name. Default is 'scraped_data.csv'.
- -p PAGES, --pages PAGES: Number of pages to iterate.
- -rn, --removeNull: Keep null values (if any) as None. Default is True.

## Examples
### Example 1: Changing Save Type and File Name
Save the scraped data as a JSON file with a custom file name:
`python main.py -s json -f custom_data.json`
### Example 2: Specifying Number of Pages to Scrape
Scrape data from 5 pages:
`python main.py -p 5`
### Example 3: Keeping Null Values as None
Scrape data while preserving null values:
`python main.py --removeNull False`

## How is our solution is different
1. Multiple save types: Users can choose the format in which they prefer to save the output , among the available format
2. Data verification: Using the blog link url , user can easily validate the data, instead of manually searching for it
3. Null Check: During data collection itself user can choose to discard Null types if any
4. Easy to set up: Being a python script , it’s easy to setup and run

## Requirements
- python3
- beautifulsoup4==4.12.2
- pandas==2.1.3
- requests==2.31.0
- SQLAlchemy==2.0.23

