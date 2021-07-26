# Testing

[Back to README.MD file](#README.md)

## Table of Contents
1. [Testing User Stories](#testing-user-stories)
2. [DevTools](#dev-tools)
    * [Responsiveness](#responsiveness)
    * [Console Debugging](#console-debugging)

3. [Manual Testing](#manual-testing)

4. [Automated Testing](#automated-testing)
    * [Code Validation](#code-validation)
    * [Browser Validation](#browser-validation)
    
5. [User Testing](#user-testing)
    * [Mentor Review](#mentor-review)
    * [User Review](#user-review)

## Testing User Stories

1. As a new user, I want to find out about the subscription plans and facilities Workbench offers.
2. As a new user, I want to find out how much each Workbench plan will cost per month.
3. As a new user, I want to see where Workbench sites are located and where the nearest one to me is.
4. As a new user, I want to buy a Workbench subscription.
5. As a new user, I want to buy a one-off meeting room or office space session when I don't have a subscription.
6. As an existing user, I want to buy a one-off meeting room or office space session on top of my subscription.
7. As an existing user, I want to view my current subscription and personal details and be able to edit or cancel them.
8. As as a new or existing user, I want to make payments securely and easily on the website.
9. As an existing user, I want to be able to log in and log out of my account.

## DevTools

### Responsiveness

### Console Debugging

## Manual Testing

### Sitewide Features

### Home

### All Plans

### Individual Plan

### Checkout

### Checkout Complete

### Profile

### Locations

### Contact

### Login/Logout/Allauth

## Automated Testing

### Code Validation

This project used the [W3C Markup Validation Service](https://validator.w3.org/nu/) to validate HTML code. This identified several missing closing div tags, miss <td> tags for the checkout-complete table. Other warnings and errors could be safely ignored because they related to the use of templating in the html files, which are clearly a necessary part of this Django application. Absence of doctype was also an error raised, but as the application extends from base.html, this could also be safely ignored.

<img width="1680" alt="home-validated" src="https://user-images.githubusercontent.com/68863341/126988018-b6c6e931-b006-4b45-be80-f9a020def913.png">
<img width="1680" alt="plans-validated" src="https://user-images.githubusercontent.com/68863341/126988036-41453f3a-04a2-422d-8bd1-4fc818678cc7.png">
<img width="1680" alt="individual-plan-validated" src="https://user-images.githubusercontent.com/68863341/126988063-898e9307-fb5e-4b83-9cf6-c6112b5d0e7f.png">
<img width="1680" alt="checkout-validated" src="https://user-images.githubusercontent.com/68863341/126988074-ebd46913-9cb2-4bb9-811f-a48f8fefb72d.png">
<img width="1680" alt="checkout-complete-validated" src="https://user-images.githubusercontent.com/68863341/126988083-5c4a7f3f-c1f8-46c0-b027-04585d5b9b68.png">
<img width="1680" alt="profile-validated" src="https://user-images.githubusercontent.com/68863341/126988098-26e4c312-6f8e-4499-af6c-4278a82fb3fb.png">
<img width="1680" alt="locations-validated" src="https://user-images.githubusercontent.com/68863341/126988105-1786aaf2-72e0-4a6e-bfe6-5bf184853a95.png">
<img width="1680" alt="contact-validated" src="https://user-images.githubusercontent.com/68863341/126988109-8a00c6ce-bb37-4295-bee1-e0446c04d3c2.png">
<img width="1680" alt="404-validated" src="https://user-images.githubusercontent.com/68863341/126988120-90ff46d4-09b7-459d-bce6-95934e0446b4.png">
 
This project used the [JSHint](https://jshint.com/) website to validate Javascript code. The only issues which needed attention were missing semi-colons at the end of several lines.
<img width="1539" alt="googleMaps-validated" src="https://user-images.githubusercontent.com/68863341/126989195-7ba059be-f8d9-4b89-a01a-a8f09fa162a1.png">
<img width="1538" alt="sendEmail-validated" src="https://user-images.githubusercontent.com/68863341/126989204-e906d712-0cc2-48c3-8a5d-b021fb48d631.png">
<img width="1534" alt="stripe-validated" src="https://user-images.githubusercontent.com/68863341/126989440-c5cbf6de-77fd-409c-a010-a8b42df9d794.png">

This project used [PEP8 Online](http://pep8online.com/) to validate python code. Minor errors such as line to long were found.
   
<img width="1520" alt="PEP8-validation" src="https://user-images.githubusercontent.com/68863341/126990170-d1a7e5bc-4b8c-4246-b5a6-189c1c1e9c09.png">

### Browser Validation
   
Chrome - displays correctly:
<img width="1622" alt="chrome-display" src="https://user-images.githubusercontent.com/68863341/126996090-18d24a65-b259-4915-8872-4dd413b7253b.png">


Safari - displays correctly:
<img width="1459" alt="safari-display" src="https://user-images.githubusercontent.com/68863341/126996120-1d63c27d-a884-4ebe-8274-2844e30c1433.png">


[Autoprefixer CSS online](https://autoprefixer.github.io/) was used to add the necessary prefixers to CSS so that the live website renders across all other browsers.

### Device Validation

The live deployment of this project displays correctly on all of the following device types which were tested via DevTools:

- iPhone 5C
- iPhone 6/7/8
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone X
- iPhone 6/7/8 Plus
- iPad
- iPad Pro
- Laptop with touch
- Laptop with MDPI screen
- Laptop with HiDPI screen

## User Testing

### Mentor Review
My mentor, Seun, was very helpful with her feedback and suggestions when it come to reviewing this project. She made the following suggestions:
   - Reset email form once an email has been sent, as well as showing feedback to the user on screen about whether their message was successfully sent or not. I did this by checking the presonse codes in the page's Javascript are setting the HTML of an otherwise empty div to either a success or fail message.
   - Hide password characters! My checkout form was showing the password inputted by the user rather than indistinguisable dots. Seun found me [this helpful thread](https://stackoverflow.com/questions/24223654/django-crispy-forms-shows-password-as-clear-text) on how to achieve this when rendering the field through a crispy form template.
   - Suggested the user of Google Maps API rather than a static image map I had to begin with. This enhanced the user interactivity of the site and Javascript composition for a better looking site.

### User Review

