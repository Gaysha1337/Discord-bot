import requests, random
from bs4 import BeautifulSoup

"""
TODO:
- Get full url with user's search images
Later: 
- Multiple tags
- How many images(look for a fix incase user asks for too many images)
- Page Number
"""

def build_url(query):
    full_url = "https://rule34.paheal.net/post/list/{}/1".format(query)
    #print(full_url)
    return full_url
def request_url(full_url):
    r = requests.get(full_url)
    html = r.content
    return html
def create_soup(html):
    soup = BeautifulSoup(html,"html.parser")
    print(soup)
    return soup

soup = BeautifulSoup(request_url(build_url("Akeno_Himejima")),"html.parser") # del after; this if for testing
def get_image_urls(): # Make soup the arg later
    img_links = []
    all_query_images = soup.findAll("a",{"class":"shm-thumb-link"})
    for a in all_query_images:
        if a.img:
            img_links.append(a.img["src"])
    #print(img_links)
    return img_links
    
def display_imgs(link_list = get_image_urls(), img_num_to_show=10):
    user_img_amount = random.sample(link_list,img_num_to_show)
    for img in user_img_amount:
        print(img)
    #print(user_img_amount)
        
        
#build_url("Yuno_Gasai")
#create_soup(request_url(build_url("Yuno_Gasai")))
#get_image_urls()
display_imgs()