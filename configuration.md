# Configuration

## Introduction

All of the configuration files for the Ponodo framework are stored in the `config` directory. Each option is documented, so feel free to look through the files and get familiar with the options available to you.

These configuration files allow you to configure things like your database connection information, ...

## Environment Configuration

It is often helpful to have different configuration values based on the environment where the application is running. For example, you may wish to use a different cache driver locally than you do on your production server.

To make this a cinch, Ponodo utilizes the ... library. In a fresh Ponodo installation, the root directory of your application will contain a .env.example file that defines many common environment variables. During the Ponodo installation process, this file will automatically be copied to .env.

Ponodo's default .env file contains some common configuration values that may differ based on whether your application is running locally or on a production web server. These values are then retrieved from various Ponodo configuration files within the config directory using Ponodo's env function.

If you are developing with a team, you may wish to continue including a .env.example file with your application. By putting placeholder values in the example configuration file, other developers on your team can clearly see which environment variables are needed to run your application.

> Any variable in your .env file can be overridden by external environment variables such as server-level or system-level environment variables.

### Environment file security

Your .env file should not be committed to your application's source control, since each developer / server using your application could require a different environment configuration. Furthermore, this would be a security risk in the event an intruder gains access to your source control repository, since any sensitive credentials would get exposed.

## Environment Variable Types

All variables in your .env files are typically parsed as strings, so some reserved values have been created to allow you to return a wider range of types from the env() function:

...

If you need to define an environment variable with a value that contains spaces, you may do so by enclosing the value in double quotes:

```
APP_NAME="My Awesome Application"
```

### Retrieving Environment Configuration

All of the variables listed in this file will be loaded into the $_ENV PHP super-global when your application receives a request. However, you may use the env helper to retrieve values from these variables in your configuration files. In fact, if you review the Ponodo configuration files, you will notice many of the options are already using this helper:

The second value passed to the env function is the "default value". This value will be returned if no environment variable exists for the given key.

### Determining The Current Environment

## Accessing Configuration Values

You may easily access your configuration values with importing `config` function from `ponodo.config` in your application. The configuration values may be accessed using "dot" syntax, which includes the name of the file and option you wish to access. A default value may also be specified and will be returned if the configuration option does not exist:

```python
from ponodo.config import config

value = config('database.name')

# Retrieve a default value if the configuration value does not exist
value = config('database.name', default='awesome')
```