# djschema
Django Postgres Schema Isolation

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

