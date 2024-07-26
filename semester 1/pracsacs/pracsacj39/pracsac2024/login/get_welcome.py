class GetWelcome:
    def __init__(self):
        pass
    def get_text(self):
        with open("pracsac2024/login/welcome.txt", mode="r") as f:
            reader = f.read()
        return reader