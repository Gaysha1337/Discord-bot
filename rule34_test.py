import requests, random
from bs4 import BeautifulSoup

"""
TODO:
- Get full url with user's search images
Later: 
- Multiple tags (tag**, iterate through them and append to url with + after each tag)
- How many images(look for a fix incase user asks for too many images)
- Page Number
"""
x = build_url(1)
def build_url(tags):
    if str(tags)!=None:
        tags = tags.replace(" ", "+")
        if str(tags) == "":
            return
       # += "&tags={}".format(tags)
    full_url = "https://rule34.xxx/index.php?page=post&s=list&tags={}+".format(tags)
    return full_url
def request_url(full_url):
    r = requests.get(full_url)
    html = r.content
    return html
def create_soup(html):
    soup = BeautifulSoup(html,"html.parser")
    return soup
#soup = BeautifulSoup(request_url(build_url("akeno_himejima")),"html.parser")# del after; this if for testing
def get_image_urls(soup): # Make soup the arg later
    img_links = []
    all_query_images = soup.findAll("img",{"class":"preview"})
    for img in all_query_images:
        src = img["src"]
        #print(src)
        img_links.append(src)
    #print(img_links)
    return img_links


def display_imgs(img_num_to_show,link_list):
    if img_num_to_show > len(link_list):
        print("There aren't enough images, the max imgs will be shown:" ,len(link_list))
        img_num_to_show = len(link_list)
        num_imgs_to_show = random.sample(link_list,img_num_to_show)
        #return " ".join(num_imgs_to_show)
        return num_imgs_to_show
    else:
        #print("There are infact:", img_num_to_show,"images to show")
        num_imgs_to_show = random.sample(link_list,img_num_to_show)
        #return " ".join(num_imgs_to_show)
        return num_imgs_to_show

#print(display_imgs(2000,get_image_urls(create_soup(request_url(build_url("akeno_himejima"))))))
#print(build_url("Furry gay"))