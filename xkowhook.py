import requests
import colorama
import time
import os

def terminate_program():
    time.sleep(1)
    exit()

def validate_webhook(hook_url):
    response = requests.get(hook_url).text
    return "\"message\": \"Unknown Webhook\"" not in response

def execute_spam(webhook_url, alias, delay_time, spam_amount, spam_message, delete_after):
    counter = 0
    while True if spam_amount == "inf" else counter < int(spam_amount):
        try:
            response = requests.post(webhook_url, json={
                "content": str(spam_message),
                "name": str(alias),
                "avatar_url": "https://i.imgur.com/t5Q8PEo.png"
            })
            if response.status_code == 204:
                print(f"{colorama.Fore.GREEN + colorama.Style.BRIGHT} | [+]  Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Fore.RED + colorama.Style.BRIGHT} | [-]  Failed{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay_time))
        counter += 1
    
    if delete_after.lower() == "y":
        requests.delete(webhook_url)
        print(f'{colorama.Fore.GREEN + colorama.Style.BRIGHT}Webhook deleted')
    
    print(f'{colorama.Fore.GREEN + colorama.Style.BRIGHT}Done')

def setup_spam():
    print(f"""{colorama.Fore.GREEN + colorama.Style.BRIGHT}\n
 |          _                 _                 _    
 |    __  _| | _______      _| |__   ___   ___ | | __
 |    \ \/ / |/ / _ \ \ /\ / / '_ \ / _ \ / _ \| |/ /
 |     >  <|   < (_) \ V  V /| | | | (_) | (_) |   < 
 |    /_/\_\_|\_\___/ \_/\_/ |_| |_|\___/ \___/|_|\_\
 |
 |
 |{colorama.Fore.WHITE + colorama.Style.BRIGHT}
     """)
    webhook_url = input(" |      Enter webhook: ")
    alias = input(" |      Enter webhook name: ")
    spam_message = input(" |      Enter spam message: ")
    delay_time = input(" |      Enter delay time: ")
    spam_amount = input(" |      Amount of messages: ")
    delete_after = input(" |      Delete webhook afterwards? [Y/N] > ")
    
    try:
        delay_time = float(delay_time)
    except ValueError:
        terminate_program()
    
    if not validate_webhook(webhook_url) or (not spam_amount.isdigit() and spam_amount != "inf") or (delete_after.lower() != "y" and delete_after.lower() != "n"):
        terminate_program()
    else:
        execute_spam(webhook_url, alias, delay_time, spam_amount, spam_message, delete_after)
        terminate_program()

if __name__ == '__main__':
    os.system('cls')
    os.system("title xkowhook - xkow.xyz")
    colorama.init()
    setup_spam()
