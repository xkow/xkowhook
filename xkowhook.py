import requests, colorama, time, os


def _exit():
    time.sleep(5)
    exit()
    
def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://avatars.githubusercontent.com/u/49077814?s=400&u=3fd0ffb76b0057cbad4c889d7b5b86974888bb4e&v=4"})
            if data.status_code == 204:
                print(f"{colorama.Back.GREEN} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.GREEN}Webhook deleted')
    print(f'{colorama.Fore.GREEN}Done')


def initialize():
    print(f"""{colorama.Fore.GREEN+colorama.Style.BRIGHT}\n
 |          _                 _                 _    
 |    __  _| | _______      _| |__   ___   ___ | | __
 |    \ \/ / |/ / _ \ \ /\ / / '_ \ / _ \ / _ \| |/ /
 |     >  <|   < (_) \ V  V /| | | | (_) | (_) |   < 
 |    /_/\_\_|\_\___/ \_/\_/ |_| |_|\___/ \___/|_|\_\
 |
 |
 |{colorama.Fore.WHITE+colorama.Style.BRIGHT}
     """)
    webhook = input(" |      Enter webhook: ")
    name = input(" |      Enter webhook name: ")
    message = input(" |      Enter message: ")
    delay = input(" |      Enter delay: ")
    amount = input(" |      Amount of messages: ")
    hookDeleter = input(" |      Delete webhook afterwards? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls')
    os.system("title xkowhook - xkow.xyz")
    colorama.init()
    initialize()
