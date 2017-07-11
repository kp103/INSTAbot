from constants import *
import requests
from get_user_id import get_user_id
import urllib

def get_user_post(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print "user not exist"
        exit()
    url=BASE_URL+'users/%s/media/recent/?access_token=%s' %(user_id,APP_ACCESS_TOKEN)
    print "GET requested url :%s" %url
    req_media=requests.get(url).json()

    if req_media['meta']['code']==200:
        if len(req_media['data']):
            media_name=req_media['data'][0]['id']+'.jpeg'
            media_url=req_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(media_url,media_name)
            print "image downloaded"
        else:
            print"data not found"
    else:
        print "code other than 200"
