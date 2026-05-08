class Router():
    def __init__(self):
        self.path = {}
        self.handler = ""

    def register(self,path: str, handler: str):
        self.path = path
        self.handler = handler

    def dispatch(self, path, **kwargs):
        pass

    

