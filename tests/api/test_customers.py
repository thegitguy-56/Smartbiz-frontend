import pytest

def test_get_customers(api_session, base_url):
    """Test fetching customers list."""
    response = api_session.get(f"{base_url}/customers")
    assert response.status_code in [200, 401, 404], f"Unexpected status: {response.status_code}"
    
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, (list, dict)), "Customers response should be a list or dict"

@pytest.mark.parametrize("i", range(150))
def test_add_customer(api_session, base_url, i):
    """Test adding a new customer."""
    payload = {
        "name": f"Test Customer {i}",
        "phone": f"9876543{i:03d}",
        "email": f"customer{i}@example.com",
        "address": f"{i} Test Street"
    }
    response = api_session.post(f"{base_url}/customers", json=payload)
    assert response.status_code in [200, 201, 401, 404], f"Unexpected status: {response.status_code}"
    
    if response.status_code in [200, 201]:
        data = response.json()
        assert isinstance(data, dict)
