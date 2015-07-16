# djschema
Django Postgres Schema Isolation
.. image:: https://img.shields.io/pypi/v/django-redis.svg?style=flat
    :target: https://pypi.python.org/pypi/django-redis

# usage
Change the Django database ENGINE to 'djschema' and set SCHEMA to be the name of the schema you want to use.

```
'default': {
    'ENGINE': 'djschema',
    'SCHEMA': 'schema_name',
    'NAME': 'database',
    'HOST': '127.0.0.1',
    'PORT': '8458'
}
```

