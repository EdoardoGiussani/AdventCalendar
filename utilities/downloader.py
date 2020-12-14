import requests
from github3 import login

def GetUrl():
    print('Url of the day:')
    url = input()
    return url

def GetSession(url):
    s = requests.Session()
    s.get(url)
    return s

def GitHubLogin(session, url):
    session.post(url, data={'login_field': '', 'password': ''}, allow_redirects=True)

def GetContent(session, url):
    r = session.get(url)
    content = r.content.decode('utf-8')
    return content

def WriteFile(content):
    with open('downloader\\pageTemplate.txt', 'w') as f:
        f.write(content)

def ReadTemplatePage():
    with open('downloader\\pageTemplate.txt', 'r') as f:
        content = f.read()
    return content

def ExtractPage(content):
    start = content.find('<article class="day-desc">')
    end = content.find('')


if __name__ == "__main__":
    url = GetUrl()
    session = GetSession(url)
    GitHubLogin(session, url)
    content = GetContent(session, url)
    WriteFile(content)

    url = GetUrl()
    content = GetContent(session, url)
    WriteFile(content)
    #content = ReadTemplatePage()
    #page = ExtractPage(content)