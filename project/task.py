import json
class Task:
    def __init__(self,name: str,type: int):
        self.name = name
        self.type = type
    def toJson(self):
            return json.dumps(self,default= lambda o: o.__dict__, sort_keys=True, indent=4)