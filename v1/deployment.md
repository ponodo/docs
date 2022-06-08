# Deployment


## Gunicorn

```shell
gunicorn -w 4 -b 0.0.0.0:5000 your_project:app
```

The -w 4 option uses 4 workers to handle 4 requests at once. The -b 0.0.0.0:5000 serves the application on all interfaces on port 5000.

Gunicorn provides many options for configuring the server, either through a configuration file or with command line options. Use gunicorn --help or see the docs for more information.

The command expects the name of your module or package to import and the application instance within the module. If you use the application factory pattern, you can pass a call to that.