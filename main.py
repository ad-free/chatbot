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
        return data["data"]

    def download_data(self, url: str = None) -> None:
        pass

    def processing_data(self) -> bool:
        for data in self.data:
            self.title.append(data["title"])

        return True

    def training_bot(self, title: str = None):
        if not title:
            return False
        result = []

        if title in self.title:
            for t in self.data:
                if title == t["title"]:
                    for paragraph in t["paragraphs"]:
                        for qas in paragraph["qas"]:
                            answer = qas["answers"][0]
                            result.append(qas["question"])
                            result.append(answer["text"])
        self.trainner.train(result)

    def response(self, question: str = None):
        if not question:
            question = "Hi, can I help you?"
        return f"[Master Bot] {self.chatbot.get_response(question)}"


if __name__ == "__main__":
    chatbot = ChatBotMaster()
    chatbot.processing_data()

    for i in range(len(chatbot.title)):
        print(f"{i}. {chatbot.title[i]}")

    title = input("[Master Bot] What is your title? --> ")
    chatbot.training_bot(title)
    while True:
        question = input("[Master Bot] What is your question? --> ")
        if question == "exit":
            break
        print(chatbot.response(question=question))
