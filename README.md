<h1 align="center">Fairchild School Parent-teacher Booking App </h1>

Developer: Krishan Gharu

[Visit this website]()

![Responsive Image]()

<br>

## **Contents**

* [About](#about)
* [User Experience Design](#user-experience-design)
  * [Strategy Plane](#strategy-plane)
    * [Target Audience](#target-audience)
    * [Mission Objectives](#mission-objectives)
    * [The Why](#The-Why)
    * [Ideas & Inspiration Mind Map:](#The-Inspiration-and-Ideas-Map)
    * [Demographic](#Demographic)
    * [Colour Palette Ideas](#Colour-Palette-Ideas)
    * [Content Strategy](#Content-Strategy)
    * [Typography](#Typography)
  * [The Scope Plane](#the-scope-plane)
    * [Functional Requirements](#functional-requirements)
    * [Content Requirements](#content-requirements)
    * [Interaction Design](#interaction-design) 
    * [Scope of MVP](#scope-of-mvp)
  * [The Structure Plane](#The-Structure-Plane)
    * [Site Architecture](#Site-Architecture)
    * [Roles and Processes](#Roles-and-Processes)
  * [The Skeleton Plane](#The-Structure-Plane)
    * [User Interface](#User-Interface)
    * [Manifestations of Data](#Manifestations-of-Data)
    * [Progressive Disclosure](#Progressive-Disclosure)
    * [Header and Footer](#Header-and-Footer)
    * [Navigation](#Navigation)
    * [CTA Buttons](#CTA-Buttons)
  * [The Surface Plane](#The-Surface-Plane)
  * [User Stories](#User-Stories)
    * [Parest User Journeys](#)
    * [Teacher User Journeys](#)
    * [Super Admin](#)
    * [Non-Related Visitor](#)
* [Technologies used](#Technologies-used)
* [Libraries used](#)
* [App Features and Highlights](#Features)
* [Information Architecture](#Information-Architecture)
  * [Database](#Database)
  * [Entity-Relationship Diagram](#Entity-Relationship-Diagram)
  * [Data Modeling](#Data-Modeling)
* [Testing](#Testing)
* [Deployment](#Deployment)
  * [Local deployment](#Local-deployment)
  * [Heroku Deployment](#Heroku-Deployment)

* [Credits](#Credits)

* [Acknowledgments](#Acknowledgments)

# About

[Fairchild School Appointment App](http link) is for a fictitious school called Fairchild School, and allows Parents, Guardians, Carers to book a consultation with their child’s Teacher. The App is responsive so Parent can book and Teachers can manage appointments on mobile and tablet devices.

The app is developed by [Krishan Gharu](https://github.com/kslg).

Repository: [GitHub Repo](http link)


[Back to contents](#contents)

# User Experience Design

I used the 5 Planes of UX to provide a conceptual framework.


# Strategy Plane:

## Target Audience:

- Target Audience: 
`Users` Parents, Guardians and Carers.
`Admin` Teachers.
`Super Admim` School IT Department / School Office Admins.

## Mission Objectives:

- To develop an `mvp (minimum viable product)` that allows `Users` to book appointments with `Admin` Teachers for parents evening and other consultations.
- The app must be simple, easy for parents to use and must be able to book an appointment in `less than three clicks`.
- `Super Admins` will have backend access to manage appointments for the Users and Admin.

### The Why:

- The school was using paper forms which becomes costly and is environmentally unfriendly.

## Ideas & Inspiration Mind Map
![image](/documentation/readme_folder/images/mindmap_1.png)
![image](/documentation/readme_folder/images/mindmap2.png)



## Colour Palette Ideas:
![image](/documentation/readme_folder/images/color_pallette_ideas.png)

## Content Strategy:

- Main functionality is to book an appointment with the child's teacher.
- The Teacher has thier own admin area to view appointments and accept the appointment.
- The booking form will be easy to get to via the top navigation header or from the CTA button on the homepage.


## Typography:
https://fonts.google.com/
Montserrat was used due to it's warm style and being easy to read. The are qualities found in most school websites.
![image](/documentation/readme_folder/images/google_fonts.png)

[Back to contents](#contents)

# Scope Plane:

## Functional Requirements:

1. Problem: The `User` needs to have direct access to the appointment form to make an appointment.

- Solution: Acces the form in `less than three clicks`.

2. Problem: `Users` must not be allowed to see other `User` appointments order to protect their sensitive data.

- Solution: Create an `Admin Area` so only Teachers can login and gain access.

3. Problem: `Users` need to be notified that thier appointment is confirmed.

- Solution: The `Admin` can accpect the appointment which then `sends a confirmtion email` to the `User`

4. Problem: If appointment is no longer needed then it need to be removed from the appointments list.

- Solution: The `Admin` can `delete appointment records` from the Admin Area.

5. Problem: The `Admin` accidentally click delete on the appointment.

- Solution: `Defensive Programming` put in place to ask the `Admin` to confirm deletion of the appointment. 

6. Problem: Harmful bots and malicious attackers could use the appintment form to crash the site.

- Solution: Implement a `CAPTCHA` to the form so human intervention is needed to submit the form.
  - CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a type of security measure known as challenge-response authentication. CAPTCHA helps protect the site from spam and automated scipts by asking the `User` to complete a simple test that proves you are human and not a computer trying to break into a password protected account.

  - A CAPTCHA test is made up of two simple parts: a randomly generated sequence of letters and/or numbers that appear as a distorted image, and a text box. To pass a the test and prove your human identity, simply type the characters you see in the image into the text box.


## Content Requirements:

- `Public` Homepage with hero text to explain what the app is for.
- `Public` Booking form for the `User` to create the appointment.
- `Public with Restrictions` Admin area to Teacher `Admin` to manage the appointments.
- `Public` Login Page
- `Private` Teacher `Admin` Register Page - Not public facing page. This will be a private link shared to Teachers.

## Interaction Design:

- All CTA (Call to Action) buttons will change colour to let the customers know that the buttons are clickable. 
- The `User` and `Admin` are notified for all changes to appointments and data.
- The `Admin` login state is reflected to the `Admin` on the front-end.
- The `User` recieves an email confirmation when the appointment have been accepted by the `User`

## Scope of MVP:
Using the MoSCoW prioritisation method to outline the importance of each requirement and what needs to be delivered in the MVP.

![image](/documentation/readme_folder/images/moscow_pp4.png)

[Back to contents](#contents)

# The Structure Plane:

## Site Architecture

![image](/documentation/readme_folder/images/site_structure.png)

## Roles and Processes

- Permitted access based on `User` and Teacher `Admin` Role:

| Page Name | User | Admin | Super User |
| ------------- | ------------- | ------------- | ---------- |
| home page                   | Y | Y | Y |
| login page                  | N | Y | Y |
| registration page           | N | Y | Y |
| logout page                 | N | Y | Y |
| teacher admin               | N | Y | Y |
| make appointments           | Y | Y | Y |
| view appointments           | N | Y | Y |
| update appointments         | N | Y | Y |
| delete appointments         | N | Y | Y |


[Back to contents](#contents)

# The Skeleton Plane:

## Header:
- Cream background.
- Dark Green Text.
- Hover States: Underline style.

  - Example:
  <br>
![image](/documentation/readme_folder/images/header.png)

## Footer:
- Brown background.
- Dark Green text.
- Crean Icon.

  - Example:
  <br>
![image](/documentation/readme_folder/images/footer.png)


## Colour Palette:

![image](/documentation/readme_folder/images/colour_pallete.png)


# Manifestations of Data

## Data at rest

- Appointment Data in the Admin
<br>
![image](/documentation/readme_folder/images/data_at_rest_appointments.png)
<br>
- Teacher in the Admin
<br>
![image](/documentation/readme_folder/images/data_at_rest_teachers.png)

## Data in motion

1. Data is `captured` from the appointment form and `stored` in the database.
<br>
![image](/documentation/readme_folder/images/data_in_motion_appointment_form.png)
![image](/documentation/readme_folder/images/data_in_motion_admin.png)
<br>

2. An `email` is sent to the `User` when a appointment is accepted by the `Admin`
<br>
![image](/documentation/readme_folder/images/data_in_motion_email.png)

## Data in use

Appointment Data is `accessed` when the Teacher `Admin` logs into the Teacher Admin area.

![image](/documentation/readme_folder/images/data_in_use_manage_appointment.png)


# The Skeleton Plane:


# User Stories

## **User**

| Issue ID    | User Story |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/1)| User Story: Install Bootstrap 4 Theme
|[#2](https://github.com/kslg/appointment-app/issues/24)| User Story: Django Simple CAPTCHA on Login Page
|[#3](https://github.com/kslg/appointment-app/issues/6)| User Story: CRUD - CREATE Functionality
|[#2](story link)| 
|[#2](story link)| statement  
|[#2](story link)| statement  
|[#2](story link)| statement  
|[#2](story link)| statement  
|[#2](story link)| statement  

## **Teacher Admin**

| Issue ID    | User Story |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/23)| User Story: Sign Out Success Message
|[#2](https://github.com/kslg/appointment-app/issues/5)| User Story: CRUD - READ Functionality
|[#3](https://github.com/kslg/appointment-app/issues/7)| User Story: CRUD - UPDATE Functionality
|[#4](https://github.com/kslg/appointment-app/issues/8)| User Story: CRUD - DELETE Functionality
|[#5](https://github.com/kslg/appointment-app/issues/14)| User Story: Send Email to Parent when appointment is Approved. django.core.mail module.
|[#6](story link)| statement  
|[#7](story link)| statement  



[Back to contents](#contents)

---

## Technologies used

- ### Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [jQuery](https://jquery.com/): was used to control click events and sending AJAX requests.
    + [jQuery User Interface](https://jqueryui.com/) was used to create interactive elements.

- ### Databases:

    + [SQLite](https://www.sqlite.org/): was used as a development database.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
    + [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [Draw.io](https://www.lucidchart.com/) was used to make a flowchart for the README file.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [pycodestyle 2.9.1](https://pypi.org/project/pycodestyle/): was used to validate Python code for the website.

[Back to contents](#contents)

---

## Features


**Navbar**

![Navbar]()

Navbar has the following links:
- home page
- button "get started", which leads to the registration page and login page
- ![Get Started button](documentation/features/navbar/get_started_button.png)
- It also has a logo of the school
- ![Logo](documentation/features/navbar/main_logo.png)

The simplistic design of the navbar is based on the decision to make the use of the webapp easy for the user.


**Home page**

**Make Appointment Page**

**Login page**

**Register page**

**CRUD Functionalily**

**Defensive Programming**

**User Athentication**

**Django Simple CAPTCHA on Make Appointment Page**

**Email Confirmation**

**Bootstrap Theme**

**Bootstrap Alerts**

**Application Delete Page**

**Time Slot selector**

```Python
  # Time slot options
  TIME_SLOTS = (
      ('0', '15:30 - 15:45'),
      ('1', '15:45 - 16:00'),
      ('2', '16:00 - 16:15'),
      ('3', '16:15 - 16:30'),
      ('4', '16:30 - 16:45'),
      ('5', '16:45 - 17:00'),
  )
```

**Teacher Dropdown Selector**

**Date Picker on Make Appointment Page**



[Back to contents](#contents)

---


---

## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

### Entity-Relationship Diagram

* The ERD was created using [Draw.io](https://www.lucidchart.com/).

- [Database Scheme]()



[Back to contents](#contents)

---
## Testing

Testing against the Acceptance Criteria in the User Stories.

[Back to contents](#contents)

---

## Deployment

- The app was deployed to [Heroku](https://heroku.com).
- The app can be reached by the [link]()

### Local deployment to Staging

### Deployment to Git


---

1. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`


1. Create a `.gitignore` file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a `.env` file. This will contain the following environment variables:

    ```python
    import os
      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
      os.environ['DEBUG'] = 'True'
    ```

    *During the development stage DEBUG is set to True, but it is vital to change it to False.*

1. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access the admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.


### Heroku Deployment

* Set up a local workspace on your computer for Heroku:
    - Create a list of requirements that the project needs to run:
      - type this in the terminal: `pip3 freeze > requirements.txt`
    - Commit and push the changes to GitHub
    
* Go to [www.heroku.com](www.heroku.com) 
* Log in or create a Heroku account.
* Create a new app with any unique name <name app>.

  ![Heroku. Create New App](documentation/deployment/new_heroku_app.png)

* Create a Procfile in your local workplace:

  ![Heroku. Procfile](documentation/deployment/heroku_procfile.png)
    
    This file will will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
    - Commit and push the changes to GitHub.

* Go to resources in Heroku and search for postgresql. Select Hobby dev - Free and click on the provision button to add it to the project.

  ![Heroku. Postgres](documentation/deployment/heroku_postgres.png)

* Go to the settings app in Heroku and go to Config Vars.

  ![Heroku. Settings](documentation/deployment/settings_tab.png)

Click on Reveal Config Vars and add the following config variables:

| Key      | Value          |
|-------------|-------------|
| DATABASE_URL | ... | 
| DISABLE_COLLECTSTATIC | 1 |
| EMAIL_HOST_PASS | ... |
| EMAIL_HOST_USER | ... |
| HEROKU_HOSTNAME | ... |
| SECRET_KEY | ... |


* Copy the value of DATABASE_URL and input it into the .env file and generate a secret key (you may use [Djecrety](https://djecrety.ir/) for secret key generation).
* Create EMAIL_HOST_PASS and EMAIL_HOST_USER with a gmail account and add values to these keys.
* Migrate changes.
* Set debug to False in settings.py
* Commit and push the changes to GitHub.
* Connect your repository to Heroku.

  ![Heroku. Connect to Heroku](documentation/deployment/heroku_connect_github.png)

* Deploy the app to Heroku by clicking "Deploy Branch" button. If you want to enable auto-deployment, click "Enable Automatic Deployment".

  ![Heroku. Deploy to Heroku](documentation/deployment/heroku_deploy_branch.png) 


The deployment process will start.

  ![Heroku. Deploy to Heroku](documentation/deployment/heroku_deploying.png) 

Click "View build logs" to see the progress of the deployment.

  ![Heroku. Deploy to Heroku](documentation/deployment/heroku_deploying_view.png)


*Due to security updates, Heroku dashboard will not allow you to deploy your app from GitHub. Thus, you need to run the following commands in your terminal:*

| action | terminal command | comment |
| ------ | ---------------- | ------- |
| login to your heroku account | `heroku login -i` | |
| create a new app on heroku | `heroku create NAME-OF-YOUR-APP` | if you haven't created the app before, and then, you can access the app via the Heroku dashboard and set up your config vars.|
| add remote to your local repository | `heroku git:remote -a NAME-OF-YOUR-APP` | if you have already created app on Heroku (before the security updates) and connected it using Heroku dashboard |
| deploy new version of the app | `git push heroku main` | |
| rename app | `git remote rename NAME-OF-YOUR-APP NAME-OF-YOUR-APP-2` | |

**Final Deployment**

* Set debug to False locally + delete DISABLE_COLLECTSTATIC from config vars in Heroku dashboard.
* Commit and push the changes to GitHub.

[Back to contents](#contents)
---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://www.heroku.com/): for the free hosting of the website.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [Favicon Generator. For real.](https://realfavicongenerator.net/): for providing a free platform to generate favicons.

*All names are fictional (the majority of the names were taken from "The Simpsons" and "Rick and Morty" cartoons), and any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.*

[Back to contents](#contents)
---

## Acknowledgments


[Back to contents](#contents)