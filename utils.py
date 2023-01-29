import requests
import json
import sqlite3
import pandas as pd



def get_user_profile(username):
    url = "https://leetcode.com/graphql/"

    payload = json.dumps({
    "query": "\n    query recentAcSubmissions($username: String!, $limit: Int!) {\n  recentAcSubmissionList(username: $username, limit: $limit) {\n    id\n    title\n    titleSlug\n    timestamp\n  }\n}\n    ",
    "variables": {
        "username": username,
        "limit": 1
    }
    })
    headers = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': '',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'csrftoken=gD78nsWDHzXWmhIoYyFi4J8TDATUDLk4WgUkA8ID9CcBDMBJmvN8O2Sq048osIul; gr_user_id=d7245a98-fdb9-4ca7-a444-674cf95129f9; 87b5a3c3f1a55520_gr_session_id=dee1db2a-f548-4573-bc07-ff40ef16d7a9; 87b5a3c3f1a55520_gr_session_id_dee1db2a-f548-4573-bc07-ff40ef16d7a9=true; _gid=GA1.2.1942280488.1674988597; _gat=1; _ga=GA1.1.1037758665.1674988597; _ga_CDRWKZTDEX=GS1.1.1674988596.1.0.1674988600.0.0.0; _dd_s=rum=1&id=974bee0a-8720-4986-8e68-98e9afb77cbc&created=1674988595478&expire=1674989501479; csrftoken=2JpuNBL3KcoJVAxExt4qDltUe3ORWPj2CSZQ18h06dCHa8bvY3sfyz46VJvA6H7U',
        'dnt': '1',
        'origin': 'https://leetcode.com',
        'pragma': 'no-cache',
        'random-uuid': '9e74ea68-689d-8412-92b0-9e30528635d7',
        'referer': 'https://leetcode.com/Navneet_jain_0154/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-csrftoken': 'gD78nsWDHzXWmhIoYyFi4J8TDATUDLk4WgUkA8ID9CcBDMBJmvN8O2Sq048osIul'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()
    

def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()


def get_problem_data(titleSlug):

    url = "https://leetcode.com/graphql/"
    
    payload = json.dumps({
    'query': '\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n  }\n}\n    ',
         'variables': {
        'titleSlug': titleSlug,
        },
    })

    headers = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': '',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'csrftoken=gD78nsWDHzXWmhIoYyFi4J8TDATUDLk4WgUkA8ID9CcBDMBJmvN8O2Sq048osIul; gr_user_id=d7245a98-fdb9-4ca7-a444-674cf95129f9; 87b5a3c3f1a55520_gr_session_id=dee1db2a-f548-4573-bc07-ff40ef16d7a9; 87b5a3c3f1a55520_gr_session_id_dee1db2a-f548-4573-bc07-ff40ef16d7a9=true; _gid=GA1.2.1942280488.1674988597; _gat=1; _ga=GA1.1.1037758665.1674988597; _ga_CDRWKZTDEX=GS1.1.1674988596.1.0.1674988600.0.0.0; _dd_s=rum=1&id=974bee0a-8720-4986-8e68-98e9afb77cbc&created=1674988595478&expire=1674989501479; csrftoken=2JpuNBL3KcoJVAxExt4qDltUe3ORWPj2CSZQ18h06dCHa8bvY3sfyz46VJvA6H7U',
        'dnt': '1',
        'origin': 'https://leetcode.com',
        'pragma': 'no-cache',
        'random-uuid': '9e74ea68-689d-8412-92b0-9e30528635d7',
        'referer': 'https://leetcode.com/Navneet_jain_0154/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-csrftoken': 'gD78nsWDHzXWmhIoYyFi4J8TDATUDLk4WgUkA8ID9CcBDMBJmvN8O2Sq048osIul'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()
