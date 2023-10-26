# Password Breach Checker

This script helps you determine if a particular password has been exposed in any known data breaches using the 'Have I Been Pwned' API.

## Description

The script uses the SHA-1 hash of the password and only sends the first 5 characters of this hash to the API. The API then returns a list of all hashes that match these first 5 characters. The script checks this list locally to find out if the full hash (and therefore the password) has been exposed. This approach ensures that the full password hash (or the password itself) is never exposed to the API.

## How to Use

1. Ensure you have the `requests` library installed. You can install it using pip:
   ```
   pip install requests
   ```

2. Run the script:
   ```
   python checkmypass.py
   ```

3. When prompted, enter the password you want to check. The password won't be displayed on screen for security reasons.

4. The script will then inform you whether the password has been exposed in any known breaches.

## Functions

- `request_api_data(query_char)`: Makes a request to the API with the first 5 characters of the password's hash.
  
- `get_password_leaks_count(hashes, hash_to_check)`: Checks the list of returned hashes against the tail of the user's password hash.
  
- `pwned_api_check(password)`: Converts the password to a SHA-1 hash and uses the above two functions to check for breaches.

- `main(password)`: The main driver function that invokes the password check.

## Note

Always ensure that you are using a secure and private connection when running scripts that deal with sensitive information, like passwords.
