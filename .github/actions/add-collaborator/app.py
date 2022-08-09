#https://realpython.com/api-integration-in-python/

import requests
from requests.auth import AuthBase
import traceback
import json
import argparse

api_base_url = "https://api.github.com/repos"

headers = {
    'Accepts': 'application/vnd.github+json'
    }

body = {
    "permission": "push"
}

class GithubTokenAuth(AuthBase):
    def __init__(self,token):
        self.token = token
    def __call__(self,req):
        req.headers['Authorization'] = 'token ' + self.token
        return req
class StripArgument(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.strip())

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", help = "Repository name to add collaborator into in format owner/repo", default="radoscis/gh-custom-actions", action=StripArgument)
    parser.add_argument("-c", "--collaborator", help ="Collaborator username", default="piotrjanis", action=StripArgument)
    parser.add_argument("-t", "--token", help ="Authentication token", required=True, action=StripArgument)
    args = parser.parse_args()
    return args

def start():
    args = parseArguments()
    makeRequest(args.repo,args.collaborator,args.token)

def makeRequest(repo,collaborator, token):
    request_url = f"{api_base_url}/{repo}/collaborators/{collaborator}"
    try:
        response = requests.put(
            url=request_url,
            headers=headers,
            json=body,
            auth=GithubTokenAuth(token)
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError as err:
        print('Connection Error occured !')
        traceback.print_exc()
        raise SystemExit(err)
    except requests.exceptions.ConnectTimeout as err:
        print('Connection Timeout occured !')
        traceback.print_exc()
        raise SystemExit(err)
    except requests.exceptions.HTTPError as err:
        print('HTTP Err occured !')
        traceback.print_exc()
        raise SystemExit(err)
    except Exception as err:
        print('Other Exception Occured !')
        traceback.print_exc()
        raise SystemExit(err)
    finally:
        print(f"::set-output name=response::{json.dumps(response.json(),sort_keys=True, indent=2)}")

if __name__ == '__main__':
    start()


# owner = "radoscis"
# repo = "gh-custom-actions"
# collaborator = "piotrjanis"
# token = "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"




