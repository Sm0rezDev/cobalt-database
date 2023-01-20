import unittest
from cobalt import Cobalt


sample_database = {
    'devs': [  # Table
        {'id': '1', 'name': 'Simon', 'email': 'simon.wei@chasacademy.se', 'role': 'Developer'},
        {'id': '2', 'name': 'Saeed', 'email': 'saeed.sadeghighahroodi@chasacademy.se', 'role': 'Scrum master'},
        {'id': '3', 'name': 'Melina', 'email': 'melina.asplund@chasacademy.se', 'role': 'Developer'},
        {'id': '4', 'name': 'Mary', 'email': 'mary.makseu@chasacademy.se', 'role': 'Developer'},
        {'id': '5', 'name': 'Jannatul', 'email': 'jannatul.ferdoese@chasacademy.se', 'role': 'Developer'},],
    'client': [  # Table
        {'id': '1', 'name': 'Giacomo', 'email': 'gt@sarimner.com', 'role': 'Product owner'},]
}


cbd = Cobalt()

# Loads sample database.
[cbd.save(key, val) for key, val in sample_database.items()]


class TestDatabase(unittest.TestCase):

    def test_fetch_Wildcard(self):
        cbd.table = 'devs'
        self.assertEqual(cbd.fetch('', ''), cbd.data[cbd.table])

    def test_fetch_item_by_id(self):
        self.assertEqual(cbd.fetch('1', ''), [cbd.data[cbd.table][0]])

    def test_fetch_item_by_value(self):
        self.assertEqual(cbd.fetch('', 'name'), [val['name'] for val in cbd.data[cbd.table]])
