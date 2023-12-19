<h1>Grupo Pierola Romania</h1> 

<p>A simple website designed for sales of wines.</p>

<h2>UX</h2>
<p>This website is designed for people over 18 years old interested in purchasing of wines from Spain.</p>
<h3>User Stories</h3>
<ol>
<li>
    <p>As user I want to buy wines from spain.</p>
    <p>The website is dedicated for sales of spanish wines</p>
</li>
<li>
    <p>As user I want to order couple wines.</p>
    <p>The website has a page dedicated for displaying and sorting the wines, as well as a bag, the user can select couple wines and to order them through the checkout sistem with card payment provided</p>
</li>
<li>
    <p>As user I want to see my order history and to save my delivery address</p>
    <p>The website has an authentication sistem that allow to the user to create and accound and a "my profile" page where he/she can save their details and to see every order submited.</p>
</li>
<li>
    <p>As business owner I want manage the products, orders and offers</p>
    <p>The website has a product management page where new products can be added, characteristics of the existing one modified. </p>
</li>
<li>
    <p>As business owner I want manage the products</p>
    <p>The website has a orders page where the business owner can track the orders of the client so he/she can start the delivery </p>
</li>
<li>
    <p>As business owner I want manage the offers</p>
    <p>The website has a offers where the business owner can create, display, update, delete  </p>
</li>
<li>
    <p>As user who speak romanian I want to be able to use the website</p>
    <p>The website is translated in romanian</p>
</li>
</ol>
</ul>


<h2>Features</h2>

<h3>Existing Features</h3>
<h4>1.Authentication</h4>
<p>Allows to users to create an profile where they can save their delivery address or to see a order history</p>
<p>Allows to users to create and authentificate using social accounts: Google </p>
<h4>2.Bag</h4>
<p>Allows to users to create a selection of wines and to be keep as long the user is browsing the website</p>
<h4>3.Checkout</h4>
<p>Allows to users to place an order and to make payments by card</p>
<h4>4.Search</h4>
<p>Allows to users to search for wines by name or key word</p>
<h4>5.Product, order and offers management</h4>
<p>Allows the business owner to create, update, delete products, orders and offers</p>
<h4>Internationalization</h4>
<p>The language of the website can be switch between english and romanian</p>

<h3>Features Left to Implement</h3>
<h4>1.Authentication with social accounts: Apple</h4>
<h4>2.Return and cancel order</h4>
<h4>3.Apply discounts discribed in the offer </h4>

<h2>Technologies Used </h2>
<h3><a href="https://www.python.org/">Python3</a> & <a href="https://www.djangoproject.com/">Django</a></h3>
<p>A poweful framework with a lot of built in features</p>
<h3><a href="">AWS S3 Bucket</a></h3>
<p>To store media and static files</p>
<h3><a href="https://stripe.com/">Stripe</a></h3>
<p>Provides a good online payment sistem</p>
<h3><a href="https://jqueryui.com/">JQuery</a></h3>
<p>Helpt me for DOM manipulations and for implementation of stripe</p>
<h3><a href="https://getbootstrap.com/">Bootstrap</a></h3>
<p>Used for creating the grid of the website and styling</p>
<h3><a href="https://www.w3schools.com/html/html_basic.asp">HTML</a> & <a href="https://www.w3schools.com/css/">CSS</a></h3>

<h2> Database Design & Implementation </h2>

<p>The database is described by the Entity Relationship Diagram </p>
<img src="readMePictures/Grupo Pierola Romania Database ERD.png" alt="ERD Image"> )



<h2>Testing</h2>

<h3>Over 18 customers</h3>
<p>To test that only users over 18 old can access products page, I tried to access it by typing its url for example <a href="https://grupo-pierola-ro-official.herokuapp.com/wines">https://grupo-pierola-ro-official.herokuapp.com//wines</a>, to see if the user is redirected to check age page if his or her age wasn't checked or isn't logged in. The only pages available without check age being contact and about.</p>

<h3>Administrator permissions</h3>
<p>To test that only the admistrator of the website can edit or delete products I tried to enter the url of the view that does that, being logged in as administrator and not.</p>

<h3>Bag</h3>
<p>To test that the bag keeps it content as long the user is browsing the website I add couple items in it and browse different pages. Then I close the tab and enter again on website, the bag keeps its content. </p>


<h2>Deployment</h2>
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
<h3>Heroku</h3>
<ol>
    <li>To deploy to heroku I had to install Postgress a database provided by them, and to set the key of it in settings of framework
    </li>
    <li>
        <p>Environment variables</p>
        <ol>
            <li>
            AWS_ACCESS_KEY_ID - S3 Bucket
            </li>
            <li>
            AWS_SECRET_ACCESS_KEY - S3 Bucket
            </li>
            DATABASE_URL - Postgress database 
            <li>
            EMAIL_HOST_PASSWORD - Email
            </li>
            <li>
            EMAIL_HOST_USER - Email
            </li>
            <li>
            SECRET_KEY - Django Framework
            </li>
            <li>
            STRIPE_PUBLIC_KEY - Stripe
            </li>
            <li>
            STRIPE_SECRET_KEY - Stripe
            </li>
            <li>
            STRIPE_WH_SECRET - Stripe webhooks
            </li>
            <li>
              USE_AWS - To tell to framework what storage of static and media files to use
            </li>
        </ol>
    </li>
    <li>
     Install Gunicorn - server 
    </li>
    <li>
     Psycopg2-binary - database adapter
    </li>
     <li>
        Set AWS 3 Bucket
        <ol>
            <li>
                Create bucket
            </li>
            <li>
                Create group of users
            </li>
            <li>
                Create policy
            </li>
            <li>
                Create user
            </li>
            <li>
             Install django-storages
            </li>
        </ol>
    </li>
     <li>
     Set Debug - False
    </li>
</ol>

<p>To run the code locally you have to:</p>
<ol> 
    <li>Clone the github repository</li>
    <li>Create a virtual enviroment (good practice, not necessary)</li>
    <li>Install the requirements_dev.txt </li>
    <li>Set the enviroment variables described above ( and creating the necessary dependences as: S3 Bucket, Stripe account, EMAIL)</li>
    <li>open a local server provided by Django</li>
</ol>

<h2>Credits</h2>
<h3>Content</h3>
<p>The informations about products and image are provided by the owner of the company Grupo Pierola Romania</p>
<h3>Acknowledgements</h3>
I received inspiration for this project from Boutique ado <a href="https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546">GitHub Link</a>
  