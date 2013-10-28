### Django URL Shortener

This app allows users to input a URL and save it as a shorter URL, with a unique code appended to the end of a base URL.

### Getting Setup

Begin by navigating to a directory you wish clone the project into, and then clone the project:

    $ git clone https://github.com/triplec1988/urlShortener.git

Then navigate to the project, create a virtual environment, and install the requirements

    $ cd urlShortener
    $ virtualenv --distribute venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

From here you'll need to validate the models and create a local sqlite3 database (no need to create a superuser)

    $ python manage.py syncdb

Now you can run the server

    $ python manage.py runserver

Navigate to `http://127.0.0.1:8000/shortener/list/` and check out the app in action!
