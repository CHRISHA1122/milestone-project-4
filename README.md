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
* Delete a product.

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

* I have used Bootstrap throughout the site primarily to assist with design and responsiveness and added my own custom styling.

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

There are 8 individual models in 3 apps
- Category - stores all categories.
- Color - stores all colour options.
- Product - stores product data.
- CustomizableProduct - stores all customizable product details.
- Order - stores users details.
- OrderLineItem - stores product order details.
- UserProfile - stores profile data.
- UserProfile - stores profile data.

![Physical Database Model]()

* Built with Django using Postgresql and AWS for the database.
The application structure is as follows:
* bm_designs - contains all main set up for the website.
* home - contains all index/home content for the website.
* products- contains all product content for the website.
* profiles - contains all profile content for the website.
* bag - contains all bag content for the website.
* checkout - contains all checkout content for the website.
* templates - contains all base.html and allauth files for the website.
* static - contains all css, js and images for the website.
* media - contains all images for the website.
* Application is created and setup by running python3 manage.py runserver.

Additional gadgets used in back-end:

* django-allauth
* django-countries
* django-crispy-forms
* django-storages
* gunicorn
* stripe
* Pillow

## Technologies

### Languages

This project was built using [HTML5](https://en.wikipedia.org/wiki/HTML5),[CSS3](https://en.wikipedia.org/wiki/CSS) and [JS](https://www.javascript.com/) using a link from [Python](https://www.python.org/).

### Frameworks

Here is a list of the following technologies used in this project:

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
HTML 5 was used to create the structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS)
CSS 3 was used to style the website.
- [JS](https://www.javascript.com/)
JS was used to give interactivity.
- [Python](https://www.python.org/)
Python was used for its database mechanics.
- [SQLAlchemy](https://www.sqlalchemy.org/)
 SQLAlchemy was used for its database mechanics.
- [AWS](https://aws.amazon.com/)
 AWS was used for its database mechanics.
- [GitHub](https://github.com/)
GitHub was used to store the projects code.
- [Gitpod](https://gitpod.io/)
Gitpod terminal was used to commit my code using Git and push it to Github.
- [Heroku](https://heroku.com/)
Heroku was used to deploy the project.
- [Bootstrap](https://getbootstrap.com/)
Bootstrap was used for its easy design and responsiveness.

## Testing

### Browsers


### Mobile

### HTML Validator

### CSS Validator

### JS Validator

### Python Validator

### Manual Testing

### Bugs

### Future Updates

## Deployment

### Github

To clone this project into Github you will need:

1. A Github account.
2. Install the Gitpod extension.
3. Log into Gitpod with your Github account.
4. On the GitHub website find and click on the [Github repository](https://github.com/CHRISHA1122/milestone-project-3) of intrest.
5. Locate the green button named Gitpod in the top right corner of the repository and click on it,
6. This will trigger a new Gitpod workspace to be created from the code in Github where you can work locally.

### Heroku

1. In app.py file, ensure that debug is not enabled, i.e. not set to True.
2. Create a plan file with no extensions called 'Procfile' in the root directory of your project (if it doesn't already exist), within it add the line 'web: python app.py' (essentially same thing we do when we run our program locally).
3. Create a requirements.txt file by running the command the following command in your terminal:
- `pip freeze --local > requirements.txt`
4. Procfile and requirements.txt files should both be committed to your Git repository.
5. Create an account on [Heroku](https://signup.heroku.com/login?redirect-url=https%3A%2F%2Fid.heroku.com%2Foauth%2Fauthorize%3Fclient_id%3D8ba4d6bc-6d8c-4de8-8d31-9e540595c199%26redirect_uri%3Dhttps%253A%252F%252Fdevcenter.heroku.com%252Fauth%252Fheroku%252Fcallback%253Fback_to%253D%252F%26response_type%3Dcode%26scope%3Didentity%26state%3D5627683e234758322a2e4a8ae45f254b4883a8266b26975c).
6. Create a new application and name it same as your project (if name is available, if not choose one).
7. In the application dashboard, navigate to the 'Deploy' section.
8. Link your GitHub account in the Deployment method section, then in the 'App connected to GitHub' select your project repository. Enable automatic deployment if desired, otherwise deployment will need to be manually done.
9. Next, configure your 'Config Vars'. Those should contain sets of key-value pairs of the keys you have stored in your local env.py, such as:
  - IP
  - PORT
  - SECRET_KEY
  - MONGO_URI
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
10. Go to the project dashboard and in 'Manual Deploy' section select the correct branch, then click 'Deploy Branch' button.
11. This will trigger the site's deployment. Once deployment has completed, click on the "Open App" button to open the deployed application.

If the above steps have been followed correctly you will be greeted by your website's landing page.

### ElephantSQL

1. Navigate to ElephantSQL.com and click “Get a managed database today”.
2. Select “Try now for FREE” in the TINY TURTLE database plan.
3. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account.
4.  Create new team:
 - Add a team name (your own name is fine)
 - Read and agree to the Terms of Service
 - Select Yes for GDPR
 - Provide your email address
 - Click “Create Team”
 -You should get a message saying Your account is successfully created!.
5. Click “Create New Instance”.
6. Set up your plan:
 - Give your plan a Name (this is commonly the name of the project).
 - Select the Tiny Turtle (Free) plan.
 - You can leave the Tags field blank.
7. Select “Select Region”.
8. Select a data center near you.
9. Then click “Review”.
10. Check your details are correct and then click “Create instance”.
11. Return to the ElephantSQL dashboard and click on the database instance name for this project.
12. In the URL section, clicking the copy icon will copy the database URL to your clipboard you will need it for the heroku set up.

## Credits

### Code

### Images

## Acknowledgements

* I would like to thank the [Code Institute](https://codeinstitute.net) for the learning material and all the other support on offer.
* I would like to thank my mentor for all the help and guidence through the project.


