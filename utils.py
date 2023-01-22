import requests
import json
import sqlite3
import pandas as pd




def check_new_submission():
    get_user_data





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
    'cookie': 'csrftoken=2JpuNBL3KcoJVAxExt4qDltUe3ORWPj2CSZQ18h06dCHa8bvY3sfyz46VJvA6H7U; _dd_s=rum=1&id=5deee191-4cbb-4cfa-8edf-0b864696cc97&created=1674375268554&expire=1674376168555',
    'dnt': '1',
    'origin': 'https://leetcode.com',
    'pragma': 'no-cache',
    'random-uuid': 'f0de8fd2-efb1-03b1-d602-a3e68a875ba4',
    'referer': 'https://leetcode.com/madhavj211/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-csrftoken': '2JpuNBL3KcoJVAxExt4qDltUe3ORWPj2CSZQ18h06dCHa8bvY3sfyz46VJvA6H7U'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
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