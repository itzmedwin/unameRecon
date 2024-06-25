import requests
import threading
import time
from websites import urls

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'

class uname:
    def __init__(self, name, urls):
        self.name = name
        self.urls = urls
    
    def check_url(self, url):
        try:
            full_url = f'{url}{self.name}'
            resp = requests.get(full_url)
            if resp.status_code == 200:
                print(f"Found available site {full_url} with code: {GREEN}{resp.status_code}{WHITE}")
            elif resp.status_code == 301:
                print(f"Redirect detected {full_url} with code: {YELLOW}{resp.status_code}{WHITE}")
            elif resp.status_code == 403:
                print(f"No permission to access {full_url} with error: {RED}{resp.status_code}{WHITE}")
            else:
                pass
        except requests.exceptions.RequestException as e:
            print(':sadge:')

    def check(self):
        threads = []
        for url in self.urls:
            thread = threading.Thread(target=self.check_url, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
if __name__ == '__main__':
    username = input("Enter username: ")
    uname(username, urls).check()


