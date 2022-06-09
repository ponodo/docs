---
title: Controllers
draft: false
description: |
    Controllers is great place to connecting your request, model, and also outputing the response.
section: The Basics
---


```python
class BookController(Controller):


    def index(self):
        return 'hello'
```

Middleware

```python
class BookController(Controller):

    def __init__(self):
        self.middleware('auth')
        self.middleware('auth', only=['index'])
        self.middleware('auth', except_=['view'])

    def index(self):
        return 'hello'
```