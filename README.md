# BMDESIGNS

## E-Commerce store for personalised items.
------------------------------------

![Image showing Website on different devices]()

[View the live site here](https://milestone-project-4-bmdesigns-bfbe9959c9ae.herokuapp.com/)

BMDesigns is a small craft business specializing in personalised items.

BMDesigns is a fully functional E-Commerce store built in Django using Python, JavaScript, CSS, Bootstrap5, HTML and it incorporates stripe payments.
The site includes user authentication and Full CRUD functionality for products.

## Table of Contents

- [**Project Goals**](#project-goals)
- [**User Experience UX**](#user-experience-ux)
- [**Wireframes**](#wireframes)
- [**Features**](#features)
- [**Technologies**](#technologies)
- [**Testing**](#testing)
- [**Deployment**](#Deployment)
- [**Credits**](#credits)
- [**Acknowledgements**](#acknowledgements)

## Project Goals

The main aim of the site is to give users a lace to but personalised items.

The target audience is anyone wanting to buy items for themself or as a gift.

This version has been built for project 5 of the Code Institute Diploma in Software Development and therefore doesn't accept real payments and any orders made won't be fulfilled.

If you would like to test the payment functionality please feel free to do so by entering the card details below when prompted:

`Card number: 4242 4242 4242 4242  Exp: any future date eg. 11/26 CVC: any 3 digits eg 123`

### User goals

* Enjoyable experiance on the site.
* To be able to create an account.
* Easily login and logout.
* Recieve email confirmation after registering.
* To be able to customize my account.
* View a list of products.
* View individual product details.
* Easily view total of purchases.
* Search for a product.
* Easily select a size and quantity.
* View items in my bag to be purchased.
* Adjust the quantity of items in bag.
* Easily enter my payment information.
* View an order confirmation after checkout.
* Recieve email confirmation after checkout order.

### Developer goals

* Create a clean responsive interactive website for milestone project.
* An easy to navigate site.
* A project that would be good enough to go in a portfolio.
* A site to sell products.
* To provide the site owner with a place to showcase work and expand there digital presence.
* To add products.
* To edit/update products.
* Deete a product.

## User Experience - UX

### Scope

#### Potential/Existing User Stories

- User Sign in or Sign out
	* User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can avail of the sites full functionality
	* Receive Welcome Emails - As a user I would like to receive a welcome email upon signing up
    * Reset password Functionality - As a user I would like to be able to reset my password to keep my account safe
    * Visibly logged in or out - As a user I would like to know if I am logged in or not

- Landing page
	* As a User I would like to be brought to the landing page upon first visiting the site so that I can see what options are available to me
    * As a User from the landing page I should clearly be able to see and navigate the navbar
    * As a User on the landing page I should be easily able to go straight to the shop and purchase an item

- View Products, Admin CRUD
    * As a user I should be easily able to see a list of products available.
    * As a user I should be able to click on any item to see more information about it.
    * As an Admin I can add products to the database
    * As an admin I can edit products in the database
    * As an admin I can delete products from the database

- Shopping Cart
    * As a user I can easily view the contents of my Cart
    * As a user I can easily add/edit/delete the contents of my Cart
    * As a user I can easily identify the total cost of my Cart

- User Feedback/Confirmation
    * As a user I receive prompt feedback concerning my activity on the site
    * As a user I can see a order confirmation message
    * As a user I receive an order confirmation email

- Payment Feature
    * As a user I can visit a payment screen
    * As a user I can input my credit/debit card details

- User Profile
    * As a user I can sign in/create a profile so that personal information can be stored.

- Social links
    * As a user I can easily find social media links and when pressed they take me to the correct site.

- Customer Reviews
    * As a user I can clearly see reviews left by past customers.

### Design Choices

#### Fonts

* The fonts used were taken from [Google Fonts](https://fonts.google.com/)
* The fonts Roboto and Lato were used because they are popular and therefore more recognisable.

#### Icons

* Icons used were taken from [Font awesome](https://fontawesome.com/)
* All icons used were chosen because they are easily recognisable to clients.

#### Colours

![Colour Palette image]()

* The primary colour choices of white and grey were chosen for the navbar and background because they have a clean clear aspect while contrasting well with each other, the grey overlay was taken from the logo.
* Black, grey and white were chosen to make the writing stand out against the background.

#### Styling

* I have used Materialize throughout the site primarily to assist with design and responsiveness and added my own custom styling.

#### Images

* The logo and products were given to me by a family member who sells personalised items on facebook.
* The social media links are credited in the credits section.

## Wireframes

Wireframes for the project were developed after the idea was scribbled on a piece of paper, the program used being Figma.

## Features

The ecommerce website is designed to strictly adhere to accessibility guidelines across all pages, with easy navigation between them. Device responsiveness approach taken throughout project. The plan for this project was carried out using the Agile Methodology in Github.

### Front-End Structure

#### Navbar and Footer

* The navbr and footer were taken from materialize and styled to suit needs. The same navbar and footer used on every page for easy navigation. Added social media links to the footer.

The website is split into 6 apps each with there own html, models, views urls and forms. A number of other folders and files were used for allauth, css and media.

1. Home - index.html
- Landing page, and first page user encounters when they visit the website, includes a link to the products page.


2. Log In - signup.html
- The user is able to log in to the website using an existing account, otherwise they are invited to create a new one. Once logged in they are redirected to the home page.


3. Profile - profile.html
- Available only to the user logged in via which they can view their account info, provides links via which user can change their profile info.


4. Update Profile - update_profile.html
- Available only to the user logged in, allows user to change edit their account details.


5. Products - products.html
- A page where users can see all products.


6. Product Detail - product_detail.html
- A page where users can select a product and see all details aswell as sizes and quantity.


7. Add Product - add_product.html
- Only available to superusers so they can add new products.


8. Edit Product - edit_product.html
- Only available to superusers so they can edit existing products.

9. Bag - bag.html
- A page where users can see the products thet have selected to buy aswell as the total cost.


10. Checkout - checkout.html
- A page where users can fill in there personal details and complete an order.


11. Checkout Success - checkout_success.html
- A page where users can see there order confirmed.


### Back-End Structure

#### Physical Database Model

Below model displays all fields stored in the database collection.

There are
- Order - stores users details.
- OrderLineItem - stores product order details.

