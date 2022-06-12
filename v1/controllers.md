---
title: Controllers
draft: false
description: |
    Controllers is great place to connecting your request, model, and also outputing the response.
section: The Basics
---


## Writing Controllers

### Basic Controllers

```python
from app.http.models import User
from .Controller import Controller


class UserController(Controller):
    
  def show(self, id):
    """
    Show the profile for a given user.
    """

    return view('user.profile', {
        'user': User.find(id)
    })
```


Defined in `routes/web.py`

```python
from ponodo.facades import Route
from app.http.controllers import UserController


Route.get("/users/@id", controller=UserController, action="show")
```

### Single Action Controller

```python
class ProvisionServer(Controller):

  def __call__(self):
    # ...
```

```python
Route.post("/server", controller=UserController)
```

or

```python
from ponodo.decorators import controller

@controller
def provision_server():
    # ...
```

```python
Route.post("/server", controller=provision_server)
```

## Controller Middleware

```python
Route.get("profile", to="user@show").middleware("auth")
```

```python
@Middleware("auth")
class UserController(Controller):

  @middleware("log")
  def index(self):
    # ...

```

## Dependency Injection & Controllers

### Constructor Injection

```python
from app.http.controllers import Controller
from app.repositories import UserRepository


class UserController(Controller):

  def __init__(self, users: UserRepository):
    self.users = users

```

### Method Injection

```python
from ponodo.http import Request


class UserController(Controller):
    
  def update(self, request: Request, id);
    pass
```