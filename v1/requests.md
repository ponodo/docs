---
title: Requests
draft: false
description: ''
section: The Basics
---

## Introduction

## Interacting With The Request

### Accessing The Request

To obtain an instance of the current HTTP request via dependency injection, you should type-hint the `ponodo.http.Request` class on your route closure or controller method. The incoming request instance will automatically be injected by the Ponodo service container:

```python
from ponodo.http import Request


class UserController(Controller):

  def store(request: Request):
    name = request.input("name")
    # ...
```

## Request Path & Method

### Retrieving The Request Path

```python
uri = request.path
```

### Inspecting The Request Path / Route

```python
if request.is("admin/*"):
  # ...

```

### Retreiving The Request URL

```python
url = request.url

url_with_query_string = request.full_url
```

```python
request.full_url_with_query(type="phone")
```

### Retreiving The Requst Method

```python
method = request.method

if request.is_method("post"):
  # ...

```

## Input

### Retreiving All Input Data

```python
inputs = request.all
```

### Retreiving An Input Value


```python
name = request.input("name")

```

```python
name = request.input("name", default="John Doe")

```

### Retreiving Input From The Query String

```python
name = request.query("name")
```

### Retreiving Boolean Input Values


```python
archived = request.bool("archived")
```

### Retreiving Date Input Values

It will return `pendulum`

```python
birthday = request.date("birthday")
```

```python
birthday = request.date("birthday", format="!H:i", timezone="Asia/Jakarta")
```

### Retreiving Input Via Dynamic Properties


```python
name = request.name
```

### Retreiving A Portion of The Input Data


```python
request.only("username", "password")

request.reject("password_confirmation")
```