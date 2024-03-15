For day 96 of the 100 Days of Code course, the goal was to create a custom API based website. For this project, since I live relatively close to ski and snow resorts, I decided to create an application that pulls weather data from Open Weather Map and displays that weather information on a website.

The program first connects to the Open Weather Map 5 Day Forecast endpoint and collects weather data for the specified coordinates. Since I live close to Lake Tahoe, I passed six ski and snow resorts from the Lake Tahoe area through the endpoint to pull their weather information.

The information I found useful was was used to populate dictionaries for each resort. Those ski and snow resorts were then added to a list composed of each snow resort with the information desired.

To properly generate the tables for the Flask website, a seperate function, generate_tables, was used to create lists formatted so that each list entry lined up with the appropriate row being rendered.

Most of the work used to create this website was performed in the weatherdata.py file. The webpages.py file is used to launch the web application and display the web pages. The home page lists each snow resort that was was passed through the Open Weather Map API. When a snow resort is selected, the five day weather information that is passed from weatherdata.py is displayed along with a link to the resports website.
