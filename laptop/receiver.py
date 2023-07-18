import signal
from kaspersmicrobit import KaspersMicrobit
from decoratorOperations import debounce
from slack_sdk import WebClient


last_value = None
# [Slack] Click profile > Three dots > Copy member ID
user = "000000000"
"""
1- Go to https://api.slack.com/apps
2- Create New App > From Scratch
3-In the app settings page > "OAuth & Permissions" > "User Token Scopes"
4- Add scopes "users.profile:read" and "users.profile:write"
5- Copy "User OAuth Token"
6- [Optional] Restrict API Token Usage to your IP address
"""
token = "xoxp-000000000-000000000-000000000-000000000"

client = WebClient(token)


def select_emoji(input: str):
    match input:
        case "1":
            return ":zzz:"
        case "2":
            return ":metal:"
        case "3":
            return None
        case "4":
            return ":brb:"
        case "5":
            return ":thinking_face:"
        case "6":
            return ":coffee:"
        case _:
            return None


@debounce(5)
def on_received_string(input: str):
    global last_value
    print(f"RX: '{input}'")
    emoji = select_emoji(input)
    if emoji is None:
        return print(f"[X] no emoji found for input='{input}'")

    if emoji == last_value:
        return print(f"[X] unchanged value='{input}'")

    last_value = emoji
    print(f"updating status: {emoji}")

    client.users_profile_set(
        user=user,
        profile={
            "status_emoji": emoji
        }
    )


with KaspersMicrobit.find_one_microbit() as microbit:
    microbit.uart.receive_string(on_received_string)
    signal.pause()
