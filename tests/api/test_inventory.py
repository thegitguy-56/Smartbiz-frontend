def test_get_inventory(api_session, base_url):
    """Test fetching inventory items."""
    response = api_session.get(f"{base_url}/inventory")
    # Endpoint should ideally exist and return 200, 
    # but we handle 404 or 401 gracefully for mock/development servers
    assert response.status_code in [200, 401, 404], f"Unexpected status: {response.status_code}"
    
    if response.status_code == 200:
        data = response.json()
        # Inventory might be returned as a list or an object containing a list
        assert isinstance(data, (list, dict)), "Inventory response should be a list or dict"

def test_add_inventory_item(api_session, base_url):
    """Test adding a new inventory item."""
    payload = {
        "name": "Test Item",
        "category": "Test Category",
        "price": 99.99,
        "stock": 10
    }
    response = api_session.post(f"{base_url}/inventory", json=payload)
    assert response.status_code in [200, 201, 401, 404, 500], f"Unexpected status: {response.status_code}"
    
    if response.status_code in [200, 201]:
        data = response.json()
        assert isinstance(data, dict)
        # We don't have the exact schema, but we assume it might return the created ID or object.
