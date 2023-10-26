import requests
import hashlib
from getpass import getpass

def request_api_data(query_char):
    '''
    This function makes a request to the "Have I Been Pwned" API using the first 5 characters of an SHA-1 hash.
    It returns the API response which contains password hashes matching those 5 characters.
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url) 
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, check the API' )
    return res

def get_password_leaks_count(hashes, hash_to_check):
    '''
    This function processes the API response to determine how many times a specific password hash has been leaked.
    It compares the user's password hash (minus the first 5 characters) with the hashes in the API response.
    It returns the count of times the password has been exposed in data breaches.
    '''
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    ''' 
    This function converts a password into an SHA-1 hash, then uses the first 5 characters of that hash to make a query to the API.
    It then checks if the remainder of the hash is found in the API response, determining if the password has been compromised.
    It returns the full SHA-1 hash of the password.
    '''
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    print(get_password_leaks_count(response, tail))

    return sha1password

def main(password):
    pwned_api_check(password)
    pass

if __name__ == '__main__':
    password = getpass("Give me a string to evaluate how many times it has been liked:")
    main(password)