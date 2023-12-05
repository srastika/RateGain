# RateGain Scraper

## Overview
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

## Requirements
- python3
- beautifulsoup4==4.12.2
- pandas==2.1.3
- requests==2.31.0
- SQLAlchemy==2.0.23

