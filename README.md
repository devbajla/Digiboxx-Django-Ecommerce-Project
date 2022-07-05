# Digiboxx-Django-Ecommerce-Project
This project focused on building a simple e-commerce website for a library. The website has the functionality 
to create accounts and login, check the books available, and return or borrow new books.

The project was coded in Python using the Django REST framework, which is used to make web APIs. 
Django’s framework makes use of different templates, views and models to design a web API, and 
this project focused on writing basic versions of each of these aspects. 

In Django, templates use a text-based language to design the user-facing end or the front end side of the application. 
These templates were written as HTML files in this project and were kept very simple as the focus was more so on 
understanding how Django works and less on design and aesthetics. Each web page such as the home, login and available 
books pages had different templates which ranged in their functionality and complexity. While some pages like the home 
page were extremely simple with just a few links to other pages, other pages like the create user and login pages took 
in user input, while others like the available books page displayed data from the database in tables. The templates 
provided the front end interface, while both taking user input, and displaying data from the back end. 

The inputs taken in from the front end as well as the data on the back end were both managed using views. Views are 
Python scripts, which use the Django framework and once again ranged in complexity. Some views were as simple as 
rendering a template, while views like the create user view had to handle user input and add the data to the models in 
the back end. Additionally, some views like the order history view retrieved data from the back end and sent it to the 
template so that the user could see it, while the login view simultaneously took in user data and checked it against 
the database to authenticate the user’s login. The login view also started making using of a ‘session’ which stored 
the user’s id so that it could be used across the other pages until the user had logged out. 

Finally, the data stored by the website was stored in different data tables called models. This project used 3 models: 
Users, Products, and Orders. The users model stored basic information about library members such as name, email, mobile, 
borrowing status, and a password used for login. The products model contained information about the books in the library 
such as their names, stock, and availability. Finally, the orders model contained pairs of users and the books they had 
borrowed, along with the status of the order (whether it was currently borrowed or returned). These models allowed the 
website to track which books were currently being borrowed by which users and whether a user can borrow a new book or not.

