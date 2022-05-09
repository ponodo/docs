# Template Engine


## Introduction

Ponodo include a simple yet powerful templating engine. All templates are compiled into plain Python code and cached until they are modified, meaning this adds essentially zero overhead to your application. The template template files use the `.html` file extension and are typically stored in the `app/views` directory.

Views may be returned from routes or controllers using view method. Of course, as mentioned in the documentation on views, data may be passed using the view method's second argument:


```python
from ponodo.view import view

Route.get('/', lambda: view('greeting', {'name': 'Akung'}))
```

## Displaying Data

You may display data that is passed to your views by wrapping the variable in curly braces. For example, given the following route:

```python
Route.get('/', lambda: view('greeting', {'name': 'Akung'}))
```

You may display the contents of the name variable like so:

```python
Hello, {{ name }}
```

### HTML Entity Encoding

By default, `{{ }}` statements are automatically sent through Python's htmlspecialchars function to prevent XSS attacks. If you do not want your data to be escaped, you may use the following syntax:


```python
Hello, {{ name|e }}
# or
Hello, {{ name|escape }}
# or
Hello, {{ name|e('html') }}
# or
Hello, {{ name|escape('html') }}
```

## Directives

### If statements

You may construct if statements using the `@if`, `@elif`, `@else`, and `@endif` directives. These directives function identically to their Python counterparts:


```html
@if len(records) == 1:
    I have one record
@elif len(records) > 1:
    I have multiple records!
@else:
    I do not have any records!
@endif
```

For convenience, the template also provides an @unless directive:

```
@unless Auth.check():
    You are not sign in.
@endunless
```

### Switch statements

> Todo

### Loops
In addition to conditional statements, the template engine provides simple directives for working with Python's loop structures. Again, each of these directives functions identically to their Python counterparts:

```
@for item in collections:
    Show the {{ item }}
@endfor

@while True:
    Looping forever
@endwhile
```

### Including subviews

The `@include` directive allows you to include view from within another view. All variables that are available to the parent view will be made available to the included view:


```html
<div>
    @include('shared.errors')
 
    <form>
        <!-- Form Contents -->
    </form>
</div>
```

Even though the included view will inherit all data available in the parent view, you may also pass an array of additional data that should be made available to the included view:

```python
@include('view.name', {'status': 'complete'})
```

### Raw

In some situations, it's useful to embed Python code into your views. You can use the `@py` directive to execute a block of plain Python within your template:

```python
@py
    counter = 1
@endpy
```

### Comments

This template engine also allows you to define comments in your views. However, unlike HTML comments, the template comments are not included in the HTML returned by your application:

```html
{{-- This comment will not be present in the rendered HTML --}}
```

## Building Layouts

Layouts may also be created via "template inheritance". This was the primary way of building applications.

To get started, let's take a look at a simple example. First, we will examine a page layout. Since most web applications maintain the same general layout across various pages, it's convenient to define this layout as a single view:

```html
<html>
    <head>
        <title>App Name - @yield('title')</title>
    </head>
    <body>
        @section('sidebar')
            This is the master sidebar.
        @show
 
        <div class="container">
            @yield('content')
        </div>
    </body>
</html>
```

As you can see, this file contains typical HTML mark-up. However, take note of the `@section` and `@yield` directives. The `@section` directive, as the name implies, defines a section of content, while the `@yield` directive is used to display the contents of a given section.

Now that we have defined a layout for our application, let's define a child page that inherits the layout.

When defining a child view, use the `@extends` directive to specify which layout the child view should "inherit". Views which extend a layout may inject content into the layout's sections using `@section` directives. Remember, as seen in the example above, the contents of these sections will be displayed in the layout using `@yield`:

```html
@extends('layouts.app')
 
@section('title', 'Page Title')
 
@section('sidebar')
    @parent
 
    <p>This is appended to the master sidebar.</p>
@endsection
 
@section('content')
    <p>This is my body content.</p>
@endsection
```

In this example, the sidebar section is utilizing the `@parent` directive to append (rather than overwriting) content to the layout's sidebar. The `@parent` directive will be replaced by the content of the layout when the view is rendered.

The `@yield` directive also accepts a default value as its second parameter. This value will be rendered if the section being yielded is undefined:

```
@yield('content', 'Default content')
```

## Forms
### CSRF field

Anytime you define an HTML form in your application, you should include a hidden CSRF token field in the form so that the CSRF protection middleware can validate the request. You may use the `@csrf` directive to generate the token field:

```html
<form method="POST" action="/profile">
    @csrf
 
    ...
</form>
```

### Method field

Since HTML forms can't make `PUT`, `PATCH`, or `DELETE` requests, you will need to add a hidden `_method` field to spoof these HTTP verbs. The `@method` directive can create this field for you:

```html
<form action="/foo/bar" method="POST">
    @method('PUT')
 
    ...
</form>
```


## Stacks

allows you to push to named stacks which can be rendered somewhere else in another view or layout. This can be particularly useful for specifying any JavaScript libraries required by your child views:

```
@push('scripts')
    <script src="/example.js"></script>
@endpush
```

You may push to a stack as many times as needed. To render the complete stack contents, pass the name of the stack to the @stack directive:


```html
<head>
    <!-- Head Contents -->
 
    @stack('scripts')
</head>
```
