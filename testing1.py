import requests
import gifparse
import pprint
import jsonpickle
import json

site="https://s3.us-east-2.amazonaws.com/oooverflow-challs/f1b69d1d5c8e874ffae9ce29d39435eda78ce7ae44428c88ff29cb368f8fead6/redacted-puzzle.gif"
gif_bytes=requests.get(site).content
gif = gifparse.parse(gif_bytes)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(gif.__dict__)
print(type(gif))
print(dir(gif))

print("HEADER")
print(type(gif.header))
print(dir(gif.header))
test="__dict__"
#print(gif.header[str(test)])

serial = jsonpickle.encode(gif)
print(json.dumps(json.loads(serial), indent=2))


"""def getitems(obj):

  def getkeys(obj, stack):
    for k, v in obj.items():
      k2 = ([k] if k else []) + stack # don't return empty keys
      if v and isinstance(v, dict):
        for c in getkeys(v, k2):
          yield c
      else: # leaf
        yield k2

  def getvalues(obj):
    for v in obj.values():
      if not v: continue
      if isinstance(v, dict):
        for c in getvalues(v):
          yield c
      else: # leaf
        yield v if isinstance(v, list) else [v]

  return list(getkeys(obj,[])), list(getvalues(obj))

pp.pprint(getitems(gif))
"""
