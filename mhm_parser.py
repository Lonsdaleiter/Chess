class MHMParser:

    @staticmethod
    def get_data(filename):
        file = open(filename)
        return file.read()

    @classmethod
    def get_item(cls, filename, identification):
        data = cls.get_data(filename)
        rt = None

        for part in data.split("/"):
            if part.split(":")[0] == identification:
                rt = part.split(":")[1]
                break

        return rt

    @classmethod
    def get_items(cls, filename, ids):
        data = cls.get_data(filename)
        rt = []

        for part in data.split("/"):
            if part.split(":")[0] in ids:
                rt.append(part.split(":")[1])

        return rt
