# Chatbot Guide
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
![Lines of code](https://img.shields.io/tokei/lines/github/ad-free/chatbot) ![GitHub repo size](https://img.shields.io/github/repo-size/ad-free/chatbot) ![GitHub pull requests](https://img.shields.io/github/issues-pr/ad-free/chatbot) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Features

|Versions | Description| Status |
|---------|------------|--------|
| v1      | Simple chat with chatbot | ![Completed](https://img.shields.io/badge/-Done-brightgreen) |
| v2      | Create web application   | ![Pending](https://img.shields.io/badge/-Pending-red) |
| v3      | Build and deploy with **Docker** | ![Pending](https://img.shields.io/badge/-Pending-red) |
| v3      | Build and deploy with **Kubernetes | ![Pending](https://img.shields.io/badge/-Pending-red) |

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
