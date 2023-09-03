import pytest
from  rest_framework.test import APIClient
import time
from rest_framework import status

# client = APIClient()
def test():
    assert 2==2





def test_array_gen():
    client = APIClient()
    url = '/array/'
    payload = {
        "sentence" : f"this is test entry - {time.time()}"
    }
    response = client.post(url, payload)
    print(f"Printing the resposne --- {response}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response['array']) == 500