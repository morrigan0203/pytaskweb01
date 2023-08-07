import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def auth():
    auth_data = {"username": data["username"], "email": data["email"], "password": data["password"]}
    r = requests.post(url=f'{data["site"]}{data["login_path"]}', data=auth_data)
    return r.json()["token"], r.status_code


def get_title_posts_page(token, page, not_own=True):
    res = []
    req_data = {"order": "DESC", "page": page}
    if not_own:
        req_data["owner"] = "notMe"
    headers = {"X-Auth-Token": token}
    r = requests.get(url=f'{data["site"]}{data["get_posts_path"]}', params=req_data, headers=headers)
    j = r.json()
    posts = j["data"]
    next = j["meta"]["nextPage"]
    count = j["meta"]["count"]

    for i in range(len(posts)):
        res.append(posts[i]["title"])
    return res, next, count


def get_all_title_posts(token):
    next = 0
    res = []
    while next is not None:
        pageTitles, next, count = get_title_posts_page(token, next)
        res.extend(pageTitles)
        print(next, pageTitles)
    return res


def create_post(token, title, description, content):
    create_data = {"title": title, "description": description, "content": content}
    headers = {"X-Auth-Token": token}
    r = requests.post(url=f'{data["site"]}{data["create_post_path"]}', data=create_data, headers=headers)
    j = r.json()
    return j


if __name__ == "__main__":
    tkn = auth()[0]
    print(tkn)
    # print(get_title_posts_page(tkn, 9769))
    # print(get_all_title_posts(tkn))
    print(create_post(tkn, "title", "description", "test content"))

