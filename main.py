import argparse

# import pytables
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

URL = "https://rategain.com/blog/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

SAVE_TYPE_LIST = ["csv", "json", "sql", "pickle"]
SAVE_TYPE = "csv"
FILE_NAME = "data"
PAGES = None
KEEP_NULL = True

argParser = argparse.ArgumentParser()
argParser.add_argument(
    "-s",
    "--saveType",
    type=str,
    help=f"Change save type for your data. Available save options {SAVE_TYPE_LIST} . Default is csv",
)
argParser.add_argument(
    "-f",
    "--fileName",
    type=str,
    help="Change file name. Default is 'scraped_data.csv'",
)
argParser.add_argument("-p", "--pages", type=int, help="Number of pages to iterate.")
argParser.add_argument(
    "-rn",
    "--removeNull",
    action="store_true",
    help="Keep null values(if any) as None. Default is True",
)


def parseHTML():
    """Method to parse data from website"""
    global URL, HEADERS
    c = PAGES
    current_url = URL
    data = []
    try:
        while current_url:
            print("\nGetting data from page: " + current_url)
            if c != None:
                c -= 1
            response = requests.get(current_url, headers=HEADERS)
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.content, "html.parser")
                wrap_divs = soup.find_all(class_="wrap")
                for wrap in wrap_divs:
                    item = {}
                    titles = wrap.select(".content h6 a")[0]
                    date = wrap.select(".blog-detail .bd-item:first-child  span")[0]
                    imgUrl = wrap.select(".img a")
                    likes = wrap.select(".content .zilla-likes span")[0]

                    item["title"] = titles.text if titles.text else None
                    item["blogUrl"] = titles.get("href") if titles.get("href") else None
                    item["date"] = date.text if date.text else None
                    item["imgUrl"] = (
                        imgUrl[0].get("href") if imgUrl and len(imgUrl) > 0 else None
                    )
                    item["likes"] = (
                        likes.text.split(" ")[0]
                        if likes and len(likes.text.split(" ")[0]) > 0
                        else None
                    )
                    data.append(item)

                next_page_link = soup.select_one(".next.page-numbers")
                if next_page_link:
                    current_url = next_page_link.get("href")
                else:
                    break
                if c == 0:
                    break
            else:
                print(
                    f"Failed to fetch the content for URL {current_url}. Status code: ",
                    response.status_code,
                )
                break
    except Exception as e:
        exit(f"ERROR {e}", e.with_traceback())

    saveToFile(data=data)


def saveToFile(data):
    """Method to save data to file"""
    if len(data) == 0:
        exit("No Data to save to file")
    df = pd.DataFrame(data=data)
    if not KEEP_NULL:
        df = df.dropna()
    file_name = FILE_NAME + "." + SAVE_TYPE

    if SAVE_TYPE == "csv":
        df.to_csv(file_name)
    if SAVE_TYPE == "json":
        df.to_json(file_name)
    if SAVE_TYPE == "hdf":
        df.to_hdf(file_name, key="df", mode="w")
    if SAVE_TYPE == "sql":
        engine = create_engine("sqlite://", echo=False, if_exists="replace")
        df.to_sql(file_name, con=engine)
    if SAVE_TYPE == "pickle":
        df.to_pickle(file_name)

    exit(f"File saved sucessfully to: {file_name}")


def main():
    global SAVE_TYPE, PAGES, FILE_NAME, KEEP_NULL
    args = argParser.parse_args()

    if args.saveType:
        SAVE_TYPE = str(args.saveType)
        if SAVE_TYPE not in SAVE_TYPE_LIST:
            exit(f"\nPlease select file save type from {SAVE_TYPE_LIST}")

    if args.fileName:
        FILE_NAME = str(args.fileName).strip()
        print(f"\nSave File Name: {FILE_NAME}")

    if args.pages:
        PAGES = int(args.pages)
        print(f"\nIterate till page count: {PAGES}")

    if args.removeNull:
        KEEP_NULL = True
        print(f"\nRemoving Null values: {KEEP_NULL}")

    print(f"\nData Save Type: {SAVE_TYPE}")
    parseHTML()


main()
