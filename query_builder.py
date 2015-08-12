
class QueryBuilder:

    def __init__(self):
        self.column = '*'
        self.table = None
        self.where_column = None
        self.where_value = None

    def select(self, column):
        self.column = column
        return self

    def from_table(self, table):
        self.table = table
        return self

    def where(self, where_column, where_value):
        self.where_column = where_column
        self.where_value = where_value
        return self

    def generate_sql(self):
        sql = 'SELECT {column} FROM {table}'

        if self.where_column and self.where_value:
            sql += ' WHERE {where_column}={where_value}'

        return sql.format(**self.__dict__) + ';'
