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
        with open("datasets/dev-v1.1.json", "r") as file:
            data = json.loads(file.read())
        return data.get("data", {})

    def download_data(self, url: str = None) -> None:
        pass

    def processing_data(self) -> bool:
        for data in self.data:
            self.title.append(data["title"])

        return True

    def training_bot(self, title: str = None):
        if not title:
            return False

        if title in self.title:
            for t in self.data:
                if t == t["title"]:
                    paragraphs = t["paragraphs"]
                    question = []
                    answer = []
                    for c in paragraphs["qas"]:
                        question.append(c["question"])
                        answer.append(c["answers"])
                    result = question + answer
                    self.trainner.train(result)

    def response(self, question: str = None):
        if not question:
            question = "Hi, can I help you?"
        return self.chatbot.get_response(question)


if __name__ == "__main__":
    chatbot = ChatBotMaster()
    chatbot.processing_data()
    title = input("What is your title?\n")
    question = input("What is your question?\n")
    chatbot.training_bot(title)
    print(chatbot.response(question=question))
