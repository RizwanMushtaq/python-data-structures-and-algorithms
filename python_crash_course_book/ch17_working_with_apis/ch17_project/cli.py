import requests
from dataclasses import dataclass
import plotly.express as px


API_URL = "https://api.github.com/search/repositories?q="


@dataclass
class Repository:
    id: int
    name: str
    owner: str
    stargazers_count: int
    html_url: str
    description: str

    @staticmethod
    def from_dict(d: dict) -> "Repository":
        return Repository(
            id=d["id"],
            name=d["name"],
            owner=d["owner"]["login"],
            stargazers_count=d["stargazers_count"],
            html_url=d["html_url"],
            description=d["description"],
        )


@dataclass
class ResponseType:
    total_count: int
    incomplete_results: bool
    repositorys: list[Repository]

    @staticmethod
    def from_dict(d: dict) -> "ResponseType":
        return ResponseType(
            total_count=d["total_count"],
            incomplete_results=d["incomplete_results"],
            repositorys=[Repository.from_dict(i) for i in d["items"]],
        )


def get_repositories(language: str) -> list[Repository]:
    query = f"language:{language}+sort:stars"
    url = API_URL + query
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("api fetching data failed!")
    response = ResponseType.from_dict(r.json())
    return response.repositorys


def main():
    respositories = get_repositories("python")
    print(respositories[0])
