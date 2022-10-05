import m3u8
import urllib.request as req
from concurrent import futures
test = ""
m3u8_obj = m3u8.load(test)
ts = m3u8_obj.dumps().split(",")
#print(ts)
ts_new = [s.lstrip("\n") for s in ts if "https" in s]
#print(ts_new)
def get_URL(url):
    tmp_url = url.split("/")
    for i in tmp_url:
        if ".ts" in i:
            file_name = i
            pos_1 = file_name.find(".ts")
            break
    pos = url.find("\n")
    try:
        req.urlretrieve(url[:pos],i[:pos_1 +3])
    except Exception as f:
        print(f)
    #tmp = req.urlopen(name[:pos]).read()
    #with open(tmp_name[:pos_2 + 2], "wb") as e:
        #e.write(tmp)
    tmp_list =[]
with futures.ThreadPoolExecutor() as executor:
        executor.map(get_URL, ts_new)