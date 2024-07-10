from infi.clickhouse_orm.fields import Field


class BoolField(Field):
    db_type = 'Bool'

    def to_python(self, value, timezone_in_use):
        if value == 'true':
            return True
        elif value == 'false':
            return False
        else:
            raise ValueError('Invalid value for BoolField: ' + value)

    def to_db_string(self, value, quote=True):
        if value is True:
            return 'true'
        elif value is False:
            return 'false'
        else:
            raise ValueError('Invalid value for BoolField: ' + str(value))
