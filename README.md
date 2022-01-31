# LoveYoga

View the deployed site [here](https://loveyoga.herokuapp.com/ "LoveYoga")

## PROJECT INTRODUCTION
LoveYoga is a website designed to sell access to their selection of yoga class video series', and also to sell yoga equipment such as mats, blocks, and straps. LoveYoga welcomes both new users and return users, with all levels of yoga experience

![image of site mock-ups on various screen sizes](/media/mockup.jpg "Mock Up")
___

## **USER EXPERIENCE (UX)**

###  Strategy
 - **User Stories**

New Users

1. As a new user, I want to find out what the website offers
2. As a new user, I want to easily broswe the classes and products on offer
4. As a new user, I want to learn more about the yoga trainers
4. As a new user, I want to easily select items to buy
5. As a new user, I want to add be able to view and adjust the items in my basket
6. As a new user, I want to chekout my basket and recieve order confirmation
7. As a new user, I want the option to create a user account

Returning Users

1. As a returning user, I want to be able to log in to my account
2. As a returning user, I want to view my previous orders
3. As a returning user, I want to save my delivery details to my user profile

Admin Users
1. As an admin user, I want to be able to add, update and remove products and classes from the website
2. As an admin user, I want to be able to view the orders that have been placed

### Design

 - **Colour Scheme**

   - The site is a deisgned with calming neutral palate on a white background, with a bright pink for accents on action items. Primary buttons are all solid pink, whil other actions are white with a pink outline. Teal green is used for actions that are available to admin users only, for easy differentiation.
  ![colour palatte](/media/colour-palatte.jpg "Mock Up")
   
 - **Font**

   - Quicksand is used as the logo font, while Poppins is used for all other content, Both fonts from Google fonts.

- **Images**

  - All images taken from open source sites, or from free download allowance on subscription sites. The large hero image on the home page was chosen as a calming welcome to the site and to the practices of yoga. There is purposefully no tet of actions covering the image, inviting users to take a moment of pause and reflection before the enter the site.
  - Each class, product and trainer in the database requires a submitted image

### Wireframes

Wireframes showing the each page across small, medium and large screen sizes.

 |     Page   | Wireframe | Wireframe | Wireframe |
    | ----------- | ----------- | ----------- | ----------- |
    |Home Page     | [Large](/media/home-l.jpg) | [Medium](/media/home-m.jpg)   | [Small](/media/home-s.jpg)   |
    |About page   | [Large](/media/about-l.jpg) | [Medium](/media/about-m.jpg)   | [Small](/media/about-s.jpg)   |
    |Trainers/Classes/Shop page   |  [Large](/media/trainer_class_shop-l.jpg) | [Medium](/media/trainer_class_shop-m.jpg)   | [Small](/media/trainer_class_shop-s.jpg)   |
    |Class/Product Info  |  [Large](/media/class_product_info-l.jpg) | [Medium](/media/class_product_info-m.jpg)   | [Small](/media/class_product_info-s.jpg)   |
    |Basket  | [Large](/media/basket-l.jpg) | [Medium](/media/basket-m.jpg)   | [Small](/media/basket-s.jpg)   |
    |Checkout  | [Large](/media/checkout-l.jpg) | [Medium](/media/checkout-m.jpg)   | [Small](/media/checkout-s.jpg)   |
    |Checkout Success  | [Large](/media/checkout-success-l.jpg) | [Medium](/media/checkout-success-m.jpg)   | [Small](/media/checkout-success-s.jpg)   |
    |Profile  | [Large](/media/profile-l.jpg) | [Medium](/media/profile-m.jpg)   | [Small](/media/profile-s.jpg)   |


### Database Schema
Production databases stored in Heroku Postgres, while SQL lite used for development.

  ![Database schema](/media/DBschema.png "Database schema")
___

## **FEATURES**

###  Current Features

  - Navbar:
    - Full width header containing navbar links to all pages on the site.
    - "LoveYoga" logo is displayed at the centre of the navbar, with search input for yoga classes to the left, and 'My account" dropdown' and basket tracker to the right.
    - 'My Account' dropdown only shows 'Login' and 'Register' links to new users (or if signed out), once signed in, users can link to their profile page or log out. Admin users also have acess to site management here, with links to add classes/trainers/products
    -  The basket tracker displays 0.00 default, and displays a running total as items are added to the basket.
    - Below this header is a navbar with links to 'About Us', 'Trainers', 'Classes' and 'Shop' pages
    - Navbar collapses to hambuerger menu with dropdown menu to line links on smaller screens
- Footer with contact info and links to social media sites.
 - Home Page:
    - Large fullscreen hero image
- Authentication:
    - Provided by Django-AllAuth. Registration and Login/Logout pages allowing users to mage their site access, and rest passwords if required.
 - About us page:
    - Accessible to all users.
    - Provides users a description of the site and its purpose, with description and links to the main features.
- Trainers Page:
    - Accessible to all users.
    - A responsive grid of display cards for each trainer, containing trainer image, years practicing yoga, years teaching experience, trainer bio details, and a link to the classes page filtered for that trainers classes.
    - Admin users have access to edit/delete link for each trainer.
- Classes Page:
    - Accessible to all users.
    - A responsive grid of display cards for each yoga class, containing an image for each class, class name and price. Clicking  on the class image links to the class info page.
     - Above the grid there are dropdown links to filter by trainer or yoga practice, or to sort ascending/descending by name or price.
     - Admin users have access to edit/delete link for each class.
 - Classes Info Page:
    -Accessible to all users.
   - Class image is displayed on the left hand side, along with the class description if viewing on small/med screens
   - Right side dispays the class description on large screens, and class details on all screens(Practice, Trainer, Level, Intensity, session/Series length and equipment needed)
   - Below the class details section, the price is displayed in a larger font, along with a solid pink button to add the class to the shopping basket.
   - No qty selector is available, as customers should only purchase each class series once, they will be able to download and keep the class permanently.
   - When a class is added to the basket, a toast message is displayed on the top right of the screen, with a success message and a summary of the current basket.
   - If a class is already in the basket, an error message toast is displayed.
   - Pink-outline style button links below this section lead back to the classes page, or to the shop page.
- Shop Page:
    - Accessible to all users.
   - A responsive grid of display cards for each product, containing an image for each, name, price and description. Clicking on the image links to the product info page.
   - Above the grid there is an input to search the shop, or to sort ascending/descending by name or price.
   -  Admin users have access to edit/delete link for each class.
- Product Info Page:
   - Accessible to all users.
   - Product image is displayed on the left hand side of the screen.
   - Right side dispays the Product name, description and price.
   - Image and details section are stacked on small screens.
   - Below the  details section,there is a quantity input box, with -/+ buttons either side to adjust the qty to add to the basket.
   - A solid pink action button below adds the requested qty to the basket.
    - When a product is added to the basket, a toast message is displayed on the top right of the screen, with a success message and a summary of the current basket.
   - Pink-outline style button links below this section lead back to the shop page, or to the classes page.
 - Shopping basket:
    - Accessible to all users, byt clicking on the basklet icon in the navbar.
    - Displays all the items currently in the users shopping bag, divided into classes and products section.
    - Each line shows a small image, class/image name, description, price and qty, with a subtotal price.
    - Users can click the trashcan link to remove an item from the basket and the pencil icon to adjust the qty for products.
    - Below the class/product section, there is a basket subtotal, and a €5 delivery charge added only if the user is purchasing shop prodiucts.
    - The grand total is displayed at the bottom of the basket.
    - At the bottom of the page there is a large solid pink action button to go to the secure checkout.
    - In line with this button, there are 2 pink-outline buttons to take the user back to the classes/shop page for further purchases.
-Checkout Page:
    - Accessible to all users.
    - Screen is divided into left/right sections for med/large screens, and top/bottom sections for small screens.
    - The left/top section contains the user contact details and address entry form, and the Stripe card input. The form validation is throgh django-forms, and will not submit if any of the required inputs are blank or invalid.
    - If the user is logged in, there is a checkbox which will save the users address information to their profile if clicked.
    - If the user is not logged in, links are displayed to register or log in to save this information.
    - Card input validation is provided through Stripe.
    - The right/bottom section displays a summary of the basket items for purchase, similar to the basket page display, with pink-outline button links back to the classes and shop pages.
    - Below the Stripe card input there is a large solid pink button to complete the checkout. 
    - There is also a pink-outline secondary button to return to the basket to make any changes.
    - Below the complete order button, there is a red alert display confirming the total amount to be charged to the card.
- Checkout Success Page:
  - Toast message is displayed with the order confirmation number, and this is also displayed at the top of the page.
  - Order summary is displayed below, in the same style as the shopping basket.
  - Links at the bottom of the page guide the user back to the classes or shop page for further purchases.
- Profile Page:
    - Only accessible to users who are logged in to their account.
    - Screen is divided into left/right sections for med/large screens, and top/bottom sections for small screens.
    - Left/top section displays the saved contact details for the user. The user can amend the details, and submit the changes with the solid pink "update details" button below.
    - The right/bottom section displays the list of the previous orders made by the user, Each line contains the order number, order date, summary of items/qtys, and the order total.
    - The order number links back to a copy of the checkout success page for that order with a complete summary.
    
 - Site is fully responsive (using bootstrap and CSS) to adapt to all display sizes - mobiles,  tablets and large monitors/laptop screens.

 ____
 ## **Testing**
  - Full testing documentation found in separate file [TESTING.md](TESTING.md)

____
 ## **TECHNOLOGIES USED**

 ### Languages

  - [Html5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/CSS)
  - [Javascript](https://www.javascript.com/)
  - [Python](https://www.python.org/)

 ### Frameworks, libraries and tools used

  - [Bootstrap v5.02](https://getbootstrap.com/)
    - Bootstrap was used for navbar, grid layout, responsive layout, margins, padding etc on all screen sizes.
  - [JQuery](https://jquery.com/)
    - JQuery library used for JS scripts
  - [Django Framework](https://www.djangoproject.com//)
    - Framework used to create the Loveyoga apps, models, templates and views.(v3.2)
    - Django AllAuth (v0.41.0) for user profile authentication
    - Django Crispy Forms to render user input forms
  - [Stripe](https://stripe.com/en-ie)
    - Payment processing to handle the order payments
  - [SQLite](https://www.sqlite.org/index.html/)
    - Library to host the databases during development
  - [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql))
    - Library to host the databases for the deployed site
  - [Amazon Web Services](https://aws.amazon.com/?nc2=h_lg)
    - To host the static files and images for the deployed site.
  - [Gitpod](https://www.gitpod.io/)
    - Code was written in Gitpod, and version control was managed by commit and push to GitHub.
  - [GitHub](https://github.com/)
    - Used to store the project repository
  - [Heroku](http://www.heroku.com/)
    - Used to deploy the project
  - [Gunicorn](https://gunicorn.org/)
    - HTTP server for WSGI applications.
  - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - AWS SDK for Python
  - [dj-database-url](https://pypi.org/project/dj-database-url/)
    - To utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
  - [Gmail](http://www.gmail.com/)
    - Used to send the confirmation emails
  - [Font Awesome](https://fontawesome.com/)
    - Used to display social media icons.
  - [Google Fonts](https://fonts.google.com/)
    - Used to import the Josefin Sans font used throughout the site.
  - [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Used for testing code output, especially to view various display sizes during the site creation.
  - [Balsamiq](https://balsamiq.com/)
    - Wireframes were created using the balsamiq app.
  - [JPEGmini Pro](https://www.jpegmini.com/)
    - Used to reduce file size of images while preserving quality, to improve page loading times.
 - [Image Compressor](https://imagecompressor.com/)
    - Used to reduce file size of images while preserving quality, to improve page loading times.
 - [CSV to Json converter](https://csvjson.com/)
    - Used to create Json fixtures files from CSV data
 - [Moqups website mockup generator](https://websitemockupgenerator.com/)
    - Used to generate a mockup of the site on multiple devices
   ___


## **DEPLOYMENT**

#### Deployed using Heroku

- **Instructions**
  1. Open the [repository](https://github.com/annemarie293/LoveYoga) in GitHub, then launch in GitPod
  2. Ensure dj_database_url is installed, then migrate your models and load fixture files.
  3. Create new superuser for the app.
  2. Login or create new account on Amazon Web Services to host static files
  3. Create a new bucket, user and poilcy to host the static files and images.
  4. Upload images to the bucket.
  4. Login or create a new account on Heroku.
  5. Create a new app, choosing app name and region
  6. Choose "GitHub" as the deployment method, add your GitHub repo name and click search to connect.
  7. Before clicking "Enable automatic deploys" on the deploy tab, go to "reveal config vars" on the settings tab
  8. Update the "config vars" below config vars and the appropriate values
 ![config vars](/media/config-vars.jpg "Config Vars in Heroku")
  6. Return to "deploy" tab and click "Enable automatic deploys"
  7. Then click "Deploy Branch" to deploy your app.
  8. In Gitpod, connect to heroku, save all changes, commit and push to deploy the site.

#### Forking the Repository

- **Instructions**
  1. Open the [repository](https://github.com/annemarie293/LoveYoga) in GitHub
  2. Click on the “fork” button at the top right hand side of the page, just below the navbar.
  3. A copy of the original repository will be created to your own GitHub account.


#### Cloning the Repository

- **Instructions**
  1. Open the [repository](https://github.com/annemarie293/CellarClub)
  2. Click on the “code” button to the left of the green “Gitpod” button.
  3. To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard icon. 
  4. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the clipboard icon . 
  5. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the clipboard icon.
  6. Open Git Bash.
  7. Change the current working directory to the location where you want the cloned directory.
  8. Type `git clone`, and then paste the URL you copied earlier.

`
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
`
  9. Press Enter to create your local clone.

`
  $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
  > Cloning into `Spoon-Knife`...
  > remote: Counting objects: 10, done.
  > remote: Compressing objects: 100% (8/8), done.
  > remove: Total 10 (delta 1), reused 10 (delta 1)
  > Unpacking objects: 100% (10/10), done.
 `
 
  10. For more detailed info on this process please click [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

___

## **CODE**

#### Credits

This project was inspired by the Boutique-Ado project by Code Institue and their process was used as guide in setting up this App

#### Content
  - The descriptions and details for the yoga classes were adapted from [Glo Yoga website](https://www.glo.com/)

#### Media
- **The photos used in this site were freely obtained from below image sites (some using free trials):**

- [Adobe Stock](https://stock.adobe.com/)
- [Pexels](https://www.pexels.com/)
-  [Unsplash](https://unsplash.com/)
-  [Shutterstock](https://www.shutterstock.com/)
- [Frepik](https://www.freepik.com/)

#### Acknowledgements

   - I received inspiration for this project from our course material, and help with issues from the below resources:
     - [W3schools](https://www.w3schools.com/)
     - [Stackoverlfow](https://stackoverflow.com/)
     - [Mozilla developer](https://developer.mozilla.org/en-US/) 
     - Code Institute slack channel
     - Code Institue tutor support

   - Thanks also to my mentor Rahul Lakhanpal for all his help and support throughout this course