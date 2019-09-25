# A hearing aid E-Commerce website where you can purchase your first or next hearing aid.

[![Build Status](https://travis-ci.org/Bren08/Hear-to-Hear.svg?branch=master)](https://travis-ci.org/Bren08/Hear-to-Hear)

# "Hear to Hear" Milestone Project 4
For my Django Full Stack Milestone Project 4, I have created a website called “Hear to Hear”.  This website is an E-Commerce website where end-users can purchase hearing aids and their associated accessories. To partake within the secure area of the website the user must be registered and logged in. They make their order and proceed to the checkout. Once they have entered the required payment details they will be notified by an alert message that states how the payment process went. Unregistered users can just browse through the products list. 

## UX
The main demographic for this type of website would be people of an assorted age range according to their requirements or needs. Many people can aquire a hearing loss, young and old there is no one fast rule where to say, If you are old you tend to be possibly deaf or hearing impaired, but hearing loss can affect anybody fro any age. The website is designed to have a blue/grey tranquil set up so it is not "in your face", easy to navigate, esy on th eye and the action buttons are easily identifiable, especially for the old or infirm as their eyesight may not be too good.

A typical user of this app would be looking for the following: 

### User stories

<ul>
<li><strong>As an older person who is not used to navigating websites: </strong>They will require a simple interface for them to navigate and easily find their way through the website. They will need to know immediately what options are available to them and what the website has to offer.
</li>
<li><strong>As an end user: </strong> I would be immediately looking to see the different type/designs of hearing aids that are currently available and with a vast array of products on view it makes the decision easier to purchase.
</li>
<li><strong>As a registered user: </strong>I will want to have secured access to the website. So I know for sure and have confidence that my personal details are kept secure. I can see the various costs are well displayed and as a purchaser it makes my choice easier.
</li>
<li><strong>As a user looking for further information: </strong> There is a contact us area for further information and advice regarding the products that are on sale or general hearing impaired issues. You just enter your details and your request will be dealt with.
</li>
</ul>


## Features
<ol>
<li><strong>Navigation bar: </strong>This provides highlighted link choices on every page for easy navigation and takes the end-user to their desired location.  
</li>
<li><strong>Home Page: </strong>On first landing on the website, the user sees some people who are laughing and joking and gives the homepage a nice natural feeling. From here, the navigation is visible and there is a link from the homepage to the products page withough having to navigate to the navigation bar. Here a new user can register or login from this area and continue to browse through the website.
</li>
<li><strong>Hearing Aids: </strong>Here the user can browse through the various products on offer. To complete a purchase the user will have to register or a returning user will be required to login to complete their purchase</li> 
<li><strong>Register: </strong>This is where the new user can submit their details so they can register and then go on to purchase a hearing aid or an accessory.</li>
<li><strong>Login: </strong> From here a registered user can log in to the website and continue to purchase a product. On the login page there is also a link to aquire a new password if you have forgotten your one.
</li>
<li><strong>Logout: </strong> From here a registered user can logout from the website. This view is only possible when a logged in user is active within the website.
</li>
<li><strong>Accessories: </strong> Here the logged in user can purchase some accessories to go with their new hearing aids, it is possible to utilise different add-ons that are compatible with the desired device of choice.. but even if you just need some batteries they are aslo there for purchase.
</li>
<li><strong>Checkout: </strong>Displays the proposed order and it's amount. From here the user can still decide not to purchase and empty their cart or amend it if they see fit to do so, again this is if the user is logged in, if not, they are reverted to the login page.
</li>
<li><strong>Shopping Cart: </strong>This area holds the users choices of purchase until they proceed to the checkout area to complete their transaction. Once the choices have been made the Cart then is populated by the product choices and they sit there until the user wants to checkout or amend their choices or if they would like to remove their items from the Cart. If you are not logged in choosing to checkout will revert the user back to the login page.</li>
</ol>

### Features Left to Implement

Due to lack of time remaining the following features were not implemented:
<ul>
<li>Pagination</li>
<li>Linking product info to open on a new html page that displays the information for just one product, which may improve UX</li>
<li>A cart order list and shipping facility</li>
</ul>

## Technologies Used

* [Visual Studio Code](https://code.visualstudio.com) - Used to build this project.
* [GitHub](https://github.com/) - Version control system to host my code using Git.

#### Front-End 

* [HTML5](https://en.wikipedia.org/wiki/HTML) - Used as the base for markup text.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used as the base for cascading styles.
* [JQuery](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
* [Bootstrap](https://getbootstrap.com/) - Used as the front-end framework for layout and design.
* [Stripe API ](https://stripe.com/docs/api?lang=python) - Used to make secured payments at the checkout.
* [Whitenoise](http://whitenoise.evans.io/en/stable/) - Simplified static file serving for Python web apps.

#### Back-End 

* [Python](https://www.python.org/) - Used as the back-end programming language.
* [Django 1.11.23](https://docs.djangoproject.com/en/1.11/) -  Used as my Python web framework.
* [Heroku](https://www.heroku.com/) - Hosts the deployed version of this project.
* [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.

## Testing
All pages have been tested on all screen sizes. This has been done via Google Chrome developer tools and by testing on my own personal phone and tablet.
Also all features of the page are scaling as intended in tablet and mobile devices.

I checked the registration form to see if an error occurred when entering an existing username or email, and the form validations reacts as expected.
Also, if the confirmation password1 does not match the password2, it will cause an error. I made sure that the login form
will cause an error if the username and password entered are not registered in the database.

I also checked to see if the number next to the cart is updated when a product is added or removed. 

The Stripe payment function has been verified and all transactions show up on the Stripe dashboard.

All links and forms are verified to be working correctly via manual testing.

* [Travis](https://travis-ci.org) - Is being used to monitor the build of the website/app.

breakpoint() was my friend also throughout this build it came in very handy as a python debugger through many sleepless nights!

Most of the testing for this app was done manually. I find as I start building I am constantly testing each feature and intentionally trying to find fault or break the app. I find this a very effective way to test.

## Deployment

A live version of the site is here [Hear to Hear](https://hear-to-hear.herokuapp.com)

To run this project locally you will need the following to be installed:

- Python3 to run the application.
- PIP to install all app requirements.
- Any IDE. I used Microsoft Visual Studio Code.
- GIT for version control.

Here are the steps for local deployment:

- Clone or download this repository by clicking the green 'Clone or download' button and unzipping the file that is downloaded, or you can enter the following into your Git CLI terminal:
    - `git clone https://github.com/Bren08/Hear-to-Hear.git`  

- Install all requirements from the requirements.txt file using this command:
    - `pip3 -r requirements.txt`

- Create an environment variable on your machine or in a `env.py` file for your 'SECRET_KEY', remember to reference the `env.py` file in a `.gitignore` file. The key and value pair will be:
    - SECRET_KEY : `'Your secret key value'`.

- Sign up for an account on [Stripe](https://stripe.com) a payment processing platform. Once you have created an account you have access to your API test keys: Publishable key and Stripe Secret key. Place these in your `env.py` file. The key and value pairs will be:
    - STRIPE_PUBLISHABLE : `Publishable key`.
    - STRIPE_SECRET : `Secret key`.

- Now you can run your application using the following command in your CLI:
    - `./manage.py runserver`

- Once you have run the application for the first time a `db.sqlite3` file will be created remember to reference this on your `.gitignore` file.

- Make migrations to create the database schema by running the following commands:
    - `./manage.py makemigrations`
    - `./manage.py migrate`

- To access the Django Admin Panel, you must create a superuser:
    - `manage.py createsuperuser`   

- Add `'127.0.0.1'` to Allowed Hosts in settings.py.

- Now you can run your application again using the following command in your CLI:
    - `./manage.py runserver`

- The app should now be running on *local host* `http://127.0.0.1:8000/`. Copy and paste this into a browser of your choice.     

### Deployment Hosting

- Sign up for an Heroku account and create a new app.

- Click on the resources tab and go to Add-ons, search for Postgres and install the remote database.

- Click the Deploy tab, click on Connect GitHub, and Enable Automatic Deployment. When you push your code to GitHub Heroku will automatically deploy your project. 

- In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:
    - SECRET_KEY : `Your Secret Key`
    - STRIPE_PUBLISHABLE : `Your Stripe Publishable Key`
    - STRIPE_SECRET : `Your Stripe Secret`
    - DATABASE_URL : `Postgres database key from heroku`
    - EMAIL_HOST_USER : `EMAIL_ADDRESS`
    - EMAIL_HOST_PASSWORD : `EMAIL_PASSWORD`

- Once you have done this make migrations to create the database schema for Postgres by running the following commands:
    - `./manage.py migrate`

- Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: gunicorn hear_to_hear.wsgi:application`

- Commit and Push your code to GitHub.

- Go back to Heroku and your application should be successfully deployed. If it is not deployed successfully check the logs.

### Media:

Most of the images are taken from Google images. 

### Disclaimer:
*This project is for educational purposes only*

## Acknowledgements

I would like to thank everyone on the Code Institute Tutor team, the Slack Channels and most of all my mentor Spencer Barriball, who has directed me in the right direction on every topic we discussed regarding my projects.