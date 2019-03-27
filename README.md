# **UniQueCorn Issue Tracker**
[![Build Status](https://travis-ci.org/abonello/project_5.svg?branch=master)](https://travis-ci.org/abonello/project_5)

----
## Project 5

*Milestone project for **Full-stack frameworks***  

This submission is part of the Fullstack Software Development diploma course offered by Code Institute.

*Developer: Anthony Bonello*  

_Github Repository_  
[project_5](https://github.com/abonello/project_5)

_Deployment_  
Name of app: **unique-corn**  
URI: [https://unique-corn.herokuapp.com/](https://unique-corn.herokuapp.com/)

-------
**INDEX**

* [INTRODUCTION](#introduction)
* [UXD](#uxd)  
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [WIREFRAMES](#wireframes)
* [TECHNOLOGIES USED](#technologies-used)
* [TESTING](#testing)
* [DEPLOYMENT](#deploy-to-heroku)

---
  
## INTRODUCTION
* [Back to TOP](#uniquecorn-issue-tracker)

This app allows users to log in bugs as well as asks for new features for a fictitious app, **UniQue Corn**, that supposedly produces corn to feed people. This app is mired in bugs and lack of proper functionality, so there will be lots of bugs to report. Users can also vote for features and bugs they would like to see fixed. The more votes a feature or bug has, the larger the likelihood they will be worked on.

Artistically, this app is a parody on the current political events in the UK related to the brexit issue.

---

## UXD
* [Back to TOP](#uniquecorn-issue-tracker)

This app tracks bugs and new features for a fictitious app called UniQue Corn. Data is stored in a **PostgreSQL** database. Users can buy coins which will be spent to request a new feature or vote up features and bugs.


### **Strategy** 
* [Back to TOP](#uniquecorn-issue-tracker)

#### What do I want as the owner of this web app?
I want users to be able to ask for new features and report bugs they find while using UniQue Corn App. Users can review features and bugs posted by others and leave comments about them. They can also vote for features and bugs to make them happen earlier. Users can vote for a particular feature or bug as many times as they wish if they particularly would like to support a specific one. They can even vote for their own submissions. After all, the more money we can do from this, the better.


#### What does it do?
Track issues, features and bugs raised by the users for the developers to deal with. The developers get an idea of urgency and users' backing from the amount of votes and comments. It is also a source of funding for developing the project.


#### How does it work
Users can read about the UniQueCorn App. If they register, they can request new functionality through the appropriate form. Users can also report bugs as well as comment and vote for features and bugs that are already on the system.

---

### **Scope** 
* [Back to TOP](#uniquecorn-issue-tracker)

#### Features

* The site is fully responsive.  
* Home page has quick links to important pages.  

The app should allow the user to fullfill the following tasks:

* Users can navigate through the site using a navigation system which is functional using typical menu system for both mobile and desktop platforms.  
* Users can register.  
* Users can log in.    
* Users can log out.  
* Users can see their own profile.  
* Users can reset the password (if they forget it).  
* Users can see forthcoming events on the home page.
* Users can read about UniQue Corn App.  
* Users can read the blog.  
* Users can read more information about us.  
* Users can contact us using a form.  


**The following pages/features require login.**  
* Users can buy coins. This feature has cart functionality and checkout that will accept payment using a card, powered by Stripe.  
* Users can read / add features (paid for by coins) and bugs (free).  
* Users can up-vote features and bugs (paid for by coins) increasing their likelihood to be worked on by the development team.  
* Users can add comments to both bugs and features (free for both).  
* Users can see information about how many comments and votes each feature and bug has in the form of dynamic charts. These, dynamically read the information directly from the database when the chart page is requested.


#### User stories

**User wants to register with the site**  
1. Click on the `Register` menu item.  
    (If the user had already registered previously, they will be allowed to go to the sign in page.)
2. Fill in the form.
3. Click the `Register` button.

**User wants to see their own profile** 
1. User clicks on the `Login` menu item (to log in if not already logged in).
2. User clicks on the `Profile` menu item.

This is useful if a user wants to check how many coins he/she owns.

**User needs to reset the password (ex if they forget it)**
1. (When logged out) The user clicks on the `Login` menu item.
2. The user clicks on the `Reset Password` link.
3. The user fills in the email and clicks on the `Reset Password` button.
4. If the email is used to register a user, an email will be sent. The same message will be displayed to the user independently of whether the email exist or not.
5. If the email was found in the database the user will receive an email containing a link to reset the password.
6. The user opens the email and clicks on the link inside. This will take the user to the `Reset Password` page.
7. The user is taken to a page confirming the change in password and contains a link to the `login page`.

**User wants to find info about forthcoming events**  

These are found on the home page.

**User wants to read about UniQue Corn App**  

This is found the `UQC App` page. This can be reached by selecting the `UQC App` menu item or from the `UQC App Quick link` in the home page.

**User wants to download the UniQue Corn App**  

Sorry but due to the multitude of bugs in this app and the high risk to human life the download of this app has been restricted for the forseable future.

**User wants to read the blog**  

This is found in the `Blog` page. This can be reached by selecting the `Blog` menu item or from the `Blog Quick link` in the home page.

**User wants to read more information about us**  

This is found in the `About` page. This can be reached by selecting the `About` menu item.

**User wants to contact us using**  

A specific form for this purpose can be found by following the `Contact Us` menu item. 
1. The user fills in all the fields of this form.
2. The user clicks the `Submit` button.

&nbsp;

**The following user stories require login.** 

**User wants to buy coins**
1. After logging in the user goes to the `Coins` page (use the `Coins` menu item)
2. The default number of packages to buy is one. The user can change this.
3. The user clicks on the `Add` button.
4. The number of packages selected by the user will be placed in the cart. The `cart icon` is now bright red and a `badge` showing the number of packages in the cart is displayed next to the `Cart` menu item.
5. The user clicks on the `Cart` menu item.
6. The user can review the coins that are about to be bought. (The user can change the quantity at this stage by entering a different number for the quantity and click on the `Amend` button.) The total number of coins and the total cost is displayed.
7. After reviewing the information, the user can proceed to the checkout by clicking on the `Checkout` button.
8. The user fills in the required fields in the payment form.
9. The user clicks on the `Submit Payment` button.
10. A message will be displayed to the user saying if the payment was successful or not.

**User wants to read information about features and bugs submitted**  

This is found the `Features and Bugs` page. This can be reached by selecting the `Features & Bugs` menu item or from the `Issue Tracker Quick link` in the home page.

**User wants to see information about how many comments and votes each feature and bug has**  

This can be viewed in the form of dynamic charts. These graphs read information directly from the database upon requesting the charts page.  
This is found the `Charts` page. This can be reached by selecting the `Charts` menu item.

**User wants to add a feature (paid for by coins) or bug (free)**  
1. After logging in the user goes to `Features and Bugs` page (explained above).
2. The user clicks on the `Add a Feature or Bug` button.
3. The user is taken to a new page with a form for this purpose.  
4. In the form, the user selects if a feature or a bug is to be added.  
5. The user fills in a title and a description.
6. The user clicks the `Save` button.  
NB: Adding a feature costs 300 coins. Adding a bug is free.  


**User wants to add a comment to either a bug or a feature**   (Both actions are free)  
1. After logging in the user goes to `Features and Bugs` page (explained above).
2. The user clicks on the `Add a Comment` button.
3. The user is taken to a new page with a form for this purpose.  
4. In the form, the user selects the feature or bug to which the comment is to be added. (a reminder is displayed to the user)  
5. The user fills in a `subject` and a `comment`.
6. The user clicks the `Save` button.

**User wants to up-vote a feature or a bugs** (paid for by coins)   

This increases the likelihood that this feature or bug is chosen to be worked on by the development team.  
1. After logging in the user goes to `Features and Bugs` page (explained above).
2. The user clicks on the `Promote this Feature` button.
3. A vote is added to the feature or bug that was voted for by the user.

### **Structure**

* [Back to TOP](#uniquecorn-issue-tracker)

#### Navigation
There is a fixed navigation bar at the top of the page which contains the `Logo` and the `account-related` menu items. It also holds the `Cart`. In mobile view it will also hold the menu `burger` button.
What is displayed in the account menu will depend on whether the user is loggin in or not.  
While logged out, the menu will display:
1. Login
2. Register

When a user is logged in, the menu will display:
1. Log Out
2. Profile

Below this menu there is a `showcase` section in the home page and a `title` section in the other pages. Then there is the main navigation menu. This is sticky and when the page is scrolled up it will stick below the other navigation row. In mobile view, this sticky menu is hidden and will be activated by the burger button in the previous navigation.  
This main menu allows the user to navigate to the main parts of the app.  
Some of the menu items in the main menu will only be displayed when the user is logged in.

#### Pages

1. The home page is graphic above the fold while displaying the navigation menus. Scrolling down three image based quick links are displayed. Then there is a section listing future events. At the bottom there is a footer which is common to all pages. The footer contains further links to the `About` and `Contact Us` pages. It also contains info about the company, an email and copyright info.

2. Pages for About, Blog and UQC App. These are mainly information pages.

3. Contact page allows users to contact the site admin using a form.

4. Issue tracker page. This has a tab structure, one tab for features and the other for bugs. Each tab will hold a sequence of panels, one for each feature or bug. Each panel will hold all the information related to that particular issue.  
    * Title
    * Description
    * button to add comments
    * List of comments (if any):  
        * Comment #
        * Subject
        * Comment's posted by and date/time
        * Comment text
    * Issue's posted by and date, Votes, Button to vote for this issue, a note about payment.

5. Charts displays information about the features and bugs in a graphic way. These graphs are powered by `Chart.js`.

-----------


### Skeleton
* [Back to TOP](#uniquecorn-issue-tracker)

Navigation

Two menus:  
In mobile view, the menu related to the user account and cart is visible in the nav bar while the menu for the web-app navigation is collapsed to a button on the right of the nav bar.
In desktop view, the menu related to the user account and cart remains in the top nav bar while the menu for the web-app navigation takes its own nav bar.

A banner with a headline sits between the menus on home page, while the main title sits below the second menu. The banner is removed from internal pages and the title takes place between the menus. The lower menu is sticky and it sits below the top menu when scrolling. 

The reason for having two menus is two fold. It gives more room for navigation and separates the context of the links within these menus.

The account related menu displays links depending on whether the user is loggin in or not. It displays `Login` and `Register` while the user is logged out and `Log Out` and `Profile` while the user is logged in. The cart will display in both cases but when the user is logged out the cart link is disabled.

The main menu will also differ depending on log in status of the user.  
While the user is logged out it will show the following links:
* Home
* UQC App
* Blog
* About
* Contact Us

When the user logs in, the following links will be added:
* Features & Bugs
* Charts
* Coins

On the Home page there are three quick links to the most important pages. These are image links. There is also a list of events.

At the bottom there is a footer which has the About and Contact Us links.

Pages:
* **`Home`** - has three quick links to the most important pages. These are image links. There is also a static list of events. (This can be dynamic in a new version of this app.)
* **`Features and Bugs`** - Requires login. At the top there is a button to add a new feature or bug. This page has two tabs, one for features and another one for bugs. Each tab is divided into sections, one for each feature or bug. Each section will have the information about each issue as well as comments. There are links to add a comment for that issue and to vote that issue up.
* **`Add Feature or Bug`** - Requires login. This can be reached from the Features and Bugs page.
* **`Charts`** - Requires login. This page has dynamic charts that show the amount of votes per feature, the amount of comments per feature and similarly for bugs.
* **`Coins`** - Requires login. Here the user can buy one or more packets of coins. The packets will be placed in the cart.
* **`UQC App`** - Information about the fictitious app.
* **`Blog`** - A static page that displays blog-like text. This can be upgraded later on to be dynamic, allowing the addition of new blog stories from the front end by specifically authorised users.
* **`About`** - Info about this project.
* **`Contact Us`** - A form that allows user to contact the developers team.
* **`Cart`** - Requires login. Coins that the user wants to buy will be placed here. The user can cancel a buy by setting the quantity to 0, or increase the number of coin packets to buy by setting the quantity as required and amend the cart. When there are items in the cart, the fav icon (in the nav bar) changes color to full red (it was dimmed before) and a badge showing the quantity of packets in the cart is displayed next to the cart link in the nav bar.
* **`Checkout`** - Requires login. When users are ready to pay for the coins, they can click on the `Checkout` button in the cart page. This will take them to the checkout page where they can enter the necessary information to pay for the items by card.
* **`Log in`** - A simple form that allows the user to log in. There is also the functionality to allow the user to ask for a new password.
* **`Register`** - A simple form that allows a new user to register and set up a new account.
* **`Profile`** - Requires login. A user can see information about his/her account including the amount of coins they currently hold.

[wireframe](#wireframes) - follow this link for further reading
------

### Surface
* [Back to TOP](#uniquecorn-issue-tracker)

#### Typography

The font **`Roboto`** is used as the main font for this app.  

The font **`Coiny`** is used for the Logo.  

The font **`Acme`** is used for Headings.  Acme and Coiny are combined to produce the Main title on the home page.  

 Variations on the Roboto font are achieved by using letter spacing and a variety of font weights and sizes. This helps break text and help create patterns that guide the eye where there are repeated sections, example the features and bugs tab with comments. This becomes more obvious when there are multiple comments.

The colors are derived from the natural color of ripe corn (gold-like color) and a complementary color (Blues).

## WIREFRAMES
* [Back to TOP](#uniquecorn-issue-tracker)  
* [Back to Skeleton](#skeleton)


Please click on these thumbnails to see larger images. Please note that they will open in the same window so you will have to use the back button to come back here. To avoid this, right click on the thumbnail and select `Open Link in New Tab`.

If you would like to access all the images in the wireframe folder, please use [this link](https://github.com/abonello/project_5/tree/master/Wireframe).

### Mobile Home Page  
[![Mobile Home Page](Wireframe/mobile_home_page-Thumbnail.png)](Wireframe/mobile_home_page.png)

### Desktop Home Page
[![](Wireframe/desktop_home_page-Thumbnail.png)](Wireframe/desktop_home_page.png)

### Desktop Features and Bugs page
[![](Wireframe/desktop_features_and_bugs_page-Thumbnail.png)](Wireframe/desktop_features_and_bugs_page.png)

### Desktop Charts Page
[![](Wireframe/desktop_charts_page-Thumbnail.png)](Wireframe/desktop_charts_page.png)


## TECHNOLOGIES USED
* [Back to TOP](#uniquecorn-issue-tracker)

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used to build the sctructure and the content of this project.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - used for styling this project.
- [jQuery v3.3.1](https://jquery.com) - simplifies accessing the DOM.
- [Bootstrap v3.3.7](https://getbootstrap.com/docs/3.3/) - used for some of the styles (modified), as well as layout of the content.
- [Font Awesome v4.7.0](https://fontawesome.com/v4.7.0/) - used to display icons in navbar as well as the GitHub and Linkedin Icons.
- [Google Fonts](https://fonts.google.com/) - Acme, Roboto and Coiny.
- [Chart.js v2.7.3](https://www.chartjs.org/) - used to generate the dynamic charts.
- [Stripe](https://stripe.com/gb) - used to enable card payment.
- [Django](https://www.djangoproject.com/) - This is a django project and has a number of apps that work together to build this web application.
- [Python3](https://www.python.org/) - The main language for the backend.
- [SQLite](https://www.sqlite.org/index.html) - used as a local database when in debug mode or if not in debug mode while a url for another database is not available.
- [ProgreSQL](https://www.postgresql.org/) - The main database used for deployment on Heroku.
- [Travis CI](https://travis-ci.org/) - used for integrating continuous testing. The status of build tests is displayed at the top of this readme file on github.
- [Heroku](https://www.heroku.com/) - used for deploying this application on the web.
- [Github](https://github.com/) - used for version control.


## TESTING
* [Back to TOP](#uniquecorn-issue-tracker)

The functionality of this app has undergone extensive manual testing and some automated testing using Django's testing capabilities.

The manual testing caught a number of bugs during developing which were fixed. These bugs ranged from logic problems to styling, expecially relating to inacuracies in responsive design. These have been fixed.

I also explored a couple of ways of setting environment variables locally (MacOSX). I tried both setting the variables in `.bash_profile` as well as creating an `env.py` file. I finally settled to use an `env.py` file that I import in settings.py. (NB DEVELOPMENT=1 will still need to be in `.bash_profile`).

**Validated HML** using [Nu Html Checker (w3.org)](https://validator.w3.org/nu/#textarea)
few warnings:
* warning in issue-charts.html for code in Charts.min.js
* Errors in checkout.html for code supplied by Stripe. Frameborder, allowtransparency and scrolling in the iframes are obsolete.
* Warning in the home page for a section which does not have a header. I will leave this as is.

**Validating CSS** using [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator)  
No errors found.

Checked **js syntax** using [Esprima](http://esprima.org/demo/validate.html)  
Code is syntactically valid.


## Deploy to Heroku

* [Back to TOP](#uniquecorn-issue-tracker)

_Github Repository_  
[project_5](https://github.com/abonello/project_5)

_Deployment_  
Name of app: **unique-corn**  
URI: [https://unique-corn.herokuapp.com/](https://unique-corn.herokuapp.com/)

The following documents the steps needed to deploy this app on Heroku. Other deployments may defer in detail but main steps will broadly be the same.  

If you would like to install this app follow the following steps:

1. Download the app from this [github repository](https://github.com/abonello/project_5)

2. Set it up to work on your local machine.

3. Create a superuser
    ```bash
     python manage.py createsuperuser
     ```

4. For deploying on the net, create a new app on heroku and push this repository there.

5. The requirements.txt included lists all the required installs.

6. You will need to set up a database. This app currently uses a PostgreSQL database. No changes will be necessary if you are using PostgreSQL but if you decide to use a different database you will need to make corresponding changes in `settings.py`.

7. You need to migrate the models to your newly setup database. You can use sqlite3 locally to run the migrates and then switch to your chosen database. Alternatively, make sure you have environment variables set up locally. See below for the list of variables needed.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Go to the admin panel and in the Products table create a product called 500 Coins. Write some text as description. Select an image (not important which as I have hard coded this from the static/img folder). Give it a price. I used €200.

9. You will need to set up some environment variables. Follow the instructions for your chosen deployment platform.
    * DATABASE_URL - your database url
    * EMAIL_ADDRESS_WEBADMIN - your admin email address
    * EMAIL_HOST_WEBADMIN - your email host
    * EMAIL_PASSWORD_WEBADMIN - your email password
    * EMAIL_PORT_WEBADMIN - your email port
    * HOSTNAME - the host name where you deployed this app
    * SECRET_KEY - the Django secret key. For instructions to generate a new one go [here](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key).
    * STRIPE_PUBLISHABLE - I am using stripe to take care of card payment. You will need to create a Stripe account. This will be the publishable key.
    * STRIPE_SECRET - This is the Stripe secret key.

   If you are working locally you should set a variable called DEVELOPMENT. Set this equal to 1. I am exporting mine from `.bash_profile` file.
   As a result of this, debug is set to true and sqlite3 database is used as the local database.  
   If you do not wish to use this default behaviour you will need to do some changes in settings.py. These changes will depend on what you would like to achieve.

10. You will need to start adding a few features, bugs and comments. These will be displayed in the `Features & Bugs` page and will start populating the charts.


&nbsp;   
&nbsp;   

---
