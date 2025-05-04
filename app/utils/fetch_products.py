import requests

def get_products():
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            return response.json()
        else:
            print("⚠️ Error: The response content is not in JSON format.")
            return []
    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️ HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout:
        print("⚠️ The request timed out.")
    except requests.exceptions.RequestException as req_err:
        print(f"⚠️ Error fetching products: {req_err}")
    
    return []
