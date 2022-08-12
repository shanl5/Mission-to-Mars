# 1) use Flask to render a template, redirect to another url, create a URL
# 2) Use PyMongo to interact with a Mongo database
# 3) to use scraping code, will convert from Jupyter notebook to Python
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# tell Python how to connect to Mongo using PyMongo
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set Up App Routes
# one for main HTML page everyone will view when visiting web app;
# and one to actually scrape new data using code

# First, the route for the HTML page
# the index() function is what links visual representation of web app,
# to the code
# to create later: the returned HTML template using an index.html file
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Next, the scraping route
# this will be the "button" of the web app clicked on homepage,
# will scrape updated data
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

# tell Flask to run
if __name__ == "__main__":
    app.run()