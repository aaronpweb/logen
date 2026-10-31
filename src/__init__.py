
params = {
    "page": 2,
    "threshold": 4.5,
    "query": "python"
}

class FetchLog:
    """gettings realtime data from live server logs"""
    def __init__(self, params) -> None:
        pass

class ReadLog(FetchLog):
    def __init__(self) -> None:
        super().__init__(params=params)
        self.data: dict

    """
        Reading from
        1. static Log filen(json formated logs)
        2. live log streaming data (from a url, throught a plugin)

        There are 3 types of logs structures.
            1. Unstructured (Plain Text):
            2. Semi-Structured (CSV):
            3. Structured (JSON):
    """

    def read_live(self, url, params):
        pass
    def read_file(self):
        pass
