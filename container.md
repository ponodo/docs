# Container

Understanding the Ponodo container is essential to building a powerful, large application, as well
as for contributing to the Ponodo core itself. If we can assume building application like building 
home, the container work as the foundation of your home. It has solid basic structure to make the 
whole things above it stand up strong.

There are two basic things in container, binding and resolving. This method make your application
easy to configure and extend.


## Binding

Binding is assigning concrete into abstract thing. Concrete can be a working class instance or 
concrete class itself, normally concrete can be run functionally in your code base. Oppositely, 
the abstract thing can be just a simple string, or abstract class that inherit Abstract
Base Class (ABC). The abstract class cannot run functionally in your code base. The abstract class
useful to make all concrete implementation has same structure across different situation.

In Ponodo, there are two ways in binding, instance binding and class binding. We will go further
into each of them to learn how they build the Ponodo core, as well as extending Ponodo as you will.

### Instance Binding

First type of binding is an instance binding. Binding an instance will be shared through all
application. This will be also called as singleton. The memory address will be same when request
made, so you can refer to the same instance across all places in the application.

For easy use in all places, binding can be made through importing `app` from `ponodo.core`.

```python
from ponodo.core import app


app['foo'] = Foo()

```

This will tell instance of `Foo` class to be bind into `foo`, so you will be able to access the same
instance `Foo()` across all places inside application through resolving the `foo` from the container.


> If you inside a class that has access to `app` property, you have same controlled as above. Make
> sure the `app` property is instance of `ponodo.core.Application` class. Commonly, if you are
> extending the Ponodo class you will gain access to `app` property.
>
> ```python
> from ponodo.http import Controller
> 
> 
> class HomeController(Controller):
> 
>     def __init__(self):
>         
>         self.app['foo'] = Foo()
> 
> ```

### Class Binding

Not like instance binding, class binding assign the class itself. And will instantiate when
resolving. So in each resolving, it will have different memory allocation, it is not shared and you
cannot use it across all places in application.

```python
from ponodo.core import app

app['bar'] = Bar  # <- No paranthesis, which mean not instantiated yet.

```


## Resolving

Resolving mean you gain access to an instance from binding process. Resolving from the container 
must produces class instance. You can resolving using string or abstract class. Unlike binding, there
are three types of resolving, resolving from instance binding, resolving from class binding, and
resolving without binding.

### Resolving from Instance Binding

If you use first type of binding, which is binding an instance, you can resolve it with importing
`app` from `ponodo.core` and call it using square bracket (`[]`) as like you are accessing a 
dictionary data type.

```python
from ponodo.core import app

# bind it
app['foo'] = Foo()

# resolve it
foo = app['foo']

```

Sometimes resolving using method parantheses (`()`) is more convenient to give you access into
additional arguments, keyword arguments, and methods. But in this case we are not pass any of them.

```python
from ponodo.core import app

foo = app('foo')
```

### Resolving from Class Binding

Not like instance binding, which is singleton. In class binding, the instance will be crated when
resolving occur. So in each resolving, it will have different memory allocation, it is not shared
and you cannot use it across all places in application.

```python
from ponodo.core import app

# Bind it
app['bar'] = Bar  # <- No paranthesis, which mean the class not instantiated yet.

# Resolve it
bar = app('bar')
```

Behind the scene, this will instantiate `Bar` class and assign it into `bar` variable, the `bar`
variable will has the same value as `Bar()`.

#### Resolving With Constructor

In instance binding, you can pass the constructor argument before bind it into the container. But in
class binding, the instantiate process occur far after binding, which is when resolving. So, how we
pass constructor arguments when resolving?

You can pass the constructor arguments as keyword arguments in `app()` or using `.arguments()`
method. Please take a look in `Zoo` example below.

```python
class Zoo:

    def __init__(self, name):
        self.name = name

```

Normally instantiate `Zoo` class will be some like below, but how use it when resolving?

```python
zoo = Zoo('giraffe')

```

In Ponodo container, if you need the `arguments` within application container, you can call it using
keyword arguments or call it in chained method.

```python
# preferred using keyword arguments
zoo = app('zoo', name='giraffe')

# or using chained method
zoo = app('zoo').arguments(name='giraffe')

```

### Resolving Without Binding

Until this section, you will pass an abstract inside first `app` argument. Which can be a string or
abstract class. But you can also pass a concrete inside first `app` argument. In this case you no
need to bind concrete into abstract anymore.

```python
from ponodo.core import app 


class Baz:
    ...

# Without bind Baz into container, 
# you can resolve Baz directly
baz = app(Baz)
```
