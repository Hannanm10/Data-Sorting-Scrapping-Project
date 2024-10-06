from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to the ChromeDriver executable
chrome_service_path = r'C:/Users/HANNAN/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

url1 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=monitors&_sacat=0&_pgn=0"
url2 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=lcd+monitor&_sacat=0&_pgn=0"
url3 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=pc&_sacat=0&_pgn=0"

# Initialize lists to store the extracted data from each monitors product listing
productNames = []       # To store the names of monitors
productConditions = []  # To store the conditions of monitors
productPrices = []      # To store the prices
shippingCost = []       # To store the shipping cost of each monitor
productLocation = []    # To store the location of each monitor
productSold = []        # To store number of sold monitors
productSeller = []      # To store seller of the product

# Global variables for counting products and pages
i = 1  # product counter
j = 1  # page counter

# Function for performing sorting
def DataScraping(url):
    
    # Declare i and j as global variables
    global i, j
    
    # Initialize the Chrome WebDriver with the path to the ChromeDriver executable
    chrome_service = Service(
        executable_path= chrome_service_path)
    browser = webdriver.Chrome(service=chrome_service)
    
    # Open Ebay
    browser.get(url)
    print(f"\n{browser.title}\n")
    
    time.sleep(2)
    
    # Use BeautifulSoup to parse the page source (HTML) for scraping    
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    try:
        # Infinite loop for scraping multiple pages until the last page is reached
        while True:
            
            print(f"\nPage {j}:\n")
            
            # Find all the product containers on the current page
            for data in soup.findAll('div', class_='s-item__info clearfix'):
                # Extract the name of the product
                name = data.find('div', class_='s-item__title')
                # Extract the condition of the product
                condition = data.find('span', class_='SECONDARY_INFO')
                # Extract the price
                price = data.find('span', class_='s-item__price')
                # Extract the shipping estimate
                shipping = data.find('span', class_='s-item__shipping s-item__logisticsCost')
                # Extract the location
                location = data.find('span', class_='s-item__location s-item__itemLocation')
                # Extract the number of sold items
                sold = data.find('span', class_='s-item__dynamic s-item__quantitySold')
                # Extract the seller of the product
                seller = data.find('span', class_='s-item__seller-info-text')

                # Append the extracted data to the corresponding lists, using 'N/A' if the data is missing
                productNames.append(name.text if name else 'N/A')
                productConditions.append(condition.text if condition else 'N/A')
                productPrices.append(price.text if price else 'N/A')
                shippingCost.append(shipping.text if shipping else 'N/A')
                productLocation.append(location.text if location else 'N/A')
                productSold.append(sold.text if sold else 'N/A')
                productSeller.append(seller.text if seller else 'N/A')
                
                
                print(f"{i} Product Scraped.")
                i += 1

            try:
                # Find the next page element from its class
                next_button = browser.find_element(By.CSS_SELECTOR, "a.pagination__next")
                # Storing the next page's url 
                next_page_url = next_button.get_attribute("href")
            
                # If there is no next page
                if not next_page_url:
                    print("No more pages.")
                    break
            
                # Go to the next page
                browser.get(next_page_url)
                time.sleep(2)
                soup = BeautifulSoup(browser.page_source, 'html.parser')
                j += 1
                
            except Exception as e:
                # If any exception occurs
                print("No more pages or error:", e)
                break
    finally:
        # Close the browser
        browser.quit()
        
DataScraping(url1)
DataScraping(url2)
DataScraping(url3)

# Create a DataFrame from the lists containing the scraped data
scraped_data = pd.DataFrame({
    'Name': productNames,
    'Condition': productConditions,
    'Price': productPrices,
    'Shipping Cost': shippingCost,
    'Location': productLocation,
    'Total Sold': productSold,
    'Seller': productSeller
})

# Save the DataFrame as a CSV file
scraped_data.to_csv('ScrapedEBAY.csv', index=False, encoding='utf-8')
print("Scraping completed, data saved.")