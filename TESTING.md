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

_1. As a new user, I want to find out about the passes and facilities Workbench offers._

The landing page for the Workbench website offers a comprehensive line to the user in large font at the top of the page. The types of passes are displayed in a visually appealing card format beneath this with links to more info about each one. The process of how to go about getting a Workbench pass is clearly set out below this, in a three part description. The 'Plan' tab also displays all of the types of passes to the user. Clicking on the 'select' button below each one will display all of the infomation about that particulart plan. No payment intent has been created for the browsing user at this point, and they can always navigate away using the 'All Plan' back button.

_2. As a new user, I want to find out how much each Workbench pass will cost._

Each individual plan page displays the price of the respective plan, easily identifiable by the red '£' icon. On the checkout page, the price for the selected plan is also display on the plan details and order summary section, as well as below the checkout button to warn the user how much their card is about to be charged.

_3. As a new user, I want to see where Workbench sites are located and where the nearest one to me is._

The 'Locations' tab displays all of the Workbench locations across the UK using the Google Maps API. The user can interactive with the map by zooming in and out and dragging the view using their cursor. The use of cluster markers ensures that, when zoomed out, the map does not look too 'busy' for the user to make sense of.

_4. As a new user, I want to buy a Workbench pass._

The website creates a smooth process for the user from browsing to checkout. For the homepage or the 'Plans' tab, the user can click through to more information about an individual plan, an if they click continue, they are presented withe the checkout page which includes a comprehensive display of all of the details about the plan they are intending to purchase. This transition process from browsing to checkout was modelled off of [WeWork's](https://www.wework.com/) checkout process; it feels like a much more intuitive process and better suited to the service on offer than a checkout 'bag' since it is not material goods being sold.

_5. As a new user, I want to buy a one-off meeting room or office space session rather than a pass._

The 'Plans' tab clearly displays the option for a user to purchase a one-off pass rather than a month pass by dividing the two types into two separate sections. At each stage of the checkout process on post-checkout on their profile, the 'plan type' is also displayed for the user. 

_6. As an existing user, I want to view my current pass and personal details and be able to edit or cancel them._

Once a user has made a purchase, they now have a user profile in the database and can now log in to the site as a member. The 'Profile' tab displays all of the details about the plan they have purchased as well as their default billing information. This information can also be updated from here, using the fields and 'Update Info' button.

_7. As as a new or existing user, I want to make payments securely and easily on the website._

The user can fill out all of their details on the checkout page and securely checkout via Stripe. Webhooks ensure the order will always be placed in the database when a payment has succeeded, regardless of the user exiting the browser prematurely etc.

_8. As an existing user, I want to be able to log in and log out of my account._

All users who make a purchase are automatically logged in to the member-only side of the site on completion of payment. They can then use their choosen password and assigned username (their first and last name combined with the last 4 digits of their phone number) to login in the future. The use of Django's authentication system ensure this is a secure process, making sure a user confirms their email address and can reset their password if necessary. Usernames and full names cannot be changed for security.

## DevTools

Making good use of browser DevTools was an important part of building this website. Experimenting with HTML and CSS without changing the actual files, for example, padding, margin and position values, was a very useful resource to have. Reloading DevTools and the original code in the browser is far easier then having to restore a file in my IDE terminal.

### Responsiveness

This project uses Bootstrap as a frontend framework for building a responsive layout. Responsiveness was tested in DevTools by viewing the website on every screen size, the smallest being an iPhone 5C and the largest being a laptop with HiDPI screen. Multiple media queries for each screen size are set out at the end of my base.css file, located in the static folder.

### Console Debugging

Viewing the console in DevTools was a useful way to debug code. For example, when I was having trouble display my Google Maps API, I could access the console and see that it was because the current web address did not have permission to make call to the API, as set out in my Google Console.

<img width="644" alt="console-debugging-example" src="https://user-images.githubusercontent.com/68863341/127141460-7b35bb11-3734-485b-a317-7363861ad251.png">

## Manual Testing

### Sitewide Features

- The favicon displays in the browser tab correctly on all pages.
<img width="251" alt="favicon-testing" src="https://user-images.githubusercontent.com/68863341/127141842-c77dac38-8216-4433-8c14-57b1dcc86ae4.png">

- The navbar displays the appropriate links and collapses into a burger icon with a dropdown list on smaller screens.]

<img width="605" alt="navbar-testing" src="https://user-images.githubusercontent.com/68863341/127141939-a3b40451-cc08-4318-9922-118e0831c037.png">

- A customised 404 page displays when a random url is entered. This confirms that debug is set to False for the deployed site.

<img width="768" alt="404-testing" src="https://user-images.githubusercontent.com/68863341/127142202-9c42fcca-aa0c-4161-9626-2d4c42b416da.png">

- The footer displays consistently on all pages.

- The homepage can be returned to on any page by clicking the navbar-brand link in the top left.

### Home

