import json
import unittest

from fastapi.security import HTTPBasicCredentials
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestMainCase(unittest.TestCase):
    def test_now_endpoint(self):

        response = client.get("/v1/now")
        data = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 200)
        self.assertTrue("now" in data)

    def test_vip_coords_correct(self):
        credentials = HTTPBasicCredentials(username="user1", password="111")
        response = client.get("/v1/VIP/5", auth=(credentials.username, credentials.password))

        data = json.loads(response.content.decode())
        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("gpsCoords" in data)
        self.assertTrue("lat" in data["gpsCoords"] and "long" in data["gpsCoords"])

if __name__ == '__main__':
    unittest.main()
