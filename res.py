import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, source):
        self.source = source
        
    
    def get_response(self):
        # Open the file and read the content line by line
        try:
            f = open(self.source, "r")

            for line in f:
                # Strip any leading/trailing whitespaces, including newlines
                subdomain = line.strip()

                try:
                    # Join the subdomain with the domain name to form the URL
                    url = f"https://{subdomain}"
                    # print(url)

                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, 'html.parser')

                    if r.status_code == 200:
                        print(f"Title: {soup.title.string} ", end= "")
                        print(f"URL  : {subdomain} ")
                      
                    # else:
                    #     print(soup.title.name)
                    #     print(r.status_code)

                except Exception:
                    pass

        except KeyboardInterrupt:
                    print(f"keyboard interrupted by user")
    
                
if __name__ == "__main__":
    server = Content("list-subdomain-urls")
    server.get_response()
