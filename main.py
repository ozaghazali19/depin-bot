import random
import requests
from colorama import *
from src.deeplchain import log, log_line, countdown_timer, read_config, _banner, mrh, pth, kng, hju, bru, htm, reset, _clear
from src.core import Depin, load_proxies

config = read_config()
init(autoreset=True)

def main():
    upgrade_skill = config.get('auto_upgrade_skill', False)
    auto_task = config.get('auto_complete_task', False)
    auto_open_box = config.get('auto_open_box', False)
    max_price = config.get('auto_open_box_max_price', 0)
    auto_buy_item = config.get('auto_buy_item', False)
    max_item_price = config.get('auto_buy_item_max_price', 0)
    auto_sell_item = config.get('auto_sell_item', False)
    delay = config.get('account_delay', 5)
    loop = config.get('countdown_loop', 3800)
    use_proxy = config.get('use_proxy', False) 
    proxies = load_proxies() if use_proxy else None

    try:
        with open("data.txt") as file:
            query_data_list = file.readlines()
        query_data_list = [data.strip() for data in query_data_list if data.strip()]
        if not query_data_list:
            raise ValueError("data.txt is empty or contains only empty lines.")
    except FileNotFoundError:
        log(mrh + f"data.txt file not found.")
        return

    for i, query_data in enumerate(query_data_list, start=1):
        proxy = random.choice(proxies) if proxies and use_proxy else None
        dep = Depin(proxy=proxy)

        log(hju + f"Processing account {pth}{i}/{len(query_data_list)}") 
        if proxy:
            proxy_url = proxy 
            if '@' in proxy_url:
                host_port = proxy_url.split('@')[-1]
            else:
                host_port = proxy_url.split('//')[-1]
            
            log(hju + f"Using proxy: {pth}{host_port}")
            log(htm + "~" * 38)

        user_data = dep.extract_user_data(query_data)
        user_id = user_data.get("id")
        if not user_id:
            log(mrh + f"User ID not found in data.")
            continue

        token = dep.local_token(user_id) or dep.login(query_data, user_id)
        if not token:
            log(mrh + f"Login failed for user ID: {pth}{user_id}")
            continue

        while True:
            try:
                dep.user_data(user_id)
                dep.j_l(user_id)
                dep.daily_checkin(user_id)
                dep.claim_mining(user_id)

                device_indices = dep.get_device_indices(user_id)
                if not device_indices:
                    log(htm + f"No valid device indices found for user ID: {pth}{user_id}")
                    break
                device_index = device_indices[0]

                if auto_open_box:
                    dep.open_box(user_id, max_price)
                else:
                    log(kng + f"Auto open cyber box is disabled!")
                if auto_buy_item:
                    dep.auto_buy_item(user_id, device_index, max_item_price)
                else:
                    log(kng + f"Auto buy item is disabled!")
                for item_type in ["CPU", "GPU", "RAM", "STORAGE"]:
                    dep.get_items_by_type(user_id, item_type)
                if auto_task:
                    dep.get_task(user_id)
                    dep.complete_quest(user_id)
                else:
                    log(kng + f"Auto complete task is disabled!")
                if upgrade_skill:
                    dep.upgrade_skill(user_id)
                else:
                    log(kng + f"Auto upgrade skill is disabled!")
                if auto_sell_item:
                    dep.sell_user_items(user_id)
                else:
                    log(kng + f"Auto sell item is disable!")
                break 

            except requests.exceptions.ProxyError as e:
                log(mrh + f"Proxy error occurred: {e}")
                if "407" in str(e): 
                    log(bru + f"Proxy authentication failed. Trying another")
                    if proxies:
                        proxy = random.choice(proxies)
                        proxies 
                        log(bru + f"Switching to new proxy: {pth}{proxy}")
                    else:
                        log(mrh + f"No more proxies available.")
                        break
                else:
                    log(htm + f"An error occurred: {htm}{e}")
                    break

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    log(bru + f"Token expired or Unauth. Attempting to login")
                    token = dep.login(query_data, user_id)
                    if token:
                        log(hju + f"Re-login successful Continuing action")
                    else:
                        log(mrh + f"Re-login failed  Skipping")
                        break
                else:
                    log(htm + f"HTTP error occurred: {htm}{e}")
                    break

        log_line()
        countdown_timer(delay)
    countdown_timer(loop)

if __name__ == "__main__":
    _clear()
    _banner()
    while True:
        try:
            main()
        except KeyboardInterrupt:
            log(mrh + f"Process interrupted by user.")
            exit(0)

