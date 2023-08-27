

class HTML(bytearray):
    def __init__(self):
        super().__init__()

    def __str__(self):
        text = super.__str__(self)
        return text[12:-2]