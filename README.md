# Workbench

<img width="1308" alt="workbench-project-overview" src="https://user-images.githubusercontent.com/68863341/126550474-3d109583-a929-4cb6-b7f6-b5f26dc8ba1d.png">

View the live website for this project on Heroku [here.](https://daisybutler-workbench.herokuapp.com/)

Workbench is a membership website which provides remote workers with access to fully equipped workspaces in locations throughout the UK. Members can choose between two different subscription plans to suit their access requirements. One-off access to meeting rooms and office space can also be purchased by subscribers and non-subscribers.

The idea of this website was inspired by the shift from in-person to remote working for all office-based companies during the coronavirus pandemic. With the belief that this shift is here to stay, the option to access fully-equipped office environments on a flexible basis will only continue to grow in demand.

## Table of Contents

1. [UX](#ux)

    * [Primary Goal](#primary-goal)

    * [User Profile](#user-profile)

    * [User Stories](#user-stories)

    * [Design Process](#design-process)

    * [UX Design](#ux-design)

    * [Colours](#colours)

    * [Fonts](#fonts)

    * [Wireframe Mockups](#wireframe-mockups)

2. [Features](#features)
    * [Pages](#pages)

        * [Home](#home)

        * [plans](#plans)

        * [Individual Plan](#individual-page)

        * [Checkout](#checkout)

        * [Login](#login)

        * [Profile](#profile)

    * [CRUD Functionality](#crud-functionality)

    * [Database Structure](#database-structure)

    * [Structure overview](#structure-overview)

    * [Field Relationships](#field-relationships)

    * [Features to Implement in the Future](#features-to-implement-in-the-future)

3. [Technologies Used](#technologies-used)

    * [Languages](#languages)

    * [Tools](#tools)

    * [Frameworks](#frameworks)

    * [Libraries](#libraries)

    * [Database Management System](#database-management-system)

    * [Graphics](#graphics)

4. [Testing](#testing)

5. [Deployment](#deployment)

6. [Credits](#credits)

    * [Inspiration](#inspiration)

    * [Media](#media)

    * [Code](#code)

## UX

### Primary Goal

The primary goal of this website is to get users to sign up for a monthly subscription plan in return for access to workspaces throughout the UK. The website markets the services available to potential members and allows existing members to manage their subscription and personal information.

### User Profile

- ***The ideal user of this website is:***

    An individual who is working remotely on a full time or flexible basis in a job which mainly requires them to be at a desktop. Predominately this will be office professionals but is likely to include self-employed individuals who would like to seperate home life from work life.

- ***Users of this website are looking to:***

    Access a fully-equipped workplace environment, in order to maximise their productivity and create a work/home life separation which working from home may not be facilitating for them.

- ***This website facilitates this for the user by providing:***

    Access to work-orientated environments on a regular basis. Two types of passes allow the user only to pay for the access they need, which accomodates both full-time and part-time flexible workers.

### User Stories

1. As a new user, I want to find out about the passes and facilities Workbench offers.
2. As a new user, I want to find out how much each Workbench pass will cost per month.
3. As a new user, I want to see where Workbench sites are located and where the nearest one to me is.
4. As a new user, I want to buy a Workbench pass.
5. As a new user, I want to buy a one-off meeting room or office space session when I don't have a pass.
6. As an existing user, I want to view my current pass and personal details and be able to edit or cancel them.
7. As as a new or existing user, I want to make payments securely and easily on the website.
8. As an existing user, I want to be able to log in and log out of my account.

### Design Process

- **UX Design**

1. Strategy Plane

During my research, I was influenced heavily by the global workspace provider ![WeWork](https://www.wework.com/en-GB). Arguably, they are the leaders in the area. Their business model is strongly rooted in simplicity and ease, which is a key component for a service looking to maximise productivity by minimising disruption for office-based workers.

2. Scope Plane

Having identified the main requirements and style for a workspace site, I investigated the scope of creating a website to satisfy it. The primary feature and main attraction of the website would to allow a user to make a plan purchase in order to access a Workbench. This process must be simple and the exact features included must be easy to identify. In order to fullfill this, the whole site must be orientated around getting the user to the checkout page. The site will achieve this in a subtle way by displaying multiple calls to action throughout the site which encourage the user to enquiry into more details about a plan and then continue to a checkout page.
In addition to this, the website must display information to the user about the times of plans and locations offers. Details about prices and included features must be accessible and clearly displayed, as well as easy location browsing for comfirmation of accessibility for the individual. This is will be achieved by a dedicated page for each plan which sets out all of the features included in a uniform fashion. Locations are also easily found usin the map on the locations page.

3. Structure Plane

Once I had decided on the features I wanted to include, I moved on to the structure. My pages would be divided up into 'Home', 'All Plans', 'Locations' and 'Contact', plus a navbar button for 'Login'. For authenticated users, the login button would be replaced with a logout button and a 'Profile' link would become accessible too.

4. Skeleton Plane

Having planned out my structure, I created wireframes in Figma (see #wireframes). On entering the site, the homepage would be displayed to the user. This would consist of a brief description of the service to assure the user they are in the right place for what they are looking for. Following this would be a display of the types of plans available with links to. Find out more information about each. Underneath this would be a more detailed instruction of how the service works and a final call to action at the bottom fo the page.

The All Plans page will display all of the available plans to the user within containers based on the plan time e.g. subscription or one-off followed by the short description of each. The user can click on the 'Learn More' button to be redirected to a individual plan page with more information. From this page, the user can either return to the all plans page or click continue to proceed to checkout.

The Locations page will display a map with the locations available for Workbench access. This interactive way of displaying locations is clear and easy way for the user to check accessibility.

The Contact page will allow the user to submit an enquiry to the Workbench site should they have a question which cannot be answered by the site. 

The Login button takes the user to a loin page where, if they are an existing Workbench user, they can login into their account and see/manage their plan.  

5. Surface Plane

I wanted the Workbench design to be simple with a light colour scheme since desirable workspace should be open and have plenty of light; a site to convey this vibe is therefore an important part of the marketing process. I chose red as the accent colour based off a personal liking for its combination with white and other neutral colours. It also has corporate vibes and, since this is the market the site is looking to target, the choice makes sense.


- **Colours**
    - #FFFFFF white (background)
    - #F7F7F7 light grey (backing contrast)
    - #D91F44 warm red (accent)
    - #EEECE7 warm beige (backing contrast)
    - #313131 black (footer, popups)
    
- **Fonts**
    - Headings - Open Sans semi-bold 600
    - Paragraphs - Open Sans regular 400
The choice of Open Sans for the text on the site was based on its neutrality as a font. It is easy to read and the san-serif gives the site a modern feel.

### Wireframe Mockups
#### Home
<img width="624" alt="home-wireframe" src="https://user-images.githubusercontent.com/68863341/126553038-a5142bd1-ca19-4446-824b-3bf54f607c94.png">

#### All Plans
<img width="775" alt="all-plans-wireframe" src="https://user-images.githubusercontent.com/68863341/126552808-e54def78-39a1-4e71-9d2c-85a01481ba95.png">

#### Individual Plan
<img width="807" alt="individual-plan-wireframe" src="https://user-images.githubusercontent.com/68863341/126552872-aeb8d73d-7baf-4775-b114-d348d7a0590c.png">

#### Locations
<img width="738" alt="locations-wireframe" src="https://user-images.githubusercontent.com/68863341/126552790-b6eb42b7-a333-4a3d-8bf1-1e1600d325a4.png">

#### Contact
<img width="743" alt="contact-wireframe" src="https://user-images.githubusercontent.com/68863341/126553743-c2f5a473-7242-47d7-83f5-d15194ea4531.png">

#### Profile
<img width="725" alt="profile-wireframe" src="https://user-images.githubusercontent.com/68863341/126552760-46c30025-e41f-472b-b8a1-8dc6e1b1bd00.png">

#### Login
<img width="744" alt="login-wireframe" src="https://user-images.githubusercontent.com/68863341/126553011-8d4c6c16-b941-4d1a-be79-6ac520113b3f.png">

This project's entire Figma wireframes can be accessed [here.](https://www.figma.com/file/LiH3RoaQylAGs7fQ1vsOiv/Milestone-4?node-id=31%3A11)

## Features

### Home
The homepage gives the user a simple idea of the service offered with a large landing image and description. Then all three types of plans are set out with call to action buttons to take the user to a page with more information about each one. Beneath this as a section describing multiple locations to access and a button to the Locations page. Below this is a three step guide to how using the Workbench service works and a final call to action at the bottom leading to the all plans page.

<img width="793" alt="home-demo" src="https://user-images.githubusercontent.com/68863341/126555304-776a7307-8698-402a-8ee9-d4d59749426a.png">

### Plans
The plans page presents the different purchasing options to the user, divided up based on their type. Passes for the whole month are in one box and one-off passes are in the box below. Each individual type of plan as a button which the user can click to take them to a page with the full description of that plan only.

<img width="793" alt="all-plans-demo" src="https://user-images.githubusercontent.com/68863341/126555412-5f79e40a-98cf-4cae-92e3-12714cda085a.png">

### Individual Plan
Each individual plan lists the plan's full details in a clear and easy to read format, including icons to break up the text. The user can either return to the previous page by clickin the 'All Plans' button or click 'Continue' to proceed to checkout with this plan.

<img width="598" alt="individual-plan-demo" src="https://user-images.githubusercontent.com/68863341/126555557-482ecf88-9e20-4b08-b064-5bc178ce00e1.png">

### Checkout
The checkout page is generated with the plan fields pre-populated based on what plan page the user came from. An order summary appears to the right of this. The user must fill out their billing, account and payment details before clicking the submit payment button. On successful payment, the user is redirected to the checkout complete page.

<img width="1006" alt="checkout-demo" src="https://user-images.githubusercontent.com/68863341/126555669-f4bc9e38-0ee2-4be1-9f53-3e94a85797f9.png">

### Checkout Complete
The checkout complete page displays a message to indicate that the payment as been successful and the membership is active. The plan details are also summarised below. A 'Visit Profile' encourages the user to visit their profile since an account has automatically been created for them in the database upon successful checkout.

<img width="1009" alt="checkout-complete-demo" src="https://user-images.githubusercontent.com/68863341/126555912-54034165-700c-405f-829d-0c58b93c1c3b.png">

### Profile
The profile page is only accessible for authenticated users and appears as a navigable link in the navbar if the user is logged in. The plan the user has purchased appears in a summary box, including details about when the plan is valid for. Below this, the user can find their username and a link to chane their account password. They can also update their default billin information on directly on the page.

<img width="925" alt="profile-demo" src="https://user-images.githubusercontent.com/68863341/126556035-efdc27a6-546c-4f93-b496-ae4f4de07285.png">

### Locations
The locations page renders an interactive map using the Google Map API. Users can see all of the locations where a Workbench can be access, which is a specification they need to make at checkout if they pick a one-off or standard plan. A call to action at the bottom of the page invites users to view the plans page.

<img width="829" alt="locations-demo" src="https://user-images.githubusercontent.com/68863341/126556361-dd44a6e8-f43c-42d9-8535-49a96cf9696e.png">

### Contact
The Contact page renders fields which allows them to submit a question or enquiry to the site owner via the EmailJS API. All fields are required before the user can submit their message and an email is sent to the site email address with a reply email.

<img width="837" alt="contact-demo" src="https://user-images.githubusercontent.com/68863341/126556239-b19c8430-27f1-44cc-8168-23a63cbc8b4d.png">

### Login
The login page displays in the navbar for users who are not authenticated. The page renders the django user login fields and a message indicating that only paying members are assigned an account. An option to choose a plan is given with the button to the plans page.

<img width="1310" alt="login-demo" src="https://user-images.githubusercontent.com/68863341/126557363-8cbc67c8-eb54-41fd-aef2-33ef16e965e1.png">

### Logout
The logout page displays in the navbar for users who are authenticated. The page renders a confirmation that the user wishes to log out and a log out button.

<img width="1152" alt="sign-out-demo" src="https://user-images.githubusercontent.com/68863341/126556559-e1d32529-7277-48f6-9e96-cff16346d859.png">

### CRUD Functionality

Users can create and manipulate data to be stored in the database as follows:
- CREATE an account as the product of a successful checkout process, which stores the personal details oof the user in a user profile in the database.
- READ their details, both personal and plan choice, on their profile page. Read about the types of plans and locations available rendered from the database on the site.
- UPDATE their personal details, including billingg details and account password, on their profile page.
- DELETE their account using the delete membership button.

### User Authentication
The site makes full use of the Django authentication system. Users have an account created for them on checkout and they can log in and out of the site with their username and chosen password. Manual siggnup is not possible since a user must have made a purchase to have an account, so the built-in signup view is blocked. Logging in allows the user access their stored personal details and the plan they have purchased. The profile page is only accessible if a user is authenticated.

### User Interaction
The user can create an order model in the checkout process as well as a profile model. Their use of these models can be edited via the profile pae where they can update their details or delete their profile and membership entirely.

### Stripe Implementation
The checkout app provides the site with e-commerce functionality using Stripe. After paying successfully, the user gains access to authenticated side of the site and has an active Workbench membership. This project uses Stripe's test functionality rather than actual live payments.

### Structure and Navigation
The project uses the Bootstrap framework to accomplish an aestheitc and fully-responsive layout. A navbar is present with links to all of the site's pages. On mobile devices this collapses in to a toggleable element to the left-hand side.

### Interactive Features
The site makes use of Javascript to provide an interactive experience for the user. The locations page features an interactive map powered by Google Maps API where a user can scroll and view the labels of all of the Workbench locations.

## Database Structure
The project features custom Django models in the plans, locations, checkout and profile apps. Each order model created at checkout is associated with a user model in the database via the userProfile foreign key, creating a relationship between the two entities.

### Features to Implement in the Future
A future feature to implement on the site would be a process for checking the period a user has left of the pass they have paid for. Then, when upgrading their pass, the user would only have to pay the difference for the new pass. At the moment, a user who makes another pass purchase has this new pass immediately replace their old one and are charge the enitre new fee. Obviously, this is a flaw in the application which would need to be addressed when being used for real world membership hosting to avoid overcharing customers.

## Technologies Used

### Languages
- HTML - base language for this project.
- CSS - used for styling the HTML code.
- **[JavaScript](https://www.javascript.com/)** - used to make the website interactive.
- **[Python3](https://www.python.org/download/releases/3.0/)** - used to build the backend of this project.
- **[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)** - this project uses the templating language Jinja for incorporating Python functionality into the frontend.

### Tools
- [**Gitpod**](https://www.gitpod.io/) - the IDE Gitpod was used in the building process of this website.
- [**HTML Validation**](https://validator.w3.org/) - HTML was validated using W3C Validator.
- [**CSS Validation**](https://jigsaw.w3.org/css-validator/) - CSS was validated using W3C CSS Validator.
- [**JSHint**](https://jshint.com/) - Javascript was validated using JSHint.
- [**PEP8 Online**](http://pep8online.com/) - Python was validated using PEP8 Online.
- [**Free Formatter**](https://www.freeformatter.com/) - Free Formatter was used to format all HTML, CSS and Javascript files.
- [**Google Chrome DevTools**](https://developers.google.com/web/tools/chrome-devtools) - DevTools were used to debug and test code in the browser.

### Frameworks
- **[Django](https://www.djangoproject.com/)** - this project uses the Django Python web framework for creating a fullstack application.
- **[Bootstrap](https://www.getbootstrap.com/)** - this project uses Bootstrap to optimise its layout and structure in the frontend.

### Libraries
- **[FontAwesome](https://fontawesome.com/)** - this project uses FontAwesome 5 to provide icons.
- **[Google Fonts](https://fonts.google.com/)** - this project uses Google Fonts to style the website's fonts.

### APIs
- **[EmailJS](https://www.emailjs.com/)** - this project uses EmailJS API to facilitate the sending of emails from users to site owner via to the Contact page.
- **[Google Maps API](https://www.emailjs.com/)** - this project uses the Google Maps API to render the interactive Javascript map on the Locations page.
- **[Stripe](https://www.stripe.com/)** - this project uses Stripe to facilitate e-commerce functionality in the site's checkout app.

### Hosting Platforms
- **[Heroku](https://www.heroku.com)** - this project uses Heroku to host its live deployment.
- **[Amazon Web Services](https://aws.amazon.com)** - this project uses Amazon Web Services to host its static and media files, specifically the Simple Storage Service (S3).

## Testing
Testing information can be found in this [TESTING.md file](TESTING.md).

## Deployment
This project was created in the IDE Gitpod and Github as remote repository. The deployed project on Heroku can be viewed [here.](https://daisybutler-workbench.herokuapp.com/)

This project requires registation with AWS and a S3 bucket for static and media files. Registation with Stripe is also required.

### Deployment to Heroku
To deploy to Heroku, I took the following steps:
1. I logged in to Heroku and from my dashboard, select "New" then "Create new app" from the dropdown menu.
2. I named my app and choose the region Europe as my closest region. Select "Create app".
3. On my dashboard I navigated to the resource  "Heroku Postgres" and select it as an add-on.
4. IN the command line in my IDE, I logged in to Heroku with: `heroku login` -i
5. I imported the python modules "dj_database_url" and "psycopg2" with the commands: `pip3 install dj_database_url`  and  `pip3 install psycopg2` .
6. I froze my installed modules in a requirements.txt file by entering the following into the terminal:`pip3 freeze > requirements.txt`
7. In my settings.py file, I imported dj_database_url in the head:`import dj_database_url`
8. I replace the default "DATABASES" configuration with:`DATABASES = {'default': dj_database_url.parse(os.environ.get('<DATABASE_URL>'))}`. My database url came from the "settings" tab within my Heroku dashboard.
9. I applied migrations to my new database configuration with:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
    - `heroku run python3 manage.py makemigrations`
    - `heroku run python3 manage.py migrate`
10. Then I created a superuser in the terminal with:`python3 manage.py createsuperuser`
11. In the "settings" tab of my Heroku dashboard, I selected "Reveal config vars" and set the following config vars:

<img width="910" alt="heroku-config-vars" src="https://user-images.githubusercontent.com/68863341/126898987-874ed2e0-b69a-41fb-a07b-2676d665ee98.png">

12. I then installed "gunicorn" with: `pip3 install gunicorn`

13. After installation, I create a "Procfile" and add the following in the file: `web: gunicorn <APP_NAME>.wsgi:application`

14. I temporarily disabled the collection of static files before deploying to Heroku since static files would be saved to AWS S3. I did this by adding "DISABLE_COLLECTSTATIC" with a value of "1" to my config variables (to be deleted after deploying to Heroku is complete).

15. In my settings.py, I added `['<HEROKU_APP_NAME>.herokuapp.com', 'localhost']` to ALLOWED_HOSTS.

16. I commited my changes and pushed to Github.

17. I initialised my Heroku git remote with the following: `heroku git:remote -a <HEROKU_NAPP_NAME>`

18. Finally, I pushed to Heroku with the following: `git push heroku master`

19. Setting deploys to automatic in Heroku would mean every push to the mater would also push to Heroku.

### How to run this project locally
To clone this project locally, you will need a GitHub account. Create a Github account [here.](https://github.com/)

To clone this project into Gitpod in Chrome, follow these steps:

1. Install the Gitpod Chrome extension. After installation, the extension will appear in the top right-hand corner of the browser.

2. Login into Gitpod with your GitHub username and password.

3. In GitHub, with this project's repository (daisybutler/workbench-ci-project-04) selected, click the green "Gitpod" button at the top right-hand corner of the repository. This will create a new Gitpod workspace from the code in the GitHub repository. You can now work on the project locally.

To clone this project into a local IDE, follow these steps:

1. Navigate to the GitHub repository for this project (daisybutler/workbench-ci-project-04).

2. Click "Code" in the top right-hand corner of the repository, next to the green Gitpod button.

3. With HTTPS selected, click the clipboard icon to the right of the HTTPS link to copy the clone URL to your clipboard.

4. In your local IDE, open the terminal. Ensure the current working directory is the one which you want the cloned directory to be made in.

5. Type git clone into the terminal, and then paste the URL you copied in Step 3: e.g. git clone https://github.com/USERNAME/REPOSITORY.

7. In the terminal window of your IDE, enter the following to install all required dependencies from the requirements.txt file: pip3 install -r requirements.txt.

Import os with the command import os. Then create an env.py file and add environment variables e.g. os.environ["VARIABLE_NAME"] = "YOUR_VALUE"

The project is now cloned locally and can be viewed in the browser by running the following command in the terminal window: python3 manage.py runserver and opening port 8000.

For more on cloning a repository from GitHub, visit [this link.](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

## Credits

### Inspiration

This project's business idea was modelled off of [WeWork](https://www.wework.com/en-GB), the leading provider workspaces to rent for companies and individuals. I liked their clean and straightforward appraoch to marketing their services and tried to relfect this in my own project design.

### Media

This project takes all of its media from [Unsplash](https://unsplash.com/).

### Code

A complete county dropdown list was taken from [here.](https://gist.github.com/olivertappin/4dcbf64e06aae132c12a8b9d302fae12)

This [Stack Overflow thread](https://stackoverflow.com/questions/29794052/how-could-one-disable-new-account-creation-with-django-allauth-but-still-allow/29799664#29799664) helped disable the Django sign up view, which automatically installed as part of the allauth package. 

[This code](https://stackoverflow.com/questions/33715879/how-to-delete-user-in-django) explained how to delete a user so that all expections are planned for.

How to hash a crispy-forms password field was accomplished with the help of [this thread.](https://stackoverflow.com/questions/24223654/django-crispy-forms-shows-password-as-clear-text)

[This tutorial](https://www.fullstackpython.com/django-template-loader-render-to-string-examples.html) helped me set up email confirmations.
