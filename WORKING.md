# Project 5
## Working
The purpose of this file is to document the progress of this project step by step.

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


    NB:  
    I have placed an alias in .bash_profile in ~/
    ```
    alias run="python manage.py runserver"
    ```
    I am running on MacOSX. 


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

---
## Connect to the remote database.  
28. Open `settings.py` file and scroll down to the DATABASES section. Comment out the existing DATABASES dictionary. For the string use `heroku config`. We need to import dj_database_url

    ```python
    import dj_database_url


    DATABASES = {
        'default': dj_database_url.parse("postgres://tcqoipytozvlke:0317ac04ecd88e9874ad3cb2c06d75ca417acec39c4b7a9a37d11ab023b3e761@ec2-46-137-170-51.eu-west-1.compute.amazonaws.com:5432/d4cl9o887a7f6b")
    }
    ```
    dj_database_url.parse will create a new database connection for us.

29. migrate the database
    ```bash
    python manage.py migrate
    ```
30. Push to heroku
    ```bash
    git push heroku master
    ```
    NB - Heroku is using python 3.6.7
    This will fail asking us to run teh following code. Then push again
    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1
    git push heroku master
    ```
    Trying to access https://unique-corn.herokuapp.com/ , there is an application error. We need a `Procfile`.
31. Create a `Procfile`:
    ```bash
    echo web: gunicorn UniQueCorn.wsgi:application > Procfile
    ```
    Push both to github and heroku.

32. We need to add the url on heroku to ALLOWED_HOSTS in settings.py
    ```python
    ALLOWED_HOSTS = [
        . . .
        "unique-corn.herokuapp.com",
        ]
    ```
33. Migrate and Create a superuser
    ```python
    python manage.py migrate
    python manage.py createsuperuser
    ```
    username: test-admin  
    email: test@admin.com
    password: 1234qwer

    **Can access admin site locally. Pushed to Heroku but cannot access admin there.** 
    
    **I need to migrate for the progresql too as well as create the superuser for that database (same credentials).**   

    NB: No styling


## Change test app into a simple todo app (like tutorial) 
34. Within the `testing` app, in `models.py`  create a model for a simple database.  
    Add a dunder method `__str__` to the class to display the items in a verbose format rather than objects.
    ```python
    class Item(models.Model):
        name = models.Charfield(max_length=30, blank=False)
        done = models.BooleanField(blank=False, default=False)

        def __str__(self):
            return self.name
    ```
35. Make a migration and migrate this new model.  
    I am working directly with PostgreSQL
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
36. In order to display this in the admin panel I need to register it in `admin.py` (in app folder). Import and register the model.
    ```python
    from django.contrib import admin
    from .models import Item

    admin.site.register(Item)
    ```

37. Can display in admin now display in customer side.  
    Add a view, connect to a template and urlpattern.

    * Create a view in `views.py`. Connect the view with the model by importing it.
    ```python
    from .models import Item

    def test_todo_list(request):
        results = Item.objects.all()
        return render(request, “<todo_list>.html”, {'items': results})
    ```
    * Create a `todo_list.html` template

    * Create a urlpattern in `urls.py` (root)

38. Create A view to add items - with a form.
    * In view.py create a new view. This view need to be able to handle adding a new item to the database and redirect to the todo_list view.
    ```python
    from django.shortcuts import . . . redirect

    def test_create_an_item(request):
        if request.method=="POST":
            new_item = Item()  # instance of the Item model
            new_item.name = request.POST.get('name')
            new_item.done = 'done' in request.POST
            new_item.save()
            return redirect(test_todo_list)

        return render(request, 'add_item_form.html')
    ```

    * Create a new template `add_item_form.html`.
    Remember to add the csrf_token to the form.

    * Add related urlpattern, remember to import the view
    ```python
    url(r'^add$', test_create_an_item),
    ```
    ===========================  
    **I can use `django forms` which will:**  
        * **Automatically generate a form from a model,**  
        * **Automatically check for blank fields.**  
    It needs to inherit from `forms.ModelForm`.  
    We need to create an inner class called **Meta**.  
    This provides some additional info to django to tell it what we want.

    We need to create `forms.py` in the app directory.  
    It will import `froms` and our `model`.
    ```python
    from django import forms
    from .models import Item

    class ItemForm(forms.ModelForm):
        class Meta:
            model = Item
            fields = ('name', 'done')
    ```

    The view need to be updated. Import form.  

39. Edit an item.  
    **Using a link**  
    Add an edit link to each item in `todo_list.html`.
    If it is a table place this in a new column. If the table is displayed as a paragraph or list, there is no easy way how to align these links.  
    **Using a form**  
    Better still to use a form. This form will use the GET method. We will give each button an action of `edit`. This will call a urlpattern. We need to target a specific item and we will use the id of that item to achieve this.

    Create a view that will allow us to edit that specific item. We will use the `get_object_or_404` which has to be imported from `django.shortcuts`. If it cannot find the specific item with the id we are passing in will throw a 404 error. Create a filled form with the return item.  
    ```python
    def test_edit_an_item(request, id):
        item = get_object_or_404(Item, pk=id)
        form = ItemForm(instance=item)

        return render(request, 'add_item_django-form.html', {'form': form})
    ```
    Next, create a urlpattern for this view which has to handle the id value we are passing from the url.  
    ```python
    url(r'^edit/(?P<id>\d+)$', test_edit_an_item),
    ```

    Up to now we can run the code and see that the form is prepopulated with the selected item. We can make changes but nothing will happen when we submit.
    We need to add the logic as we did for the add an item.
    ```python
    def test_edit_an_item(request, id):
        item = get_object_or_404(Item, pk=id)

        if request.method == 'POST':
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect(test_todo_list)
        else:
            form = ItemForm(instance=item)
        
        return render(request, 'add_item_django-form.html', {'form': form})
    ```

40. Toggle Status  
    Directly toggle between done/not done straight from the list instead of having to go to another page.  
    Implement a toggle button to achieve this. Place it in a column before the edit button. Here we will have a form with a POST method. It will need a csrf token since it uses a POST method.  
    Create a toggle view.
    ```python
    def test_toggle_status(request, id):
        item = get_object_or_404(Item, pk=id)
        item.done = not item.done
        item.save()
        return redirect(test_todo_list)
    ```
    The url pattern for toggle status is
    ```python
    url(r'^toggle/(?P<id>\d+)$', test_toggle_status),
    ```

41. Implement Delete item  
    I want the ability to completely delete an item from the database. Add another column with a form and a submit element in the template.  
    The view to implement this is 
    ```python
    def test_delete_item(request, id):
        item = get_object_or_404(Item, pk=id)
        item.delete()
        return redirect(test_todo_list)
    ```
    The url pattern is
    ```python
    url(r'^delete/(?P<id>\d+)$', test_delete_item),
    ```
42. Setting up local environment variables  
    in ~/.bashprofile

    In order to refresh the bash shell run:
    ```bash
    . ~/.bash_profile
    ```
    NB: either deactivate the virtual environment before you refresh the bash shell or you will have to do it after, deactivate and reactivate.
    ```bash
    deactivate
    . venv/bin/activate
    ```

    for ALLOWED hosts add
    ```
    export SITE_HOST="127.0.0.1"
    ```
    This will be loaded in settings.py by using:
    ```python
    host = os.environ.get('SITE_HOST')
    if host:
        ALLOWED_HOSTS.append(host)
    ```
    Use this after defining ALLOWED_HOSTS.

    For heroku add SITE_HOST with value of 
    unique-corn.herokuapp.com to the Config Vars

    -------
    I changed the above to eliminate the use of the if logic.

    I renamed the local environment variable in .bash_profile to HOSTNAME to match the one I am using in Heroku, then simply load it directly in ALLOWED_HOSTS
    ```python
    ALLOWED_HOSTS = [
        os.environ.get('HOSTNAME'),
        ]
    ```

    If I was working in C9 I will add
    ```python
    os.environ.get('C9_HOSTNAME')
    ```
    ___
    Database connection string

    Use
    ```python
    DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
    ```
    for Heroku. DATABASE_URL was automatically set up when we start the postgresql database.

    This will not run locally. We will use sqlite3 instead.

    We need django to recognise if we are working locally as Development or on Heroku as Production.

    Locally (or on Cloud9), we will set an environment variable called `DEVELOPMENT`. 
    ```
    export DEVELOPMENT=1
    ```
    Remember to deactivate and activate the virtual environment for this to take place

    NB: refresh .bash_profile 
    ```
    . ~/bash_profile
    ```
    or export the variable for one-time use (in CLI)
    ```
    export DEVELOPMENT=1
    ```



    
    In settings we will check if this variable exist and if yes will set a variable `development` to True.
    ```python
    if os.environ.get('DEVELOPMENT'):
        development = True
    else:
        development = False
    ```

    This means that when we are on Heroku, there will be no DEVELOPMENT config var (we do not set one), and we will automatically be in production mode.

    We will use the `development` variable to set the DEBUG state
    ```python
    DEBUG = development
    ```
    By now, `development` will be **True** or **False** according to where we are.

    We also want the `development` variable to switch databases. We want to use sqlite3 if we are working locally, ie. development, and use PostgreSQL on Heroku.
    ```python
    if development:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    ```

    NB: might need to migrate the database for sqlite3 if not already done.
    ```bash
    python manage.py migrate
    ```
43. Use environment variables to store protected information and avoid pushing such information to github. A good example is the `SECRET_KEY` used by Django. We can store this locally as an environment variable and on heroku as aconfig var. We can also use different variables for different platforms.
We will get rid of the default key and create new keys, one for development and another for production. We can generate a new Django SECRET_KEY at [MiniWebtools](https://www.miniwebtool.com/django-secret-key-generator/)

Add a secret key to ~/.bash_profile
```
export SECRET_KEY="<Replace this with the value of the secret key>"
```
On heroku, from the dashboard, set a config var with key = SECRET_KEY and value = <A different secret key>. We can also do this using heroku toolbelt.
```bash
heroku config:set SECRET_KEY="<A different secret key>"
```

The secret key will be used for hashing passwords and other security related things.

Then we can access these variables in setting.py
```python
SECRET_KEY = os.environ.get('SECRET_KEY')
```

=======================
## TESTING

44. Implement testing  
    Django comes with its own testing framework.  
    main file needed is `tests.py` in the app folder. Test inherit from the base object called **`TestCase`**.
    ```python
    from django.test import TestCase
    ```
    For tests we need to create a class and methods inside that class. The class will inherit from TestCase.

    **NB: Test names should start with `test_` otherwise django will not find them and they will not be run.** This allows us to tell django which are test methods and which are supporting/helper methods.

    The first test we will write is a small Red-Green-Refactor test.
    ```python
    class TestDjango(TestCase):
        def test_is_this_thing_on(self):
            self.assertEqual(1, 0) # Step 1: This should fail - Red
    ```
    To run the test use
    ```bash
    python manage.py test
    ```
    This tells django to look for all the tests and run them.  
    Change the test and it passes.
    ```python
    class TestDjango(TestCase):
        def test_is_this_thing_on(self):
            # self.assertEqual(1, 0) # Step 1: This should fail - Red
            self.assertEqual(1, 1)  # Step 2: This should pass - Green
    ```

    We can also create different test files to test different parts. Ex: `test_forms.py` to test the functionality of forms, `test_views.py` to test the views and `test_models.py` to test the models.

    **testing forms**
    1. test: can create an item with just a name
    2. test: correct message for missing name
    3. test: can create an item with name and status

    **testing views**
    1. test: we are going to the correct location (correct url)
    2. test: status code
    3. test: correct template is used

    In order to test the edit page we need an item in the database with its own pk. We need to create an instance of the item model.

    4. Test if edit page fails it shows 404 status code
    5. Test toggle page. 
    6. Test delete item.

    **testing models**
    1. test: done defaults to False
    2. test: can create and item with name and status

45. Coverage  
    We need to install a tool that will show how how much of our code is actually tested.
    ```bash
    pip install coverage
    ```

    NB: I notice that there are several items installed that were installed automatically by visual studio code.

    We can then use coverage to run tests
    ```bash
    coverage run manage.py test
    ```
    This runs the test we have and analyses the code covered.  

    Next we can create a report to tell us how much code has been tested.
    ```bash
    coverage report
    ```
    By default, this will test all the code. We are interested in our code. We can limit the reporting to our own app **testing**.
    ```bash
    coverage run --source=testing manage.py test
    ```
    This says that we only want to test the files in the testing directory.

    Rerun the report
    ```bash
    (venv) $ coverage report
    Name                                 Stmts   Miss  Cover
    --------------------------------------------------------
    testing/__init__.py                      0      0   100%
    testing/admin.py                         3      0   100%
    testing/apps.py                          3      3     0%
    testing/forms.py                         6      0   100%
    testing/migrations/0001_initial.py       6      0   100%
    testing/migrations/__init__.py           0      0   100%
    testing/models.py                        6      1    83%
    testing/test_forms.py                   13      0   100%
    testing/test_models.py                  13      0   100%
    testing/test_views.py                   43      0   100%
    testing/tests.py                         4      0   100%
    testing/views.py                        44     14    68%
    --------------------------------------------------------
    TOTAL                                  141     18    87%
    ```

    We can improve on the readability and functionality of this report by generating an html file with links to the code.

    ```bash
    coverage html
    ```
    This will create a folder called `htmlcov`. Open the `index.html`.

    Everytime I add tests I run
    ```bash
    coverage run --source=testing manage.py test
    coverage html
    ```

    Ex: Test for the string representation of the model is not yet covered. Add a test for this.

    Add test for post create an item with both the normal form and the django form.

    Test for initial test which uses an HttpResponse

    What is left to test is the apps.py file. In general practice, aiming for 100% coverage is not necessary, especially for code that has been generated by django.
    It can be counter productive.

    We will test it just to get 100%. Create `test_app.py`.

## Autentication App - Authentication and Authorisation

For logging in and out of users  
* Authentication - recognises the user  
* Authorisation - you are allowed to be here  

46. Add an Accounts app  
    ```bash
    django-admin startapp accounts
    ```
47. Update installed apps in settings.py  
    I already have a superuser  

48. Create a templates folder in accounts app and create index.html.

49. Create a view and urlpattern

    ```python
    def index(request):
        """Return the index.html file"""
        return render(request, "index.html")
    ```

    ```python
    from accounts.views import index

    urlpatterns = [
        . . .
        url(r'^index$', index),
    ]
    ```

50. Link hrefs to urls. Ex:
    ```html
    <li><a href="{% url 'logout' %}">Logout</a></li>
    ```

51. Create the logout url and view.  
    for the view we need to do an import

    ```python
    def logout(request):
        """Log the user out"""
        auth.logout(request)
        return redirect(reverse('index'))
    ```
    ```python
    url(r'^accounts/logout/$', logout, name="logout"),
    ```

52. Using Django messages  
    A package that comes bundled in Django - allows us to provide messages from the backend to the user.  
    In order to use messages we need to:
    1. import messages from django.contrib
        ```python
        from django.contrib import . . ., messages
        ```
    2. include the necessary code in the view
        ```python
        messages.success(request, "You have successfully logged out.")
        ```
    3. Create an area in the html file to display the message.
        ```html
        {% if messages %}
            <div>
                {% for message in messages %}
                    {{ message }}
                {% endfor %}
            </div>
        {% endif %}
        ```
    4. Update settings.py file
        ````python
        MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
        ````

53. Create Login page  
    1. Create login view
        ```python
        def login(request):
            """Return a login page"""
            return render(request, 'login.html')
        ```

    2. Update link in template
        ```html
        <li><a href="{% url 'login' %}">Login</a></li>
        ```

    3. Copy all content of index.html to a login.html. Change heading.

    4. Add new url pattern

54. Add login form    
    1. Add forms.py in accounts folder. 
        ```python
        from django import forms

        class UserLoginForm(forms.Form):
            """Form to be used to login users."""
            username = forms.CharField()
            password = forms.CharField(widget=forms.PasswordInput)
        ```
    2. Update login view.  
        import the new form we created
        ```python
        from accounts.forms import UserLoginForm

        def login(request):
            """Return a login page"""
            login_form = UserLoginForm()
            return render(request, 'login.html', {'login_form': login_form})
        ```
    3. In login template add the form we are passing from the view wrapped inside a form element. Use POST method.  
        Add submit button and csrf token
        ```html
        <form method="POST">
            {% csrf_token %}
            {{ login_form.as_p }}
            <button type="submit">Login</button>
        </form>
        ```
    4. Add logic to view to handle POST
        ```python
        def login(request):
            """Return a login page"""

            if request.method == 'POST':
                login_form = UserLoginForm(request.POST)

                if login_form.is_valid():
                    user = auth.authenticate(
                            username=request.POST['username'],
                            password=request.POST['password'])
                    
                    if user:
                        auth.login(user=user, request=request)
                        messages.success(request, "You have successfully logged in.")
                    else:
                        login_form.add_error(None, "Your username or password is incorrect.")
            else:
                login_form = UserLoginForm()

            return render(request, 'login.html', {'login_form': login_form})
        ```

55. Apply template inheritance  
    (Better to start with this earlier on)
    Inside our root project directory, create a templates directory and create a `base.html` file.  
    Update the index.html to extend base.html.   
    We need to tell django to use the template from the new folder.  
    In settings.py, find the TEMPLATES list and update the DIRS key with a value pointing to the new directory.
    ```python
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ```

56. Check if user is logged in or not and change navigation accordingly.  
    Display login and register to users who are not logged in and logout and profile to users who are logged in.
    ```html
    <nav>
        <ul>
            {% if user.is_authenticated %}
                <li><a href="{% url 'logout' %}">Logout</a></li>
                <li><a href="#">Profile</a></li>
            {% else %}
                <li><a href="{% url 'login' %}">Login</a></li>
                <li><a href="#">Register</a></li>
            {% endif %}
        </ul>
    </nav>
    ```

57. Redirect logged in users to todo page

58. Allow logging out only to logged in users. Using `login_required` from `django.contrib.auth.decorators`.

59. Add login_required to todo views.

60. Update tests to pass for login_required views.

61. Registration functionality.  
    * create view
    * create urlpattern
    * update url for registration nav link in base.html
    * create registration template
    * Add registration form - these need to store information about the user so it need access to the User model provided by django.  
        We will use UserCreationForm which already has functionality for usernames and emails. We have to extend it to have passwords.  
        We also need some ValidationError.
        These are all imported.

    * Add form validation. Define methods with name starting `clean_`
        django will use that method to clean and validate that field as named after the clean_.

62. Create User Profiles  
    We want to be able to retrieve a user from  the database.
    * Create the necessary view
    * Create a urlpattern
    * Update link in the base.html nav
    * Create a profile template

63. Prepare for password reset

    create url_reset.py - allow us to create the reset-specific urls and mapped into views.
    Add a urls.py inside accounts app  
    Move all accounts realted urlpatterns inside this new urls.py. This allows us to keep all the accounts specific code inside the accounts app. This means we can import all the urls in one go inside the main project urls.py file.

64. Reset Password    

65. Send email to console.

66. Add Password reset template.
    create a registration folder under the main template folder (the one holding base.html).  
    In this new folder we will place the templates related to resetting password.
    * password_reset_form.html


    In login.html add link saying forgot password

67. Send an actual email using my own email. Notiice that django checks that the there is an account with the entered email, otherwise it will not send the email. A note to this effect is displayed to the user.

68. Building a `custom authentication backend` to log in using the email instead of the username.
    Add an `AUTHENTICATION_BACKENDS` to settings.py. It is a list.

    Then create a `backends.py` file in the accounts app folder. Here we need to create a class EmailAuth that we referred to from settings.py.

## Bootstrap styling and Custom styles

69. For bootstrap, paste bootstrap cdn links for scripts and stylesheets in base.html.  
    This results in basic bootstrap styling.

70. For navigation bar, add `navbar navbar-default` classes. Add more classes as necessary, ex `nav navbar-nav` to the ul element.

71. Using django forms bootstrap  
    This is to bootstrap the forms  
    We can easily change the button by copying some code from the boostrsap page.  
    For the form itself we need to use a third-party library called `django_forms_boostrap` which will give us a template tag to style the form with bootstrap.

    1. We need to install this.
        ```bash
        pip install django_forms_bootstrap
        ```
    2. Update requirements.txt

    3. Include it in INSTALLED_APPS in settings.py

    4. Update the form in registration.html to use bootstrap.  
    
        a. After extending from base.html add
        ```html
        {% load bootstrap_tags %}
        ```
        This imports the javascript of the bootstrap.  
        
        b. Instead of displaying the form as_p (or anything else) we will pipe it to bootstrap
        ```html
        {{ registration_form | as_bootstrap }}
        ```
        This takes the form and passes it to the `as_bootstrap` function which will apply the styling.

Alternatives:  
|   |   |   |  
|---|---|---|  
|.form-vertical | `{{ form|as_bootstrap }}` |	Labels over controls (default)|  
|.form-horizontal |	`{{ form|as_bootstrap_horizontal }}` | Labels on same line as controls |
|.form-inline |	`{{ form|as_bootstrap_inline }}` | Compact style with inline-block controls |
  
    5. Do the same for login.html and password_reset_form.html



72. Using Custom CSS

    1. Create a static folder at the top level of the project. and create a css folder inside it. In here create a file called styles.css

    2. in base.html link to this stylesheet.
    ```html
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    ```

    3. At the very top of base.html we need to create a template tag to load static
    ```html
    {% load staticfiles %}
    ```

    4. We need to register our static files in settings.py. Basically we tell django where to find the files.

73. Add some more password reset related templates:
    * password_reset_email.html
    * password_reset_done.html
    * password_reset_confirm.html
    * password_reset_complete.html

NOT SURE IF THEY ARE BEING USED.
Will deal with these later.

## Processing payment - Stripe

Need to use:  
`sessions` to keep track of the state between the site and the user's browser.  
`Stripe`, a tool for internet commerce, allows for the acceptance of payments.  
`AWS S3` - Amazon Web Services - provides on demand cloud computing platform. Can be used to serve the static and media files.

NB: I will build this app but later I might remove / adapt some of it to tailor it better to this tracker.

74. Create a Home App - for general pages, like `about` page.
    ```bash
    (venv)$ python manage.py startapp home
    ```
    
75. Add the Home app to settings.py

76. Add a view to render an html page, and a urls.py.
    I will change the urls so that the root url will render a new index from this app as well as an about page.
    view.py
    ```python
    from django.shortcuts import render, HttpResponse

    def index(request):
        return HttpResponse("This is the new Home page.")

    def about(request):
        return HttpResponse("This is the ABOUT page.")
    ```
    urls.py
    ```python
    from django.conf.urls import url
    from .views import index, about

    urlpatterns = [
        url(r'^$', index, name="index"),
        url(r'^about/$', about, name="about")
    ]
    ```
    top level urls.py
    (renamed the url pattern for say_hello)
    ```python
    from home import urls as home_urls
    . . .

    url(r'^', include(home_urls)),

    ...

    url(r'^hello$', say_hello),
    ```

# HEROKU PROBLEM WITH LOADING CSS
Trying to solve heroku not loading stitic files

Removed
DISABLE_COLLECTSTATIC = 1 from config vars and will push again.  
This does not work.

I did DISABLE_COLLECTSTATIC = 1

I also tried 
```
heroku run python manage.py collectstatic
```
but apparently I need to set `STATIC_ROOT` somewhere.

**STILL UNRESOLVED**
=================

77. Update home page to show an html file. Do the same for about page





&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

---

.  
.  
.  
.  
# TODO
[TOP](#Project-5)

Apply Caseinsensitive Backend Auth from ecommerce tutorial. See project on Cloud9.

Build Blog App

Connect the other password reset templates

Solve Heroku CSS problem.







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

