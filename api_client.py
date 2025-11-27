import requests

def fetch_and_display_users(num_users):
    """
    Fetches users from JSONPlaceholder API and displays their name, email, and city.
    Handles network errors, non-200 responses, and missing keys.
    """
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)  # timeout to avoid hanging
        response.raise_for_status()  # Raises HTTPError for non-200 responses
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None

    try:
        users = response.json()
        for i, user in enumerate(users[:num_users]):
            name = user.get("name", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")
            print(f"{i+1}. Name: {name}, Email: {email}, City: {city}")
    except (ValueError, TypeError) as e:
        print(f"Error parsing JSON data: {e}")
        return None



if __name__ == "__main__":
    print("Fetching 3 users:")
    fetch_and_display_users(3)

    print("\nFetching 15 users (testing out-of-bounds):")
    fetch_and_display_users(15)
