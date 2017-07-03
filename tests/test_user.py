import unittest
from models.user import User, Role
from app_factory import create_app
from extensions import db
from modules.user import create_user, delete_user, get_user, edit_user
from modules.funcs import verify_and_create_role

app = create_app()


class TestDB(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        self.test_user = {
            "username": "david",
            "password": "bowie",
            "email": "davidbowie@gmail.com",
            "name": "David Bowie",
            "role_id": 1
        }
        with app.test_request_context():
            db.create_all()
            verify_and_create_role("admin")
            verify_and_create_role("worker")
            create_user(self.test_user)

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()
            db.drop_all()

    def test_user_default(self):
        with app.test_request_context():
            assert len(User.query.all()) == 1
            assert len(Role.query.all()) == 2

    def test_user_delete(self):
        with app.test_request_context():
            delete_user(self.test_user['username'])
            assert len(User.query.filter_by(active=1).all()) == 0
            assert len(Role.query.all()) == 2

    def test_get_user(self):
        with app.test_request_context():
            _user = get_user(self.test_user['username'])
            assert _user

    def test_user_add(self):
        with app.test_request_context():
            user_data = {
                "username": "exengstfeld",
                "password": "heybuddy",
                "email": "exengstfeld@gmail.com",
                "name": "Eric Engstfeld",
                "role_id": 1
            }
            create_user(user_data)
            assert len(User.query.all()) == 2
            assert len(Role.query.all()) == 2

    def test_user_edit(self):
        with app.test_request_context():
            user_data = {
                "email": "david_bowie@gmail.com"
            }
            edit_user(self.test_user["username"], user_data)
            _david = get_user(self.test_user["username"])
            assert (_david.email == user_data["email"])
            assert len(User.query.all()) == 1
            assert len(Role.query.all()) == 2

if __name__ == '__main__':
    unittest.main()
