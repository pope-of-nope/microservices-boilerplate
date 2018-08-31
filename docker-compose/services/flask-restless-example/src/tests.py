import requests
from models import Collection, Document


def URL(path):
    # HOST = "http://localhost:5000/documents/api"
    HOST = "http://127.0.0.1:5000/"
    return "{host}/{path}".format(host=HOST.rstrip("/"), path=path.lstrip("/"))


def test_collections():
    def get_list():
        url = URL(Collection.list_url())
        # url = URL("/v1/collections")
        # print(url)
        res = requests.get(url)
        assert res.status_code == 200, res.status_code
        return res.json()["objects"]

    def get_item(id):
        # url = URL("/v1/collections")
        url = URL(Collection.details_url(id))
        print(url)
        res = requests.get(url)
        assert res.status_code == 200, res.status_code
        return res.json()

    for item in get_list():
        get_item(item["id"])


if __name__ == '__main__':
    test_collections()
