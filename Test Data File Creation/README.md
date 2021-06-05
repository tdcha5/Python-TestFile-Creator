# Overview
This project was created for a few reasons to save time on some of my 

# Initial Requirements 
- Generate a list of first and last names
- Create first, last, and phone objects that I could reuse for accessibility. 
- Generate a random email 
- Create a function that will return the number of requested talents and save the talents to a CSV that can be used during testing.
- Update a file for each test to track the number of times the script is being used and which days for any metrics if requested

# Impacts to testing
- Either manually entering this test data or manually creating this file for EACH test is time-consuming and draining. 
- By automating this task, I can focus more on other aspects of the test such as data validation, email validation, troubleshooting, bug tracking, requirements review/analysis, etc. 
- Not all manual tasks need to be done each time. 
- This script also makes boundary testing easy. If I want to know how the system responds to upload 50, or 100 talent, it takes only a second to run that script vs. possibly minutes of lost time.
- Why the number of talent? Given some limitations of the data store querying, it's easier to track down anomalies by having more unique test data. 
-- Although each test has unique ids, having unique names or emails, helps track down issues faster via the UI as well as integrated systems.
-- If all I have dozens of test data named "test" that's much harder to track down

# Future enhancements
- Add checks to make sure script changes don't cause regression. 
- Use this as a template to automate some of my troubleshooting tasks by pulling data from APIs and reporting back information.
- Review (or have the script reviewed) for opportunities to clean the code 