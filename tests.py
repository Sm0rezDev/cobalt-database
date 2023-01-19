import unittest
from cobalt import Cobalt


sample_database = {
    'devs': [  # Table
        {'name': 'Simon', 'email': 'simon.wei@chasacademy.se', 'role': 'Developer'},
        {'name': 'Saeed', 'email': 'saeed.sadeghighahroodi@chasacademy.se', 'role': 'Scrum master'},
        {'name': 'Melina', 'email': 'melina.asplund@chasacademy.se', 'role': 'Developer'},
        {'name': 'Mary', 'email': 'mary.makseu@chasacademy.se', 'role': 'Developer'},
        {'name': 'Jannatul', 'email': 'jannatul.ferdoese@chasacademy.se', 'role': 'Developer'},
    ]
}


class TestDatabase(unittest.TestCase):

    def test_select(self):
        cbd = Cobalt()

        [cbd.save(key, obj) for key, obj in sample_database.items()]

        # for key, obj in sample_database.items():
        #     for item in obj:
        #         self.assertEqual(cbd.select(key, item), sample_database[key][item])

        results = cbd.execute('SELEC * FROM DEVS')
        self.assertEqual(results, sample_database['devs'])