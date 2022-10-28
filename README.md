## RH Software Manager

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

- Docker >= 20.10.9
- Docker-compose >= 1.29.2

### Installation

1. Clone the repository
```
git clone https://github.com/jcfneto/igs-software-manager.git
```

2. Enter in `igs-software-manager` folder and install the requirements
```
docker-compose up -d
```

### Create super user

To create a super user, use the command:

```
docker exec -it igs-software-manager-main_web_run_1 sh -c "python manage.py createsuperuser"
```

### Create authorization token

For any API request, the authorization token is required in the header. To create it, 
just access the admin. As per the image below.

<a href="https://imgur.com/7jWefWe"><img src="https://i.imgur.com/7jWefWe.png" title="source: imgur.com" /></a>

---

## API

### Department

With the `department/` endpoint it is allowed to make all requests (`GET`, `POST`, `PUT`, `DELETE`).

Payload example:

```
{
	"name": "Marketing",
	"created_at": "2021-03-01"
}
```

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

Payload example:

```
{
	"name": "Maria",
	"email": "maria@igs-software.com.br",
	"department": "1",
	"birth_date": "1995-02-27",
	"salary": "10000",
	"first_day": "2022-02-01"
}
```

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

Payload example:

```
{
	"email": "jose_carlos@igs-software.com.br",
	"full_name": "José Carlos",
	"password": "senhaForte",
	"password_confirm": "senhaForte"
}
```

Example:

`POST` at `user/register/`

<a href="https://imgur.com/0GdMgNC"><img src="https://i.imgur.com/0GdMgNC.jpg" title="source: imgur.com" /></a>

### Requests without Token

For any request that the token is not provided, the following message is returned.

<a href="https://imgur.com/T16PJaU"><img src="https://i.imgur.com/T16PJaU.jpg" title="source: imgur.com" /></a>

---
## Contact
José Carlos > eng.jcfneto@gmail.com
