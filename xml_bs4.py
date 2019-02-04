import xmltodict, json, random, requests

"""
Github link: https://github.com/LordOfPolls/Rule34-API-Wrapper/blob/master/Rule34-API-Wrapper/rule34.py
"""
#base_url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index"
def build_url(tags=None,pid=None,ID=None,cid=None):
    """
    Args
    limit: How many posts you want to retrieve. There is a hard limit of 100 posts per request.\n
    pid The page number.
    tags: The tags to search for. Any tag combination that works on the web site will work here. This includes all the meta-tags.\n
    cid: Change ID of the post. This is in Unix time so there are likely others with the same value if updated at the same time.\n
    id: The post id.
    """
    base_url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100"
    if pid != None:
        base_url += "&pid={}".format(pid)
    if tags != None:
        tags = str(tags).replace(" ","+")
        if str(tags) == "":
            print("You cant do that as it will try to return every image possible")
        base_url += "&tags={}".format(tags)
    if cid != None:
        base_url += "&cid={}".format(cid)
    if ID != None:
        base_url += "&id={}".format(ID)
    if pid != None or ID != None or tags != None:
        return base_url
    else:
        return None
    
# data is now base_url
def get_xml_data(modified_url):
    r = requests.get(modified_url)
    if r.status_code == 200:
        return r.content
    else:
        print("OOPSIE WOOPSIE!! \nUwu We made a fucky wucky!! \nA wittle fucko boingo! \nThe code monkeys at our headquarters are working VEWY HAWD to fix this!")


xml = get_xml_data(build_url("akeno_himejima"))
def parse_xml(xml):
    parsed = xmltodict.parse(xml)
    json_data = json.dumps(parsed,indent=2)
    return json_data
def get_img_urls(json_data):
    json_str = json.loads(json_data)
    posts = json_str["posts"]
    post = posts["post"]
    #print(posts) #this is a dict
    #print(posts["post"]) #this is a lis
    urls = [url["@file_url"] for url in post]
    random.shuffle(urls)
    print(urls)
    return urls

def parse_urls(limit, urls):
    if limit > len(urls):
            limit = len(urls)
    list_of_urls = [urls[url] for url in range(limit)]
    return list_of_urls
#print(parse_xml(xml))
#print(get_img_urls(parse_xml(xml)))
#print(parse_urls(10,urls=get_img_urls(parse_xml(get_xml_data(build_url("alexis_texas"))))))
