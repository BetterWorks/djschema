from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as Base


class DatabaseWrapper(Base):

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

        schema = self.settings_dict.get('SCHEMA')
        if schema:
            self._init_sql = '''
                CREATE SCHEMA IF NOT EXISTS "{schema}";SET SCHEMA '{schema}';
                '''.format(schema=schema)
        else:
            self._init_sql = None

    def init_connection_state(self):
        super(DatabaseWrapper, self).init_connection_state()

        if self._init_sql:
            with self.connection.cursor() as c:
                c.execute(self._init_sql)

            if not self.get_autocommit():
                self.connection.commit()
