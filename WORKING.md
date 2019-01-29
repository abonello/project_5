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





# NB

## * Will explore Testing later

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

