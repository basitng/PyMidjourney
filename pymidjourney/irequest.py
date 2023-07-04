import json
import requests
import io
from typing import Dict, Union


class APIRequest:
    API_URL = 'https://api.midjourneyapi.io/v2/'

    def __init__(self, api_key: str, callback_uri: str = None):
        self.api_key = api_key
        self.callback_uri = callback_uri

    @staticmethod
    def send_request(endpoint: str, data: dict, headers: dict, files: dict = None) -> Union[Dict, str]:
        url = APIRequest.API_URL + endpoint
        if files is not None:
            response = requests.post(
                url, data=data, files=files, headers=headers)
        else:
            response = requests.post(url, data=data, headers=headers)
            print(response)
        if response.status_code == 200:
            return response.json()
        else:
            print(response)
            return response.text

    def describe_image(self, image_file_path: str) -> Dict:
        endpoint = 'describe'
        files = [('image', image_file_path)]

        data = {}
        if self.callback_uri != "":
            data['callbackURL'] = self.callback_uri

        headers = {'Authorization': self.api_key}
        return APIRequest.send_request(endpoint, data, headers, files)

    def get_result(self, task_id: str) -> Dict:
        endpoint = 'result'
        data = json.dumps({'taskId': task_id})
        headers = {'Authorization': self.api_key,
                   'Content-Type': 'application/json'}
        return APIRequest.send_request(endpoint, data, headers)

    def upscale_image(self, task_id: str, position: int) -> Dict:
        endpoint = 'upscale'
        data = {'taskId': task_id, 'position': position}
        headers = {'Authorization': self.api_key,
                   'Content-Type': 'application/json'}
        return APIRequest.send_request(endpoint, data, headers)

    def imagine(self, prompt: str) -> Dict:
        endpoint = 'imagine'
        data = {'prompt': prompt}
        if self.callback_uri != "":
            data['callbackURL'] = self.callback_uri

        headers = {'Authorization': self.api_key}
        return APIRequest.send_request(endpoint, data, headers)

    def variants(self, messageId: str, jobId: str, position: str) -> Dict:
        endpoint = 'variants'
        data = {
            'messageId': messageId, 'jobId': jobId, 'position': position}

        if self.callback_uri != "":
            data['callbackURL'] = self.callback_uri

        headers = {'Authorization': self.api_key}
        return APIRequest.send_request(endpoint, data, headers)

    def seed(self, messageId: str, jobId: str) -> Dict:
        endpoint = 'seed'
        data = {
            'messageId': messageId, 'jobId': jobId}

        if self.callback_uri != "":
            data['callbackURL'] = self.callback_uri

        headers = {'Authorization': self.api_key}
        return APIRequest.send_request(endpoint, data, headers)
