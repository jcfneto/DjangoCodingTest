## IGS-Software Manger

Build with:

- [Python](https://www.python.org/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html)

The project includes:

- Django Admin Panel to manage:
   - The company's departments
   - Employee data
   - Application users
   - Token generation for API access


- API with three endpoints:
  - `department/`
  - `employee/`
  - `user/register/` 

---
## Getting Started

This is an example of how you may give instructions on setting up your project locally. 
To get a local copy up and running follow these simple example steps.

### Prerequisites

- Python >= 3.8
- Pip >= 21.1.1

### Installation

1. Clone the repository
```
git clone https://github.com/jcfneto/igs-software-manager.git
```

2. Enter in `igs-software-manager` folder and install the requirements
```
pip install -r requirements.txt
```

3. Create the SQLite DB and tables 
```
python manage.py migrate
```

4. Run the application
```
python manage.py runserver
```

### Create super user

To create a super user, use the command:

```
python manage.py createsuperuser
```

### Create authorization token

For any API request, the authorization token is required in the header. To create it, 
just access the admin. As per the image below.

<a href="https://imgur.com/7jWefWe"><img src="https://i.imgur.com/7jWefWe.png" title="source: imgur.com" /></a>

---

## API

### Department

With the `department/` endpoint it is allowed to make all requests (`GET`, `POST`, `PUT`, `DELETE`).

Example:

`POST` at `department/`

<a href="https://imgur.com/HO4zlDl"><img src="https://i.imgur.com/HO4zlDl.jpg" title="source: imgur.com" /></a>

`GET` at `department/`

<a href="https://imgur.com/gmpDuxO"><img src="https://i.imgur.com/gmpDuxO.jpg" title="source: imgur.com" /></a>

`PUT` at `department/`

<a href="https://imgur.com/YxOtXJ5"><img src="https://i.imgur.com/YxOtXJ5.jpg" title="source: imgur.com" /></a>

`DELETE` at `department/`

<a href="https://imgur.com/RykiIEw"><img src="https://i.imgur.com/RykiIEw.jpg" title="source: imgur.com" /></a>


### Employee

The `employee/` endpoint allows the following requests: `GET`, `POST`, `DELETE`.

Examples:

`POST` at `employee/`

<a href="https://imgur.com/yc5r895"><img src="https://i.imgur.com/yc5r895.jpg" title="source: imgur.com" /></a>

`GET` at `employee/`

<a href="https://imgur.com/Wma6HtO"><img src="https://i.imgur.com/Wma6HtO.jpg" title="source: imgur.com" /></a>

`DELETE` at `employee/`

<a href="https://imgur.com/TKvicf7"><img src="https://i.imgur.com/TKvicf7.jpg" title="source: imgur.com" /></a>

### User

With the `user/register/` endpoint it is only allowed to add a new user, that is, 
only `POST` is allowed.

Example:

`POST` at `user/register/`

<a href="https://imgur.com/0GdMgNC"><img src="https://i.imgur.com/0GdMgNC.jpg" title="source: imgur.com" /></a>

### Requests without Token

For any request that the token is not provided, the following message is returned.

<a href="https://imgur.com/T16PJaU"><img src="https://i.imgur.com/T16PJaU.jpg" title="source: imgur.com" /></a>

---
## Contact
José Carlos > eng.jcfneto@gmail.com
