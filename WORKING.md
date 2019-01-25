# Project 5
## Working

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
8. Start a new repository on github and create remotes
    ```bash
    $ git remote add origin https://github.com/abonello/project_5.git
    ```
