import requests
from dataclasses import dataclass


API_URL = "https://api.github.com/search/repositories?q="


@dataclass
class Item:
    id: int
    name: str
    full_name: str

    @staticmethod
    def from_dict(d: dict) -> "Item":
        return Item(id=d["id"], name=d["name"], full_name=d["full_name"])


@dataclass
class ResponseType:
    total_count: int
    incomplete_results: bool
    items: list[Item]

    @staticmethod
    def from_dict(d: dict) -> "ResponseType":
        return ResponseType(
            total_count=d["total_count"],
            incomplete_results=d["incomplete_results"],
            items=[Item.from_dict(i) for i in d["items"]],
        )


def get_repositories(language: str):
    query = f"language:{language}+sort:stars"
    url = API_URL + query
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    response = ResponseType.from_dict(r.json())
    print(response.total_count)
    print(response.items[0].full_name)


if __name__ == "__main__":
    get_repositories("python")
