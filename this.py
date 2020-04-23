from IPython.display import display
from PIL import Image, ImageDraw
import urllib.request
import io
import json


data = '{"content": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2F8%2F8b%2FThe_Pretender_FF_New_Single.jpg&f=1&nofb=1","annotation" : [{"label":["Wave"], "points":[[50.32, 50.89]]}]}'
parse_data = json.loads(data)


with urllib.request.urlopen(parse_data["content"]) as url:
    f = io.BytesIO(url.read())

img = Image.open(f)
draw = ImageDraw.Draw(img)
for i in parse_data["annotation"]:
    for j in i["points"]:
        draw.point((j[0], j[1]), 'red')
display(img)
