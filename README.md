# times_api
The API runs on a flask server.

## To Run the App:
<pre> python app.py</pre>

## The app will run on:
<pre>  http://localhost:8008/</pre>

## Required Libraries:
* **Flask** - This library is essential to create REST API in python. The library creates the REST API that returns the latest 5 stories on Times.com.
* **Re** - Regular expression for extracting title and link of the story.
* **Requests** - To get the HTML of the web page and convert it into string.

## Functions:
**main()**
<pre>   This function returns the main/ home page of the application showing the different routes available. </pre>

**get_time_stories() - **
<pre>   This function returns the json data containing the title and the link to the story on the webpage. </pre>

**extract_data() - **
<pre>   This function parses the HTML of the Times.com and looks for the most-popular-feed line by line and returns the data in a JSON format. </pre>
