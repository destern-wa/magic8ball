import socket


def get_response(question: str) -> str:
    """Connects to the magic 8-ball server, sends a question, and receives a response

    :param question: Question to ask
    :return: Response received
    """
    try:
        # Create client socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', 8888))
        sock.send(question.encode())
        from_server = sock.recv(4096)
        sock.close()
        return from_server.decode()
    except ConnectionError:
        return "*** Error connecting to server ***"


def main():
    print("Welcome to the magic 8-ball")
    print("+++++++++++++++++++++++++++")
    while True:
        question = input("\nAsk your question\n> ")
        print("  ... the magic 8-ball says ... ", end="")
        print(get_response(question))
        if input("Ask another question [y/n]? ").lower() != 'y':
            print("\n### Goodbye ###")
            break


if __name__ == '__main__':
    main()
