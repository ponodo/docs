# Template Engine

```html
<div>Hello {{ name }}</div>
```

```python
return view('hello')
```


For nested directory

```python
return view('admin.profile')
```

Passing data

```python
return view('hello', {
    'name': 'Fathur'
})
```


```python
return view('hello')\
    .with(name='Victoria', country='Indonesia')
```


## Templating engine


### Conditional

```html
@if role == 'admin':
    <h3>Admin</h3>
@elif role == 'user':
    <h3>User</h3>
@endif
```


```html
@for item in lists:
    <li>{{ item }}</li>
@endfor
```