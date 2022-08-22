# Mission-to-Mars
HTML/CSS Web Scraping

## Project Outline
The analysis for this project consists of a background summary and coding notes.

### Background
Create a web page populated with images, data, articles related to planet Mars, an interest of junior data scientist "Robin" who freelances astronomy work in spare time and whose dream is to work for NASA.

Areas of web page "storyboard" were comprised of data as listed in table below<sup>I</sup>:

><sup>Table formatting from README.md for course repository,
as edited by TA J Caro.</sup>

|Section|Provider|Website|
|---|---|---|
|Mars News|NASA|https: // redplanetscience.com|
|Featured Image|JPL|https: // spaceimages-mars.com|
|Facts Table||https: // galaxyfacts-mars.com|
|Hemispheres|GUSS|https: // marshemispheres.com|

<sup>I</sup> Tools utilized, summarized below, were as presented in Module 10.0.1 video and 10.1.1 installation notes.

|Tool|Provides capability to|
|---|---|
|Chrome Developer Tools|Identify HTML components|
|BeautifulSoup (\*) and Splinter (#) |Automate scrape: (#) To automate Web browser (\*) To extract data needed for analysis |
|Mongo - NoSQL database|Store the ("unstructured" \| unrelated) data|
|Flask|Display in Web application; executes scraping code, replete with button to update page with newest data|
|Bootstrap|Build a polished portfolio; framework of pre-assembled component pieces|
|Flask-PyMongo|Bridge the tools|
|(html5lib, lxml)|(libraries)|

### Coding Notes
Installation challenges encountered (solved by TA J Caro, instructional team):
- splinter with selenium versions
- MongoDB execution

Challenge issues:
- Website became unavailable
- order of precedence of Bootstrap / CSS elements
