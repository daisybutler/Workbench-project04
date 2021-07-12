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


- **Colours**
    - #FFFFFF white (background)
    - #F7F7F7 light grey (backing contrast)
    - #D91F44 warm red (accent)
    - #EEECE7 warm beige (backing contrast)
    - #313131 black (footer, popups)
    
- **Fonts**
    - Headings - Open Sans semi-bold 600
    - Paragraphs - Open Sans regular 400

### Wireframe Mockups

## Features

### CRUD Functionality

### Payment Functionality

### Interactive Features

## Database Structure

#### Structure Overview

#### Field Relationships

### Features to Implement in the Future

## Technologies Used

## Testing

Testing information can be found in this [TESTING.md file](TESTING.md).

## Deployment

### Deployment to Heroku

### How to run this project locally

## Credits

county dropdown list [https://gist.github.com/olivertappin/4dcbf64e06aae132c12a8b9d302fae12](https://www.notion.so/4dcbf64e06aae132c12a8b9d302fae12)
