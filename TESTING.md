## **TESTING**

### Validation

HTML Validation
- Errors found during testing:
    - There were some missing 'alt' attributes on image fieds, some duplicate IDs and a trailing closing div tag. '
    - There was also an as the hidden "thead" for the basket/order summary did not contain the required 5 'td' cells as used in the rest of the 'tr' rows.
    - The remainging warning is an empty H1 div for the stripe overlay spinner
 - [W3C Markup Validator](https://validator.w3.org/) 

CSS Validation
- No errors found
 - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
 
JS Validation
- Javascript validation carried out using [JS hint](https://jshint.com/)
 - Stripe-elements.js file, only some errors from JQuery $ signs, and some warnings on using template literals in ES6

PEP8 compliance
Python validation carried out using [PEP8 checker](http://pep8online.com/)
- No errors, only some "blank line contains whitespace" warnings that I wasn't able to remove

 ### User Stories Testing

  - **New Users**

1. As a new user, I want to find out what the website offers
    1. New users can acess the 'About' section from the Navbar, from any page on the site, which explains the mission of site and how to use it.
2. As a new user, I want to easily broswe the classes and products on offer
    1. The links for classes and the shop can be found on the navbar from anywhere on the site.
    2. There is also links to the shop page on the class info page, and vice versa.
    3. There is a search bar for classes on the navbar to search terms found in class names/descriptions.
    4. On the classes page, users can filter by preferred trainer or practice, and sort by price or name,
    5. On the products page, users can also search the shop for specific terms, and sort by name or price.
4. As a new user, I want to learn more about the yoga trainers
    1. Users can access the trainers link from the navbar anywhere on the site, or through the About page
    2. On the trainers page, users can browse through the trainer team and read their bio information.
4. As a new user, I want to easily select items to buy
    1. Users can browse through the classes and shop as above, and select an item to view more information.
    2. On the info page, there is a prominent "Add to Basket" button to select for purchase.
5. As a new user, I want to add be able to view and adjust the items in my basket
    1. Each time a user adds an item to their basket, a toast message is displayed show the items and qtys in their basket.
    2. Users can access the basket from any page via the link on the navbar.
    3. On the basket page, users can remove items by clicking on the red trashcan icon, or adjsut the qty of the products with the green pen icon.
6. As a new user, I want to checkout my basket and recieve order confirmation
    1. From the basket page, or from the basket toast message, the user can follow the "secure checkout" link to the checkout page
    2.  The user can quickly complete their contact details, address and card information
    3.  The user can finally click the "complete order" button to complete the process, and be redirected to the checkout success page to view their order confirmation details.
7. As a new user, I want the option to create a user account
    1. Under the "My account" dropdown on the navbar, the user can access the 'register' link to create their user account and profile on the site

 - **Returning Users**

1. As a returning user, I want to be able to log in to my account
    1. Returning users can access the 'login' link from the "My Account" dropdown on the navbar.
    2. Once logged in, they will be able to see the link for "My Profile"
2. As a returning user, I want to view my previous orders
    1. On the users profile page, they can find a summary list of all their previous oders.
    2. Clicking on the order link takes the user to a copy of the order confirmation page with the complet details.
3. As a returning user, I want to save my delivery details to my user profile
    1. On the profile page, the user can check if there are saved contact details on their account.
    2. If there are not details, the user can add these and update.
    3. If the details exist but are incorrect, the user can correct them and update.
    4. If signed in during the checkout page, the user can also check the box to save the contact details to their account.


 -**Admin Users**
1. As an admin user, I want to be able to add, update and remove products, classes and trainers from the website
    1. The admin user can view the products, classes, and trainers currently listed on the site admin page.
    2. From here they can add additional records, or edit the exiting records.
    3. When logged in to the LoveYoga site as an admin user, they will also have the option under the "MyAccount" dropdown to add new classes, trainers or products.
    4. On the Trainers, Classes, or Shop page, they will also be able to see green 'edit' and 'delete' buttons to amend or remove each record.
2. As an admin user, I want to be able to view the orders that have been placed
    1.The admin user can view the successful orders and individual order line items for each order on the site admin page.

### Manual Testing of All Elements

Testing was carried out by myself using Chrome DevTools while writing the code, and once deployed, friends and family helped to test the site on various screen sizes and web browsers.

#### Navbar

  - **Tests**

    1. Check that the 'LoveYoga' logo text is visible on all screen sizes, and resized accordingly.
       - **_Verified_**
    2. Check that navbar links are collapsed to hamburger menu for tablet and mobile screens.
       - **_Verified_**
    3. Check that dropdown menu of links is shown when hamburger menu is clicked on mobile and tablet.
       - **_Verified_**
    5. Click on each link to ensure the link goes to the correct page.
       - **_Verified_**
     6. Check the "My Account" and "Search" items collapse to icons on small screen sizes
        - **_Verified_**
    7. Check the Search input returns results on the classes page when search term is entered
       - **_Verified_**
      8. Check the basket total updates and displays the running basket total
         - **_Verified_**

#### Footer

  - **Tests**
    1. Check that footer is visible at the bottom of the page.
        - **_Verified_** 
    2. Check that the 'LoveYoga' logo tex, the contact information below, and the the social media icon links are centered and clearly visible on all screen sizes.
        - **_Verified_** 
    3. Check that the social media links open in a new tab.
        - **_Verified_** 
    4. Check that the social media links open to the correct site.
        - **_Verified_** 

  - **Bugs found during testing**
     No issues found.

#### Home Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
     2. Hero Image is visible on all screen sizes, and covers the full width and height.
        - **_Verified_**

  - **Bugs found during testing**
     No issues found.

#### User Account

  - **Tests**
     1. Register link is available under MyAccount for new users
        - **_Verified_**
     1. User can complete their username, email and pasword details to register an new account
        - **_Verified_**
     3. User recieves a confirmation email with a link to verify their email address
        - **_Verified_** 
     4. User can log in to their account once their email is verified
        - **_Verified_**  
     5. My Profile and Logout links are visible once user is logged in
        - **_Verified_**
     6. User can log out of their account
        - **_Verified_** 
     7.  User can request a password reset if they forgot their password
         - **_Verified_**
     8. User cannot access Profile page if they are not logged in
        - **_Verified_**
    
  - **Bugs found during testing**
    - Emails were not sending due to incorrect "EMAIL_HOST_PASSWORD" config var,issue was resolved when this was corrected

#### Trainers Page

  - **Tests**
     1. Page header displays "Meet our Trainers"
        - **_Verified_**
     2. Trainer information is displayed as a responsive grid of cards
        - **_Verified_**        - 
     3. Each card contains an image of the trainer, details on the years spent practicing yoga, years spent teaching, and bio information (currently Lorem Ipsum text filler)
        - **_Verified_**
     4. Each card also displays a solid pink button link for classes given by that tainer, and links to the filtered classes on the classes page
        - **_Verified_**
     5. Solid teal edit and delete buttons are displayed for Admin users when logged in
        - **_Verified_** 

  - **Bugs found during testing**
     - None

#### Classes Page

  - **Tests**
    1. Page header displays "Our Classes"
        - **_Verified_**
     2. Class information is displayed as a responsive grid of cards
        - **_Verified_**        - 
     3. Each card contains an image of the class, bold pink text displaying class name, and the class price displayed below
        - **_Verified_**
     4. Clicking the card image links to the class info page
        - **_Verified_**
     5. Solid teal edit and delete buttons are displayed for Admin users when logged in
        - **_Verified_** 
     1. At the top of the page, 'filter by trainer' dropdown is displayed. User can select a trainer and the classes will display with the approproate filter
        - **_Verified_**
    1. At the top of the page, 'filter by practice' dropdown is displayed. User can select a practice and the classes will display with the approproate filter
        - **_Verified_**
     1. At the top of the page, 'Sort' dropdown is displayed. User can select a sort preference and the classes will display with the approproate sort filter
        - **_Verified_**
     
  - **Bugs found during testing**
     - None

#### Class Info Page

  - **Tests**
    1. Page header displays "Yoga Classes"
        - **_Verified_**
     2. Class image is displayed on the left hand side on med/large screens, and at the top on small screens
        - **_Verified_**        - 
     3. Class description and details are displayed on the right hand side on med/large screens, and at the top on small screens
        - **_Verified_**
     4. Correct details and pricing are displayed for the selected class.
        - **_Verified_**
     1. Clicking 'Add to Basket' button adds the class to the shopping basket and displays the success toast with basket summary
        - **_Verified_**
    1. Clicking the 'Add to Basket' button if the class is already found in the basket returns the error toast message and the class is not added to the basket again
        - **_Verified_**
     1. Links to "Find another class" or "Need some gear" at the bottom of the page lead  to classes and shop pages respectively.
        - **_Verified_**
     
  - **Bugs found during testing**
     - None

#### Shop Page

  - **Tests**
    1. Page header displays "Shop Yoga Gear"
        - **_Verified_**
     2. Product information is displayed as a responsive grid of cards
        - **_Verified_**        - 
     3. Each card contains an image of the product, bold pink text displaying product name, and the product description and price displayed below
        - **_Verified_**
     4. Clicking the card image links to the product info page
        - **_Verified_**
     5. Solid teal edit and delete buttons are displayed for Admin users when logged in
        - **_Verified_** 
     1. At the top of the page, 'Sort' dropdown is displayed. User can select a sort preference and the classes will display with the approproate sort filter
        - **_Verified_**
    1. At the top of the page, 'search' input appears, and user can search terms, with the relevant results displaying
        - **_Verified_**
     
  - **Bugs found during testing**
     - None

#### Product Info Page

  - **Tests**
    1. Page header displays "Shop Yoga Gear"
        - **_Verified_**
     2. Product image is displayed on the left hand side on med/large screens, and at the top on small screens
        - **_Verified_**        - 
     3. Product description and details are displayed on the right hand side on med/large screens, and at the top on small screens
        - **_Verified_**
     4. Correct details and pricing are displayed for the selected product
        - **_Verified_**
    4. Below the product details section, the quantity input is displayed, and the user can add or reduce the required qty using the +/- buttons
        - **_Verified_**
     1. Clicking 'Add to Basket' button adds the product to the shopping basket and displays the success toast with basket summary
        - **_Verified_**
    1. Clicking the 'Add to Basket' button if the product is already found in the basket increases the basket qty of that product by the sleected qty and a success toast message is displayed with the basket summary.
        - **_Verified_**
     1. Links to "Find another class" or "Need some gear" at the bottom of the page lead  to classes and shop pages respectively.
        - **_Verified_**
     
  - **Bugs found during testing**
     - None
     
#### Shopping basket page

  - **Tests**
     1. Basket items are displayed in a table format with image, name & description, price, qty, and line subotal information
        - **_Verified_**
     2. Classes and Products are grouped together in separate sections, with subtotal for each.
        - **_Verified_**        
     3. If no classes in the basket, classes section is hidden
        - **_Verified_**
     4. If no products in the basket, products section is hidden.
        - **_Verified_**
    4. A red trashcan icon is displayed beside the qty for each line item. Clicking this removes the item from the basket, and success toast message is displayed.
        - **_Verified_** 
    4. A green pencil icon is displayed beside the qty for each product line item. The prduct qty field can be updated, and clicking pencil icon adjusts the product qty in the basket, and success toast message is displayed.
        - **_Verified_** 
     5. Below the products section, basket subtoal is displayed with combined total of classes and products
        - **_Verified_** 
     6. Default delivery cost of €0 is applied if there are no products in the basket. Delivery is €5 if there are products in the basket
        - **_Verified_**    
     7. Grand Total value displays the sum of the basket subtotal and the delivery value
        - **_Verified_** 
    8. The modal footer section displays buttons for "Add to favourites", "Add review" and "Close"
        - **_Verified_** 
    9. Link to 'Secure Checkout' is displayed below the grand total
        - **_Verified_**
     10. Links to "Find another class" or "Need some gear" at the bottom of the page lead  to classes and shop pages respectively.
        - **_Verified_**"

  - **Bugs found during testing**
     - None

#### Checkout Page

  - **Tests**
     1. Contact details and card info form is displayed on the left side of the screen and order summary is displayed on the right hand side of the screen, these are stacked on small screens
        - **_Verified_**
     2. If the user has previously saved their details to their profile, these will be prefilled on the form
        - **_Verified_**       
     2. Contact details and address required form fields are marked with *. Form validation kicks in on submit if these are not completed.
        - **_Verified_**   
     3. Country input field is a dropdown list of countries.
        - **_Verified_**    
     4. If logged in, checkbox is displayed to save contact information. If not logged in, links are displayed to login or register.
        - **_Verified_** 
    5. Stripe card input is displayed below the address form
        - **_Verified_** 
    6. Update Basket and Complete Order buttons are displayed below the Stripe card input
        - **_Verified_**    
     7. Red alert text is displayed below the 'complete order' button with the total amoutn to be charged to the card
        - **_Verified_** 
    8. If all details are correctly completed, clicking the "complete order" button with submit the order form. Loading overlay is displayed while the order is processing
        - **_Verified_** 
     9. If the order is successful, the order is created in the database, and customer details are saved to their profile if the check box is selected. User is directed to the 
        - **_Verified_**
     10. If the order is successful, User is directed to the checkout success page, and order confirmation number is displayed on the toast success message, and at the top of the page.
         - **_Verified_**
     11. If the order is successful,the user recieves an order confirmation email with the order details.
         - **_Verified_** 
     12. If the order is successful, a toast error message is displayed
         - **_Verified_**    
    13. If there is any issue or crash during the order submit process, the Stripe webhook will capture the order details, the order will be created in the datbase and the customer details will be saved to the profile
         - **_Verified_** 

  - **Bugs found during testing**
     - There was an issue with the stripe payment intent suceeded webhooks being successful, this was due an issue with the email config vars, and also as the webhook for gitpod endpoint was active at the same time as the deployed endpoint. These issues were resolved and the payment intent suceeded webhook is successful now and the order is being created.

#### Checkout Success page

  - **Tests**
     1. Success toast is displayed with the order confirmation number
        - **_Verified_**
    2. Order confirmation number is also displayed at the top of the page
         - **_Verified_**
     1. Order summary is displayed on the page in the same format as the basket.
        - **_Verified_**
     3. Total amount paid is displayed at the bottom fo the page.
        - **_Verified_**
     4. Links to the Classes page and shop are displayed at the bottom of the page.
        - **_Verified_**  
        - 
  - **Bugs found during testing**
    - None

#### Profile Page

  - **Tests**
     1. Profile page is only accessible by users once logged in.
        - **_Verified_**
    2. Form for the customer details is displayed on the left of the screen. Details are prefilled if they have bee previously saved.
         - **_Verified_**
     1. User can update the details and click on the update button to submit the new details.
        - **_Verified_**
     1. Previous order list is displayed on the right side of the screen
        - **_Verified_**
     3. Each line of the ord list contains order number, order date, order summary details (name + qty), and order total value
        - **_Verified_**
     3. Order number links to a copy of the order confrimation page for that order with full order summary details.
        - **_Verified_**
        
  - **Bugs found during testing**
    - No bugs found
