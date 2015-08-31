from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as Base

from .introspection import DatabaseIntrospection


class DatabaseWrapper(Base):

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

        self.schema = self.settings_dict.get('SCHEMA', 'public')
        if self.schema == 'public':
            self._init_sql = None
        else:
            self._init_sql = '''
                CREATE SCHEMA IF NOT EXISTS "{schema}";SET SCHEMA '{schema}';
                '''.format(schema=self.schema)

        self.introspection = DatabaseIntrospection(self)

    def init_connection_state(self):
        super(DatabaseWrapper, self).init_connection_state()

        if self._init_sql:
            with self.connection.cursor() as c:
                c.execute(self._init_sql)

            if not self.get_autocommit():
                self.connection.commit()
