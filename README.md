# DEPIN-BOT FOR DePIN Alliance Telegram Miniapp

This script is under development, there may still be many bugs or glitches that are definitely not comfortable, but I tried to make the full feature features as in the original Depin Alliance bot telegram.

[TELEGRAM CHANNEL](https://t.me/Deeplchain) | [TWITTER](https://x.com/itsjaw_real)

## REGISTER FIRST : [DEPIN ALIANCE](https://t.me/DePIN_Alliance_Bot?start=P8YJYaETWS)

# Feature 24/09/2024

  - Manage the items with the ability to sell items `NEW`
  - Show Device 1 Equipment : bool True/False `NEW`
  - Add Random User Agent `NEW`
  - Support for multiple proxy servers
  - Support for multiple telegram accounts
  - Completion of tasks that are of course without real verification
  - Upgrade randomly selected skills
  - Open a cyber box that can be set to the maximum price
  - Purchase items in the shop that can be set to the maximum price.
  - Automatically use items that have higher Reward Points
  - Manage the items in the account's BAG(ITEM)
  - Can run 24/7 using vps / rdp or something like that


## Requirements

- Python 3.8+

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/jawikas/depin-bot.git
    ```

2. **Navigate to the project directory**

    ```bash
    cd depin-bot
    ```

3. **Create a virtual environment (optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a `config.json` file**

    The `config.json` file should be in the root directory of the project. Here is a sample configuration:

    ```json
    {
    "use_proxy": false,
    "auto_upgrade_skill": false,
    "auto_complete_task": false,
    "show_device_equipment": false,
    "auto_open_box": false,
    "auto_open_box_max_price": 1000,
    "auto_buy_item": false,
    "auto_buy_item_max_price": 10000,
    "auto_sell_item": false,
    "account_delay": 5,
    "countdown_loop": 3800
    }


    ```
    - `use_proxy`: enable or disable the proxy usage
    - `auto_upgrade_skill`: enable or disable the automatic upgrade skill
    - `auto_complete_task`: enable or disable the automatic do tasks
    - `auto_open_box`: enable or disable the automatic open box feature
    - `auto_open_box_max_price`: set a maximum price for the open cyber box
    - `auto_buy_item`: enable or disable the automatic purchase of items feature
    - `auto_buy_item_max_price`: set a maximum price for the item to be purchased
    - `account_delay`: Delay between processing each account (in seconds).
    - `countdown_loop`: how long is the waiting time to return to the first account

2. **Create a `proxies.txt` file**

    The `proxies.txt` file should be in the root directory and contain a list of proxies in the format `username:password@host:port`.

    Example:

    ```
    user1:pass1@ip1:port1
    user2:pass2@ip2:port2
    ```

3. **Create a `data.txt` file**

    The `data.txt` file should be in the root directory and contain one account per line.

    Example:

    ```
    query1
    query2
    ```

## Usage

To run the bot, execute the following command:

```bash
python main.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact [ https://t.me/DeeplChainSup ]
