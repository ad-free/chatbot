import json

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class ChatBotMaster:
    def __init__(self, data: list = None):
        if data is None:
            self.download_data()

        self.data = self.load_data()
        self.title = []
        self.chatbot = ChatBot("Bot Master")
        self.trainner = ListTrainer(self.chatbot)

    @staticmethod
    def load_data() -> list:
        with open("datasets/data.json", "r") as file:
            data = json.loads(file.read())
        return data["data"]

    def download_data(self, url: str = None) -> None:
        pass

    def processing_data(self) -> bool:
        for data in self.data:
            self.title.append(data["title"])

        return True

    def training_bot(self, title: str = None) -> None:
        if not title or title not in self.title:
            return False
        result = []

        for t in self.data:
            if title == t["title"]:
                for qas in t["qas"]:
                    result.append(qas["question"])
                    result.append(qas["answers"])
        self.trainner.train(result)

    def response(self, question: str = None) -> str:
        if not question:
            question = "Hi, can I help you?"
        return f"[Master Bot] {self.chatbot.get_response(question)}"
