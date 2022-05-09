# Controller

Basic controller

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