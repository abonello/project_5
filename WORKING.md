# Project 5
## Working

# **UniQueCorn Issue Tracker**

[NOTES ABOUT THIS PROJECT](#Notes-about-this-project)

## Step 1
1. Create project folder
2. Create virtual environment with Python 3.7
    ```bash
    $ virtualenv venv -p python3.7
    ```
3. Start virtual environment
    ```bash
    $ . venv/bin/activate
    ```
4. Install django 1.11.15
    ```bash
    (venv) $ pip install django==1.11.15
    ```
    This installs Django 1.11.15 and pytz 2018.9
5. Initialise Git repository
    ```bash
    (venv) $ git init
    ```
6. Create README.md and .gitignore
7. Create requirements.txt
    ```bash
    (venv) $ pip freeze --local > requirements.txt
    ```
    commit.
8. Start a new repository on github and create remotes and commit
    ```bash
    $ git remote add origin https://github.com/abonello/project_5.git
    $ git push -u origin master
    ```
---
### **Notes** 

I already have heroku toolbelt installed on my computer.
```bash
$ heroku
```
gives a list of commands available to use together with a short description.

```bash
$ heroku apps
```
Will give us a list of apps. If you are not logged in you will need to enter login details.

Can also login using:
```bash
$ heroku login
```
Good to switch between accounts too.  
If `heroku login` sends you to the browser,  
try `heroku login -i`.

---
9. Install gunicorn
    ```bash
    (venv) $ pip install gunicorn
    ```
    This installs gunicorn 19.9.0  
    This will run the application on the server.

10. Install psycopg2
    ```bash
    (venv) $ pip install psycopg2
    ```
    This installs psycopg2   2.7.7  
    This allows us to connect to a PostgreSQL database.
11. Update requirements.txt
    ```bash
    (venv) $ pip freeze --local > requirements.txt
    ```
    commit.

12. Create a heroku app
    ```bash
    $ heroku create unique-corn --region eu
    ```
    https://unique-corn.herokuapp.com   
    https://git.heroku.com/unique-corn.git

13. Create a new database on heroku (PostgreSQL)  
    Heroku uses addons to set up databases.
    ```bash
    $ heroku addons:create heroku-postgresql:hobby-dev
    ```
    This creates an empty database.  

    ```
    Database has been created and is available
    ! This database is empty. If upgrading, you can transfer
    ! data from another database with pg:copy
    Created postgresql-closed-64850 as DATABASE_URL
    Use heroku addons:docs heroku-postgresql to view documentation
    ```
14. Install dj_database_url  
    ```bash
    (venv) $ pip install dj_database_url
    ```
    This allows us to parse database urls.
    This installs dj-database-url 0.5.0

15. Update requirements.txt
    ```bash
    (venv) $ pip freeze --local > requirements.txt
    ```
    and commit.

16. We can view the DATABASE_URL
    ```bash
    $ heroku config
    ```
    This will show us the url of the database which we need for the next step.  
    The same url can be found through the heroku dashboard. Go to settings and open the Config Variables.

17. Create a django project
    Call it `UniQueCorn` and put it at the root level of this directory by using `.`.
    ```bash
    django-admin startproject UniQueCorn .
    ```
    Placing it in the root will become important when we get to deploy on Heroku.

18. Running the django server

    ```bash
    (venv) $ python manage.py runserver 0.0.0.0:8000
    ```

    ===========================
    If I get `Error: That port is already in use.` I can see the servers running
    ```bash
    (venv) $ lsof -i :8000
    ```
    This will return info about servers running including PID
    ```bash
    COMMAND     PID           USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    python3.7 28335 anthonybonello    6u  IPv4 0x891c88db52932009      0t0  TCP *:irdmi (LISTEN)
    ```
    Then use the PID to kill that process:
    kill -9 <PID>
    ```bash
    (venv) $ kill -9 28335
    ```
    ===========================

    ---

    This is giving me an error. A quick goodle search shows:  
    this is a problem between Django and Python 3.7. [Django has a fix](https://github.com/django/django/commit/931c60c5216bd71bc11f489e00e063331cf21f40), but that fix hasn’t made it into a new version yet.

    NB
    line 152 of widgets.py
    ```python
    if params:
        related_url += '?' + '&amp;'.join(
            '%s=%s' % (k, v) for k, v in params.items(),
        )
    ```
    should be replaced by
    ```python
    if params:
        related_url += '?' + '&amp;'.join('%s=%s' % (k, v) for k, v in params.items())
    ```
    Now it works and the server starts properly.
    ---

19. Add 0.0.0.0 to ALLOWED_HOSTS in settings.py
    ```python
    ALLOWED_HOSTS = [
        "0.0.0.0"
        ]
    ```

20. Add **\*.sqlite3** and **\_\_pycache\_\_** to `.gitignore`.

21. Creating a `testing` app (in the root of the project) (At same level you have manage.py)
    ```bash
    $ django-admin startapp testing
    ```
22. Add the new app to the INSTALLED_APPS in `settings.py`.

23. Add a testing view and connect to url pattern  
    in views.py
    ```python
    from django.shortcuts import render, HttpResponse

    def say_hello(request):
        return HttpResponse("Hello World - This is a test")
    ```
24. Add a testing url pattern  
    in urls.py (in root), add
    ```python
    from testing.views import say_hello

    urlpatterns = [
        . . .,
        url(r'^$', say_hello),
    ]
    ```

    NB: Had to move testing app one level down in folder structure.

25. Create a template  
    Start by creating a `templates` folder in the app directory and create an html file which will be the test template, `test.html`.

26. In `view.py` create a view that will render the test template.
    ```python
    def render_test_template(request):
        return render(request, “test.html”)
    ```
27. Create the url pattern for this new view in `urls.py` (root).
    ```python
        from testing.views import . . ., render_test_template

    urlpatterns = [
        . . .,
        url(r'^test$', render_test_template)
    ]
    ```







&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

---
I am going to create a test app before proceeding to database.

-- Connect to the remote database.  
    Open `settings.py` file and scroll down to the DATABASES section.







&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

---

.  
.  
.  
.  
# Notes about this project
[TOP](#Project-5)

**Name of main app:**  
`UniQueCorn App`

**Name of this project:**  
`UniQueCorn Issue Tracker`

**Product advert:**  
* Corn generated by numbers - NO side effects  

* Now you can produce your own food at the comfort of your home directly from your computer using our UniQueCorn App.

* This product has been designed to provide a balanced diet in a single product.

**Currently known problems:**   
Humans who consume significant amounts of UniQueCorn suffer from severe malnutrition.

Help us to develop this product further by suggesting new features to this app and reproting bugs.

Main colors to use will be taken from corn color as well as various levels of grey, black and white.

