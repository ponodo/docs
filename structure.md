# Directory Structure

The blog directory will have a number of generated files and folders that make up the structure of a Rails application. Most of the work in this tutorial will happen in the app folder, but here's a basic rundown on the function of each of the files and folders that Rails creates by default:

- app
    + controllers
    + models
    + view
        - layouts
    + providers
- config
- db
    + migrations
- public
- storage
    + log
- tests
- routes

## Custom directory

If you wish to organize your application by domain application. Each domain has its own structure.


- domains
    + domain_1
        - app
            + controllers
            + models
            + view
        - db
            + migrations
        - tests
        - routes
    + domain_2
        - app
            + controllers
            + models
            + view
        - db
            + migrations
        - tests
        - routes
- config
- routes
- storage
    + log

In each domain you must create service provider and register it inside `config/app.py`