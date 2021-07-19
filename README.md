# Workbench

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

    Access to work-orientated environments on a subscription basis. Two types of subscription plans allows the user only pay for the access they need, which accomodates both full-time and part-time flexible workers.

### User Stories

1. As a new user, I want to find out about the subscription plans and facilities Workbench offers.
2. As a new user, I want to find out how much each Workbench plan will cost per month.
3. As a new user, I want to see where Workbench sites are located and where the nearest one to me is.
4. As a new user, I want to buy a Workbench subscription.
5. As a new user, I want to buy a one-off meeting room or office space session when I don't have a subscription.
6. As an existing user, I want to buy a one-off meeting room or office space session on top of my subscription.
7. As an existing user, I want to view my current subscription and personal details and be able to edit or cancel them.
8. As as a new or existing user, I want to make payments securely and easily on the website.
9. As an existing user, I want to be able to log in and log out of my account.

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
![Home]()
![Plans]()
![Locations]()
![Contact]()
![Profile]()
![Login]()

## Features

### Home
The homepage gives the user a simple idea of the service offered with a large landing image and description. Then all three types of plans are set out with call to action buttons to take the user to a page with more information about each one. Beneath this as a section describing multiple locations to access and a button to the Locations page. Below this is a three step guide to how using the Workbench service works and a final call to action at the bottom leading to the all plans page.

### Plans
The plans page presents the different purchasing options to the user, divided up based on their type. Passes for the whole month are in one box and one-off passes are in the box below. Each individual type of plan as a button which the user can click to take them to a page with the full description of that plan only.

### Individual Plan
Each individual plan lists the plan's full details in a clear and easy to read format, including icons to break up the text. The user can either return to the previous page by clickin the 'All Plans' button or click 'Continue' to proceed to checkout with this plan.

### Checkout
The checkout page is generated with the plan fields pre-populated based on what plan page the user came from. An order summary appears to the right of this. The user must fill out their billing, account and payment details before clicking the submit payment button. On successful payment, the user is redirected to the checkout complete page.

### Checkout Complete
The checkout complete page displays a message to indicate that the payment as been successful and the membership is active. The plan details are also summarised below. A 'Visit Profile' encourages the user to visit their profile since an account has automatically been created for them in the database upon successful checkout.

### Profile
The profile page is only accessible for authenticated users and appears as a navigable link in the navbar if the user is logged in. The plan the user has purchased appears in a summary box, including details about when the plan is valid for. Below this, the user can find their username and a link to chane their account password. They can also update their default billin information on directly on the page.

### Locations
The locations page renders an interactive map using the Google Map API. Users can see all of the locations where a Workbench can be access, which is a specification they need to make at checkout if they pick a one-off or standard plan. A call to action at the bottom of the page invites users to view the plans page.

### Contact
The Contact page renders fields which allows them to submit a question or enquiry to the site owner via the EmailJS API. All fields are required before the user can submit their message and an email is sent to the site email address with a reply email.

### Login
The login page displays in the navbar for users who are not authenticated. The page renders the django user login fields and a message indicating that only paying members are assigned an account. An option to choose a plan is given with the button to the plans page.

### Logout
The logout page displays in the navbar for users who are authenticated. The page renders a confrimation that the user wishes to log out and a log out button.


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
The site makews use of Javascript to provide an interactive experience for the user. The locations page features an interactive map powered by Google Maps API where a user can scroll and view the labels of all of the Workbench locations.

## Database Structure
The project features custom Django models in the plans, locations, checkout and profile apps. Each order model created at checkout is associated with a user model in the database via the userProfile foreign key, creating a relationship between the two entities.

#### Structure Overview

#### Field Relationships

### Features to Implement in the Future

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
- - **[Bootstrap](https://www.getbootstrap.com/)** - this project uses Bootstrap to optimise its layout and structure in the frontend.

### Libraries
- **[FontAwesome](https://fontawesome.com/)** - this project uses FontAwesome 5 to provide icons.
- **[Google Fonts](https://fonts.google.com/)** - this project uses Google Fonts to style the website's fonts.

### APIs
- **[EmailJS](https://www.emailjs.com/)** - this project uses EmailJS API to facilitate the sending of emails from users to site owner via to the Contact page.
- **[Google Maps API](https://www.emailjs.com/)** - this project uses the Google Maps API to render the interactive Javascript map on the Locations page.
- **[Stripe](https://www.stripe.com/)** - this project uses Stripe to facilitate e-commerce functionality in the site's checkout app.

## Testing

Testing information can be found in this [TESTING.md file](TESTING.md).

## Deployment

### Deployment to Heroku

### How to run this project locally

## Credits

### Inspiration

### Media

### Code

A complete county dropdown list was taken from [https://gist.github.com/olivertappin/4dcbf64e06aae132c12a8b9d302fae12](https://www.notion.so/4dcbf64e06aae132c12a8b9d302fae12)

This Stack Overflow thread helped disable the Django sign up view in the project: [https://stackoverflow.com/questions/29794052/how-could-one-disable-new-account-creation-with-django-allauth-but-still-allow/29799664#29799664]
