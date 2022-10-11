<h1 align="center">Fairchild School Parent-teacher Booking App</h1>

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
  * [User Journeys](#)
  * [Teacher Admin Journeys](#)
* [Agile Project Management](#agile-project-management)
  * [User Stories - User](#user-stories---user)
  * [User Stories - Teacher Admin](#user-stories---teacher-admin)
  * [Tasks](#tasks)
  * [Bugs and Issues](#bugs-and-issues)
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

## Ideas and Inspiration Mind Map
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

[Back to contents](#contents)

## Content Requirements:

- `Public` Homepage with hero text to explain what the app is for.
- `Public` Booking form for the `User` to create the appointment.
- `Public with Restrictions` Admin area to Teacher `Admin` to manage the appointments.
- `Public` Login Page
- `Private` Teacher `Admin` Register Page - Not public facing page. This will be a private link shared to Teachers.

[Back to contents](#contents)

## Interaction Design:

- All CTA (Call to Action) buttons will change colour to let the customers know that the buttons are clickable. 
- The `User` and `Admin` are notified for all changes to appointments and data.
- The `Admin` login state is reflected to the `Admin` on the front-end.
- The `User` recieves an email confirmation when the appointment have been accepted by the `User`.
- Both thr `Admin` and `User` and presents with alert messages when they trigger a certain action. i.e create an appointment, etc.

[Back to contents](#contents)

## Scope of MVP:
Using the MoSCoW prioritisation method to outline the importance of each requirement and what needs to be delivered in the MVP.

![image](/documentation/readme_folder/images/moscow_pp4.png)

[Back to contents](#contents)

# The Structure Plane:

## Site Architecture

![image](/documentation/readme_folder/images/site_structure.png)

[Back to contents](#contents)

## Roles and Processes

- Permitted access based on `User`, Teacher `Admin` and `Super Admin` Role:

| Page Name | User | Admin | Super Admin |
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
| backend django admin        | N | N | Y |


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

[Back to contents](#contents)

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


# The Surface Plane:

---

# Features


## **Navbar**

![Navbar](/documentation/readme_folder/images/navbar_desktop.png)
![Navbar](/documentation/readme_folder/images/navbar_mobile.png)

Navbar links:
- Home Page (School Logo) 
- Make Appointment
- Teacher Admin

To satisfy an MPV and keeping the Navbar simple allows Users to become familiar with the app more quickly.

## **Home page**

## **Make Appointment Page**

## **Login page**

## **Register page**

## **CRUD Functionalily**

## **Defensive Programming with Bootstrap Modal**

## **User Athentication**

## **Django Simple CAPTCHA on Make Appointment Page**

## **Email Confirmation**

## **Bootstrap Theme**

## **Bootstrap Alerts**

## **Application Delete Page**

## **Time Slot selector**

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

## **Teacher Dropdown Selector**

## **Date Picker on Make Appointment Page**



[Back to contents](#contents)

---

# Agile Project Management

## **User Stories - User**

| Issue ID    | User Story |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/1)| User Story: Install Bootstrap 4 Theme
|[#2](https://github.com/kslg/appointment-app/issues/24)| User Story: Django Simple CAPTCHA
|[#3](https://github.com/kslg/appointment-app/issues/6)| User Story: CRUD - CREATE Functionality
|[#4](https://github.com/kslg/appointment-app/issues/9)| User Story: Add Bootstrap Alert Messages  
|[#5](https://github.com/kslg/appointment-app/issues/10)| User Story: Role Based Login and Registration Functionality
|[#6](https://github.com/kslg/appointment-app/issues/11)| User Story: Restrict User Access to Teacher Admin Area

## **User Stories - Teacher Admin**

| Issue ID    | User Story |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/23)| User Story: Sign Out Success Message
|[#2](https://github.com/kslg/appointment-app/issues/5)| User Story: CRUD - READ Functionality
|[#3](https://github.com/kslg/appointment-app/issues/7)| User Story: CRUD - UPDATE Functionality
|[#4](https://github.com/kslg/appointment-app/issues/8)| User Story: CRUD - DELETE Functionality
|[#5](https://github.com/kslg/appointment-app/issues/14)| User Story: Send Email to Parent when appointment is Approved. django.core.mail module.
|[#6](https://github.com/kslg/appointment-app/issues/9)| User Story: Add Bootstrap Alert Messages 
|[#7](https://github.com/kslg/appointment-app/issues/22)| User Story: Delete Appointment - Defensive Programming with Bootstrap Modal
|[#8](https://github.com/kslg/appointment-app/issues/10)| User Story: Role Based Login and Registration Functionality

## **Tasks**

| Issue ID    | Tasks |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/4)| Task: Create Appointment Model
|[#2](https://github.com/kslg/appointment-app/issues/17)| Task: Update Login, Signup and Log out pages with Bootstrap and Crispy forms.  
|[#3](https://github.com/kslg/appointment-app/issues/3)| Task: Install Django and start up libraries

## **Bugs and Issues**

| Issue ID | Bugs / Issues |
|----------|--------------------------------------------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/25)| Issue: Trying to set up email sending via gmail
|[#2](https://github.com/kslg/appointment-app/issues/26)| Issue: Seeing this error when I click the delete button on the appointment
|[#3](https://github.com/kslg/appointment-app/issues/27)| Issue: I cannot get the appointment to delete from the pop up modal
|[#4](https://github.com/kslg/appointment-app/issues/28)| Issue: CAPTCHA Alert not showing as Warning Alert
|[#5](https://github.com/kslg/appointment-app/issues/29)| Issue: Success Alert Message not showing when admin logs out
|[#6](https://github.com/kslg/appointment-app/issues/13)| BUG: Styling on Manage Appointment Cards
|[#7](https://github.com/kslg/appointment-app/issues/19)| BUG: Fix padding issue on Account pages (Login, Sign out)
|[#8](https://github.com/kslg/appointment-app/issues/12)| BUG: Mobile View - Burger Menu does not show Nav Links
|[#9](https://github.com/kslg/appointment-app/issues/18)| BUG: Fix Bootstrap errors seen in the browser console
|[#10](https://github.com/kslg/appointment-app/issues/16)| BUG: Sign Out message showing on appointment page. Needs to show on redirect page.



[Back to contents](#contents)

---

## **Technologies used**

- ### Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): is the main language used to build the back-end.
    + [JS](https://www.javascript.com/): for the CAPTCHA Refesh function and to handle the timeout for bootstrap alerts.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): is markup language used to build the front-end templates.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): is styling language used adjust layout and front-end styles.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): a high-level Python web framework for the app.
    + [Django Simple Captcha](https://pypi.org/project/django-simple-captcha/): is a simple captcha form to prevent automated bot attacks.
    + [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html): is an integrated set of Django applications dealing with account authentication, registration and management.
    + [CrispyForms](): is an optimised way of rendering forms on the front-end in a very elegant and `DRY` way. 

- ### Databases:

    + [PostgreSQL](https://www.postgresql.org/): database to store all data.

- ### Other tools:

    + [Github](https://github.com/): hosting service for software development and version control using Git.
    + [Pip3](https://pypi.org/project/pip/): is the package manager to intstall Python modules and libraries.
    + [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Rquests for Python to understand.
    + [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python. 
    + [Heroku](https://dashboard.heroku.com/): the hosting service to host the app.
    + [VSCode](https://code.visualstudio.com/): the IDE used to program the app.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): used to identify any errors when being rendered in the browser.
    + [Font Awesome](https://fontawesome.com/): used to source social icons to be used on the app.
    + [Draw.io](https://www.lucidchart.com/) used to create the Database schema.
    + [W3C Validator](https://validator.w3.org/): used to validate HTML5 code.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): used to validate CSS code.
    + [pycodestyle 2.9.1](https://pypi.org/project/pycodestyle/): was used to validate Python code.

[Back to contents](#contents)

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


[Back to contents](#contents)
---

## Acknowledgments


[Back to contents](#contents)