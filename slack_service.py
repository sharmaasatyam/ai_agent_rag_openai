from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackService:
    def __init__(self, slack_token):
        self.client = WebClient(token=slack_token)

    def post_message(self, channel, message):
        try:
            response = self.client.chat_postMessage(channel=channel, text=message)
        except SlackApiError as e:
            print(f"Error posting message: {e.response['error']}")
