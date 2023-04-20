import os
import time
import json
import unittest
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from database import User, update_user, get_user, create_user
from main import app

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///test.db')
        params = {"db_file":'test.db', "age": 20, "income": 1000, "physiological_need": "food", "safety_need": "shelter", "love_and_belonging_need": "friendship", "esteem_need": "respect", "self_actualization_need": "self-actualization"}
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        create_user(**params)

    def tearDown(self):
        self.session.close()
        self.engine.dispose()
        os.remove("test.db")

    def test_get_user(self):
        user = get_user(db_file='test.db', user_id=1)
        assert user == {"id": 1, "age": 20, "income": 1000, "physiological_need": "food", "safety_need": "shelter", "love_and_belonging_need": "friendship", "esteem_need": "respect", "self_actualization_need": "self-actualization"}, response

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


class TestAPI(unittest.TestCase):
    def setUp(self):
        params = {"db_file":'test.db', "age": 20, "income": 1000, "physiological_need": "food", "safety_need": "shelter", "love_and_belonging_need": "friendship", "esteem_need": "respect", "self_actualization_need": "self-actualization"}
        create_user(**params)
        self.client = TestClient(app)

    def tearDown(self):
        os.remove("test.db")

    def test_create_user_route(self):
        response = self.client.get("/create_user?db_file=test.db&age=20&income=1000&physiological_need=food&safety_need=shelter&love_and_belonging_need=friendship&esteem_need=respect&self_actualization_need=self-actualization")
        
        response.raise_for_status()
        assert response.status_code == 200, response.status_code
        response_dict = json.loads(response.json())
        assert int(response_dict["id"]) > 0, response.json()

    def test_get_user_route(self):
        response = self.client.get("/get_user?db_file=test.db&user_id=1")
        assert response.status_code == 200, response.status_code
        response_dict = json.loads(response.json())
        assert response_dict == {"id": "1", "age": '20', "income": '1000', "physiological_need": "food", "safety_need": "shelter", "love_and_belonging_need": "friendship", "esteem_need": "respect", "self_actualization_need": "self-actualization"}, response_dict

    def test_update_user_route(self):
        response = self.client.get("/update_user?db_file=test.db&user_id=1&age=21&income=2000&physiological_need=food&safety_need=shelter&love_and_belonging_need=friendship&esteem_need=respect&self_actualization_need=self-actualization")
        
        response.raise_for_status()
        assert response.status_code == 200, response.status_code


if __name__ == '__main__':
    unittest.main()