- The links to each plan all render an individual plan page correctly and the locations link renders the locations page.

<img width="1195" alt="homepage-plan-links-testing" src="https://user-images.githubusercontent.com/68863341/127142653-65d09be7-2d02-4fb5-9af0-37d6c6b74fb8.png">

- The Workbench service instructions display with uniformity and expand to full width each on small screens.

<img width="810" alt="homepage-three-steps-testing" src="https://user-images.githubusercontent.com/68863341/127142927-54fb6b20-3951-4920-8860-082cc8202ead.png">

- The 'Find A Plan' button takes the user to the Plans tab.

<img width="1097" alt="homepage-allplans-button-testing" src="https://user-images.githubusercontent.com/68863341/127143116-9e51cbba-f4c4-44ff-b370-9d383a51d51b.png">

### All Plans

- Each select button below each below type returns the individual plan page corresponding to that specific plan.

<img width="1467" alt="all-plans-select-button-testing" src="https://user-images.githubusercontent.com/68863341/127143561-440157fc-c9a0-4fc9-9f57-3e775849dc87.png">

- The card elements collapse and expand based on screen size correctly and in a layout which is easy to read and navigate.

### Individual Plan

- Each plan page displays the correct information for the selected plan. Icons make the information quick and easy to read.

<img width="927" alt="individual-plan-display-testing" src="https://user-images.githubusercontent.com/68863341/127144222-e38ccd84-3841-4ceb-b395-a4d5b26cf6d1.png">

- The 'All Plans' button takes the use back tot he plans page and the 'Continue' button takes them to the checkout page.

<img width="1343" alt="individual-plans-buttons-testing" src="https://user-images.githubusercontent.com/68863341/127144451-de57bcad-3ef3-4dc4-8bf3-7c427bad9a5b.png">

### Checkout

- The checkout page displays the informations about the selected plan and a summary for the purchase the user is about to make. This test revealed that the  price in the plan details was missing a currency sign.

<img width="1404" alt="checkout-plan-details-testing" src="https://user-images.githubusercontent.com/68863341/127144701-3ef897b5-de40-4360-8dc4-f39461a2085c.png">

- All of the form fields display correctly and indicated that they are all required if the user trys to leave any blank.

<img width="1396" alt="checkout-form-validation-testing" src="https://user-images.githubusercontent.com/68863341/127145202-e7cd7623-71fa-4cc2-a547-673615ab4e8b.png">

- The password field hides the input for security.

<img width="741" alt="checkout-password-testing" src="https://user-images.githubusercontent.com/68863341/127145331-1fbf5c84-593a-4e1d-9e1c-9162d993211e.png">

- The Stripe element turns red if the card number is invalid and the amount which is about to be charged displays below the complete button.

<img width="738" alt="checkout-payment-input-testing" src="https://user-images.githubusercontent.com/68863341/127145557-75f29b20-a23c-416a-8f9f-617d73b14a41.png">

### Checkout Complete

- The checkout page redirects the user to the checkout-complete page upon successful payment and order placement. The unique order id and where a confirmation email is being sent to is displayed a username details in the content of the page.

<img width="1288" alt="checkout-complete-orderid-testing" src="https://user-images.githubusercontent.com/68863341/127145961-415d9d67-85e7-4768-b2b9-2fe58bdc9e5e.png">

- The website now displays the authenticated side of the site by automatically logging in the user. A logout button now displays in the top right and a profile tab now appears in the navbar. The visit profile button in the page content takes the user to this profile page.

<img width="1402" alt="checkout-complete-loggedin-testing" src="https://user-images.githubusercontent.com/68863341/127146252-6768a865-bdbc-4201-a401-9bd0501944ba.png">

- The order summary box displays the correct plan information from the order the user has just placed.

<img width="1343" alt="checkout-complete-order-summary-testing" src="https://user-images.githubusercontent.com/68863341/127146416-bfd287f7-9d0f-4676-a748-6a3e76b69fa5.png">

- The new user has a user profile in the database.

<img width="1472" alt="user-profile-db-testing" src="https://user-images.githubusercontent.com/68863341/127146807-57e506ef-51bf-4fd2-b031-8e412ea5280d.png">

- The order is displayed in the database with the correct user profile assigned to it.

<img width="903" alt="order-db-testing" src="https://user-images.githubusercontent.com/68863341/127146829-100fd273-94ff-4675-9759-b7e394752ce3.png">

- The payment is marked as successed in Stripe and for the correct amount.

<img width="1190" alt="stripe-payment-testing" src="https://user-images.githubusercontent.com/68863341/127147150-1d68d925-52d2-4439-b61b-fcf175e05fff.png">

- The webhooks for the payment have a status of 200.

<img width="1187" alt="stripe-webhooks-testing" src="https://user-images.githubusercontent.com/68863341/127147238-7dfda4cb-1285-4232-b2be-143e35650ff5.png">

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

