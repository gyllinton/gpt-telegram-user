# Description
GPT chat running as a Telegram user

# Screenshots
<img src="https://github.com/gyllinton/gpt-telegram-user/blob/gyllinton-gpt-telegram-user/images/screenshot-1.png"  width="400" style="border-radius:10px;">

# Installing (Ubuntu)
1. In CLI run `apt update && apt install git python-is-python3 python3-pip -y`
2. Run `git clone https://github.com/gyllinton/gpt-telegram-user`
3. cd `gpt-telegram-user`
4. Run `pip3 install -r requirements.txt`
5. Open **config.json** file and fill the data:
  ```
  {
          "api_id": "YOUR_TELEGRAM_API_ID_KEY",
          "api_hash": "YOUR_TELEGRAM_API_HASH_KEY",
          "openai": "YOUR_OPENAI_KEY"
  }
  ```
  [Telegram API ID key — Instruction](https://core.telegram.org/api/obtaining_api_id) | [Telegram API Hash Key (ibid)](https://core.telegram.org/api/obtaining_api_id) | [OpenAI Key — Link](https://platform.openai.com/account/api-keys)<br>
6. Edit **initial_messages.json** file to paste your own training data<br>
7. Run `python3 main.py`<br><br>
Enjoy!
