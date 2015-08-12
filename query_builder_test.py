import unittest
from query_builder import QueryBuilder

class QueryBuilderTest(unittest.TestCase):

    def setUp(self):
        self.builder = QueryBuilder()

    def test_select_column_from_table(self):
        self.builder.select('account_name').from_table('account')

        sql = self.builder.generate_sql()
        self.assertEqual('SELECT account_name FROM account;', sql)

    def test_select_star_from_table(self):
        self.builder.select('*').from_table('account')

        sql = self.builder.generate_sql()
        self.assertEqual('SELECT * FROM account;', sql)

    def test_column_defaults_to_start(self):
        self.builder.from_table('account')

        sql = self.builder.generate_sql()
        self.assertEqual('SELECT * FROM account;', sql)

    def test_select_with_where_clause(self):
        self.builder.select('account_name').from_table('account').where('account_id', 13977)

        sql = self.builder.generate_sql()
        self.assertEqual('SELECT account_name FROM account WHERE account_id=13977;', sql)

if __name__ == '__main__':
    unittest.main()
