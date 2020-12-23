from v1.chatbot import ChatBotMaster


if __name__ == "__main__":
    is_title = False
    chatbot = ChatBotMaster()
    chatbot.processing_data()

    for i in range(len(chatbot.title)):
        print(f"{i}. {chatbot.title[i]}")

    while True:
        try:
            if not is_title:
                title = input("[Master Bot] What is your title? --> ")
                if title not in chatbot.title:
                    print("[Master Bot] Please choice titles from above!")
                    continue
                is_title = True
                chatbot.training_bot(title)
            else:
                question = input("[Master Bot] What is your question? --> ")
                bot_response = chatbot.response(question=question)

                if bot_response == question:
                    print("[Master Bot] Sorry! I don't have the answer.")
                    continue
                print(bot_response)
        except (KeyboardInterrupt, EOFError, SystemExit):
            is_change = input(
                "\n[Master Bot] Do you want to change the title (y/n)--> "
            )
            if is_change.lower() == "y":
                is_title = False
            else:
                print("[Master Bot] Good bye! See you again.")
                break