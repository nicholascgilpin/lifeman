import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import User, update_user, get_user, create_user

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///test.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        create_user(engine_string='sqlite:///test.db', age=25, income=50000, physiological_need='food', safety_need='shelter', love_and_belonging_need='friendship', esteem_need='respect', self_actualization_need='creativity')

    def tearDown(self):
        self.session.close()
        self.engine.dispose()
        os.remove("test.db")

    def test_get_user(self):
        user = get_user(db_file='test.db', user_id=1)
        assert user.age == 25
        assert user.income == 50000
        assert user.physiological_need == 'food'
        assert user.safety_need == 'shelter'
        assert user.love_and_belonging_need == 'friendship'
        assert user.esteem_need == 'respect'
        assert user.self_actualization_need == 'creativity'

    def test_update_user(self):
        update_user(db_file='test.db', user_id=1, age=30, income=60000, physiological_need='water', safety_need='security', love_and_belonging_need='family', esteem_need='confidence', self_actualization_need='knowledge')
        user = self.session.query(User).filter_by(age=30).first()
        assert user.age == 30
        assert user.income == 60000
        assert user.physiological_need == 'water'
        assert user.safety_need == 'security'
        assert user.love_and_belonging_need == 'family'
        assert user.esteem_need == 'confidence'
        assert user.self_actualization_need == 'knowledge'

if __name__ == '__main__':
    unittest.main()