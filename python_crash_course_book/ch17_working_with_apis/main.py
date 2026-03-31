import requests
from dataclasses import dataclass


API_URL = "https://api.github.com/search/repositories?q="


@dataclass
class Item:
    id: int
    name: str
    full_name: str


@dataclass
class ResponseType:
    total_count: int
    incomplete_results: bool
    items: list[Item]


def get_repositories(language: str):
    query = f"language:{language}+sort:stars"
    url = API_URL + query
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    response_dict: ResponseType = r.json()
    print(response_dict["items"][0].keys())


if __name__ == "__main__":
    get_repositories("python")
