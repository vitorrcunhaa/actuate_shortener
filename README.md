# actuate_shortener

**Goal:**

Deliver an Http Server that does the following
1. Allows the Client to send a URL to be shortened. Note: The same
unique long URL should ALWAYS be shortened to the same unique
short URL
a. Input: URL to be shortened
b. Returns: Shortened URL
2. Allows the Client to send a shortened URL and obtain the original,
long URL
a. Input: Shortened URL
b. Returns: Original Long URL
3. Redirection of the shortened URL to the Original URL
4. Extra Credit:
a. A click counting mechanism, to see how many times people
have “Clicked on” a shortened URL

**Setup and run:**

● Clone this repository in a location of your choice

● Go inside `actuate_shortener` directory  

● At this step it is recommended that you create a virutal env with Python 3.8  
 ( How to create a virtual env: https://docs.python.org/3/library/venv.html )  

● Activate your virtual env

● Run `pip install -r requirements.txt`  
  ( If you don't have pip installed, you can do it here: https://pip.pypa.io/en/stable/installation/ )  
  
● Run `python manage.py runserver` or `python3 manage.py runserver`

● Run `python manage.py migrate` or `python3 manage.py migrate`

● Run `python manage.py createsuperuser` or `python3 manage.py createsuperuser`
 (remember this user and password, after creating the superuser, you will have access to all database objects probably in http://127.0.0.1:8000/admin/
 
Have fun 😁


