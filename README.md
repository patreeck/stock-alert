**Stock News Notifier**
This Python project is a stock market monitoring tool that retrieves daily stock data and relevant news articles for a specified company. It sends SMS notifications via Twilio when significant changes occur in the stock prices.



**Key Features**


**Stock Data Analysis:** The program fetches daily stock data for a chosen company (e.g., Tesla Inc) from Alpha Vantage API.

**Stock Price Change Monitoring:** It calculates the percentage change in stock prices between consecutive days to determine market trends.

**News Article Retrieval:** Utilizing the News API, it fetches news articles related to the specified company for market context.

**Twilio SMS Notification:** Sends concise SMS notifications containing stock information and headlines using Twilio API for immediate updates.


**Technologies Used**

**Python:** Developed entirely in Python, utilizing its extensive libraries for web requests, data processing, and datetime manipulation.

**Requests Library:** Utilized to make HTTP requests to Alpha Vantage and News API endpoints for data retrieval.

**Twilio API**: Integrated for sending SMS notifications to designated phone numbers when specific stock conditions are met.

**Datetime Module:** Employed for managing date and time calculations to retrieve the required stock data for analysis.

**JSON Parsing:** Parses JSON responses from API requests to extract relevant stock and news information.

**Error Handling:** Implements robust error handling to manage potential exceptions during API interactions.



**Prerequisites**

To use this application, ensure you have the following:

**Python 3.x:** Make sure Python is installed on your local machine.

**Twilio Account:** Sign up for a Twilio account to obtain authentication credentials and a registered phone number for sending SMS.

**Alpha Vantage API Key:** Register for an Alpha Vantage API key to access stock market data.

**News API Key:** Obtain an API key from the News API to retrieve relevant news articles.



**Setup and Configuration**

Clone or download the repository to your local machine.

Install the required Python packages using pip install -r requirements.txt.

Replace placeholder values (account_sid, auth_token, api_key_stock, api_key_news, STOCK) in the main.py script with your actual credentials and preferred stock symbol.

Customize the percentage threshold (5% by default) in the script to trigger news alerts based on your desired criteria.

Run the main.py script to start monitoring the specified stock and receive SMS notifications for significant price changes.

**Usage**

Execute main.py to initiate the stock monitoring process.

The program will retrieve the latest stock data and news articles.

Depending on the percentage change in stock prices compared to the previous day, SMS notifications will be sent via Twilio to keep you informed.

Adjust the threshold percentage in the script to receive notifications for changes that meet your investment criteria.

