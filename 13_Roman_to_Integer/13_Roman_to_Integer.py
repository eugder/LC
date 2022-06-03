class Roman2Int:
    def convert(self, roman: str) -> int:
        for i in reversed(roman):
            print (i)

convertor = Roman2Int()
convertor.convert("abc")