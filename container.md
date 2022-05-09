# Container

## Introduction

Understanding the Ponnodo container is essential to building a powerful, large application, 
as well as for contributing to the Laravel core itself.

## Basic Usage

You can bind a class that will resolve automatically to an instance, or you can bind the instance
itself directly.

### Bind and resolve instance

Binding an instance will be shared through application.


```python
app['route'] = Router()
```

Now you can resolve the binding using square bracket or normal bracket.

```python
route = app['route']

# or

route = app('route')
```

### Bind and resolve class

Binding a class will be instantiated when resolving occur.

```python
app['cache'] = Cache
```


If you bind a class, and want to pass the parameters when resolving, you can use `parameters()`
method. You free to pass arguments or keyword arguments.

```python

cache = app('cache').parameters(foo='bar')
```

behind the scene it will instantiate `Cache(foo='bar')`


### Resolving without bind

> WIP

```python
class Foo:
    
    def __init__(self, bar: Bar):
        self.bar = bar

foo = app(Foo)
```

Note that even though we did not register the Foo class in the container, 
the container will still be able to resolve the class, even injecting the Bar dependency 
automatically!
