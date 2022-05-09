# Routing

```python
Route.get('/hello', lambda: 'world')
```

```python
Route.any('/books', lambda: 'My books')
```

## Route parameters

```python
Route.get('/books/:book', lambda book: f'I love read {book}')
```

Optional


```python
Route.get('/books/:?book', lambda book='software': f'I love read {book}')
```

constraint

```python
Route.get('/books/:book', lambda book: f'I love read {book}')\
    .where(book='[a-z]+')
```

You also can pass multiple constraint

```python
Route.get('/books/:book/chapters/:chapter', lambda book, chapter: 'todo')\
    .where(book='[a-z]+', chapter='[0-9]+')
```

Controller

```python
Route.get('/books', to='book@index')
```

It will pass to controller `BookController` and method `index` in module
`app.controllers`

If you wish to move the controller outside default one, you can add into the module path.

```python
Route.get('/books', to='book@index', module='app.book.controllers')

```

Naming the route

```python
Route.get('/books', to='book@index', name='list_of_books')
```

If you want to pass the controller 

```python
from app.controller import BookController

Route.get('/books', controller=BookController, action='index')
```

this method will ignore the module kwargs because we already know the module itself by
importing it.

or if you prefer to use string

```python
Route.get('/books', controller='book', action='index')
```

## Group

> WIP

```python
with Route.group(
        middleware=['auth'],
        prefix='books',
        name='book.',
    module='app.'
) as group:
    group.get('/', to='books@index')
```