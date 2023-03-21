Interview task for the position of Senior Python Dev at UpdateOne
=========================
### Prerequisites:
* Python 3.11
* PIP
___________________________________________________
### Instructions for running the project:

* Install all prerequisites for this repository
* Run `pip install -r requirements.txt` for the project requirements
* Use `python manage.py runserver` to start the Django server
* Access it on the default localhost:port url (Usually that would be `http://127.0.0.1:8000/`)
___________________________________________________
### Workflow and Technology description:
When approaching the task I decided to utilize Django as it has a very easy to setup and use 
"out-of-the-box" structure. It allowed me to very quickly setup a server with the necessary request handling,
URL routing, and template building. I decided on using Bootstrap for stylization of the page as it had everything
I would require to make it look presentable. Because of that, I also decided not to use local static files for CSS 
as the overhead for managing proprietary static files for 3 or 4 CSS properties seemed unnecessary.


Once I was done setting up the Django project I began researching and
studying the API provided in the task. I failed to find a way to painlessly integrate the GitHub repo directly
into my project so I decided on re-using (copying) their python API class and using it as is. Once I established
that, I simply went through the API data structure, picked out what I was going to need, implemented the
filtering neccesary for each sub-task requirement and organized the data. At the same time I was iteratively
developing the template structure I would need to display the data in a comprehensive way.
Once I had the data and templates done I worked on adding a search functionality, spent some time testing the whole
implementation, fiddled around with the styling to make it as responsive as I could at the time and cleaned up the
code.