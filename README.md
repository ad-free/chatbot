# Chatbot Guide

![Lines of code](https://img.shields.io/tokei/lines/github/ad-free/chatbot) ![GitHub repo size](https://img.shields.io/github/repo-size/ad-free/chatbot) ![GitHub pull requests](https://img.shields.io/github/issues-pr/ad-free/chatbot) ![GitHub](https://img.shields.io/github/license/ad-free/chatbot)

## Setup

1. Install `pyenv`. Following [here](https://github.com/pyenv/pyenv-installer)
2. Clone `chatbot` source from github:
    ```bash
    free@root:~$ git clone https://github.com/ad-free/chatbot.git
    ```
3. Create and Active python enviroment with `pyenv`:
    ```bash
    free@root:~$ pyenv virtualenv 3.8.6 chatbot
    free@root:~$ pyenv activate chatbot
    ```
4. Install **packages** with `pip`:
    ```bash
    (chatbot) free@root:~$ pip install -r requirements.txt
    ```

## How to run

```bash
(chatbot) free@root:~$ python main.py
```

## Notes

> Please use **Linux** for running the source code. Some plugins doesn't work in Windows environment.

## License
----

MIT

**Free Software, Hell Yeah!**
