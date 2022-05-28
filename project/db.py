import redis
from task import Task

rd = redis.StrictRedis(host='redis', port=6379, db=0)


def getDocument(id: str) -> str :
    return rd.get(id)

def saveDocument(id: str, document: Task) :
    rd.set(id,document)
