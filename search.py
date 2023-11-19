import requests
from bs4 import BeautifulSoup

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def get_top_search_result(query):
    search_result = search_google(query)
    
    if search_result:
        soup = BeautifulSoup(search_result, "html.parser")
        top_result = soup.find("div", class_="tF2Cxc").find("a").get('href')
        return top_result
    else:
        return "No search results found."

def main():
    user_query = input("Enter something to search on Google: ")
    top_result = get_top_search_result(user_query)
    print(f"Top result for '{user_query}': {top_result}")

if __name__ == "__main__":
    main()
