from flask import Flask, jsonify, request
import requests
import re

app = Flask(__name__)

def extract_data():
    url = "https://time.com/"
    request_obj = requests.get(url)
    data = request_obj.text.splitlines()

    result = []
    titles = []
    links = []
    completed = False
    for i in range(len(data)):
        line = data[i].strip()
        if line == '<div class="most-popular-feed-wrapper">':
            curr_line = data[i].strip()
            while curr_line != '</div>':
                if '<h3 class="most-popular-feed__item-headline">' in curr_line:
                    curr_title = re.search(r'<h3 class="most-popular-feed__item-headline">(.*?)</', curr_line).group(1)
                    titles.append(curr_title)
                elif '<a href=' in curr_line:
                    curr_title_link = re.search(r'href=\"(.*?)\"', curr_line).group(1)
                    links.append(curr_title_link)
                i += 1
                curr_line = data[i].strip()
            completed = True
        if completed:
            break


    for i in range(5):
        curr_title = titles[i].encode('ascii', "ignore").decode()
        curr_title_link = links[i]
        temp_dict = {"title" : curr_title,
                    "link" : f"https://time.com{curr_title_link}"}
        result.append(temp_dict)

    return jsonify(result)

# Home Page
@app.route('/')
def main():
    return jsonify({'message' : 'Choose available routes.', 'routes': '/getTimeStories'})

# GET /getTimeStories
@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    return extract_data()

if __name__ == '__main__':
    app.run(host='localhost', port=8008, debug=True)