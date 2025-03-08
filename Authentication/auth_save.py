from playwright.sync_api import sync_playwright
import requests

def save_auth_state():
    with sync_playwright() as p:
        context = browser.new_context()

        # # Open login page
        # page = context.new_page()
        # page.goto("https://the-internet.herokuapp.com/login")
        # 1. Make API call to login
        response = requests.post(
                'https://reqres.in/api/login',
            data={
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
        )
        token = response.json() # Assuming the API returns a token

        print(token)

        # # Perform login
        # page.fill("#username", "tomsmith")
        # page.fill("#password", "SuperSecretPassword!")
        # page.click(".radius")
         # 2. Set the token in the browser context (Authorization header)
         
        context.add_init_script(f"""
            window.localStorage.setItem('auth_token', '{token}');
        """)
        
        # Optionally, you can also add cookies if needed
        # context.add_cookies([{
        #     'name': 'auth_token',
        #     'value': token,
        #     'url': 'https://example.com'
        # }])

        # Save authentication state
        context.storage_state(path="auth.json")

        print("✅ Authentication state saved!")
        browser.close()

# Run this function once to save login session
save_auth_state()
