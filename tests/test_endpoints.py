import unittest
import status
from datetime import datetime
from application.api.truck.business import create_trucker, delete_trucker, update_trucker

class TestEndpoints(unittest.TestCase):

    def test_trucker_insert_response_201(self):
        data = {
            "age": 0,
            "cnh": "string",
            "created_at": datetime.utcnow(),
            "destiny": "string",
            "gender": 0,
            "id": 0,
            "name": "string",
            "origin": "string",
            "owner_truck": 0,
            "truck_type": 0,
            "truckload": 0
        }
        response = create_trucker(data)
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)

    def test_trucker_update_response_204(self):
        id = 2
        data = {
            "age": 0,
            "cnh": "string",
            "created_at": datetime.utcnow(),
            "destiny": "string",
            "gender": 0,
            "id": 0,
            "name": "string",
            "origin": "string",
            "owner_truck": 0,
            "truck_type": 0,
            "truckload": 0
        }
        response = update_trucker(id, data)
        self.assertTrue(response.status_code == status.HTTP_204_NO_CONTENT)

    def test_trucker_update_response_404(self):
        id = 1
        data = {
            "age": 0,
            "cnh": "string",
            "created_at": datetime.utcnow(),
            "destiny": "string",
            "gender": 0,
            "id": 0,
            "name": "string",
            "origin": "string",
            "owner_truck": 0,
            "truck_type": 0,
            "truckload": 0
        }
        response = update_trucker(id, data)
        self.assertTrue(response.status_code == status.HTTP_404_NOT_FOUND)

    def test_trucker_delete_response_204(self):
        response = delete_trucker(1)
        self.assertTrue(response.status_code == status.HTTP_204_NO_CONTENT)


if __name__ == '__main__':
    unittest.main()