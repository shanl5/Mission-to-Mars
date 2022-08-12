# Import Splinter and BeautifulSoup
# ?? from urllib.parse import _NetlocResultMixinStr
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Import Pandas for 10.3.5
import pandas as pd

# Import datetime for 10.5.3
import datetime as dt

    #.# This code below into function `scrape_all`
    # # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

# New code for file: function `scrape_all()` to:
# 1. Initialize the browser.
# 2. Create a data dictionary.
# 3. End the WebDriver and return the scraped data.
def scrape_all():
    # Initiate **headless** driver for deployment
    # headless=False ==> can see "scraping in action"
    # headless=True ==> turns off view of script working
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Set the news title and paragraph variables to the return of the two
    # from the `mars_news()` function`
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

    #.# This code below into a function called mars_news()
    #.# the function adds try/except error handling
    # # Visit the mars nasa news site
    # url = 'https://redplanetscience.com'
    # browser.visit(url)
    # # Optional delay for loading the page; and search for combo of (`div`) and attribute (`list_text`)
    # # e.g., `ul.item_list` would be found in HTML as `<ul class="item_list">`; wait_time in seconds.
    # browser.is_element_present_by_css('div.list_text', wait_time=1)

    # # Convert the browser html to a soup object and then quit the browser
    # html = browser.html
    # news_soup = soup(html, 'html.parser')

    # # CSS works from right to left, returning last item on list instead of the first.
    # slide_elem = news_soup.select_one('div.list_text')

    # slide_elem.find('div', class_='content_title')

    # # Use the parent element to find the first `a` tag and save it as `news_title`
    # news_title = slide_elem.find('div', class_='content_title').get_text()
    # news_title

    # # Use the parent element to find the paragraph text
    # news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # news_p

def mars_news(browser):
    # Visit the mars nasa news site
    # url = 'https://redplanetscience.com'
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)
    # Optional delay for loading the page; and search for combo of (`div`) and attribute (`list_text`)
    # e.g., `ul.item_list` would be found in HTML as `<ul class="item_list">`; wait_time in seconds.
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # CSS works from right to left, returning last item on list instead of the first.
        slide_elem = news_soup.select_one('div.list_text')

        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        # news_p

    except AttributeError:
        return None, None

    return news_title, news_p

### Featured Images

# ## JPL Space Images Featured Image

    #.# This code below into a function called featured_image()
    #.# the function adds try/except error handling
    # # Visit URL
    # url = 'https://spaceimages-mars.com/'
    # browser.visit(url)

    # # Find and click the full image button
    # full_image_elem = browser.find_by_tag('button')[1]
    # full_image_elem.click()

    # # Parse the resulting html with soup
    # html = browser.html
    # img_soup = soup(html, 'html.parser')

    # # Find the relative image url
    # img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    # # img_url_rel = img_soup.find('a', class_='fancybox-thumbs').get('href')
    # img_url_rel

    # # Use the base URL to create an absolute URL
    # img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    # img_url

def featured_image(browser):    
    # Visit URL
    # url = 'https://spaceimages-mars.com/'
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        # img_url_rel = img_soup.find('a', class_='fancybox-thumbs').get('href')
        img_url_rel

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    # img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    # img_url

    return img_url

# ## Mars Facts

    #.# This code below into a function called mars_facts()
    #.# the function adds try/except error handling
    # # Scrape Mars' data facts entire table (instead of each row)
    # df = pd.read_html('https://galaxyfacts-mars.com/')[0]
    # # df.head()

    # df.columns=['description', 'Mars', 'Earth']
    # df.set_index('description', inplace=True)
    # df

    # df.to_html()

def mars_facts():

    try:
        # use `read_html` to scrape the facts table into a dataframe
        # Scrape Mars' data facts entire table (instead of each row)
        # df = pd.read_html('https://galaxyfacts-mars.com/')[0]
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
        # df.head()

    # Note BaseException since using Pandas' `read_html()` to pull data
    # instead of scraping with BeautifulSoup and Splinter so errors may be
    # other than AttributeError as for `mars_news()`, `featured_image()`
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    # df

    # Convert dataframe into HTML format, add bootstrap
    # return df.to_html()
    return df.to_html(classes="table table-striped")

#.# commented-out code line below add to `scrape_all()` function
# browser.quit()

# as at end of `app.py` file...
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())