#import library and fuction from another files
import requests
from constants import *
from get_user_id import get_user_id
def get_post_id(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'user does not exist'
        exit()

    #user endpoint for getting users poat id
    request_url=BASE_URL+'users/%s/media/recent/?access_token=%s' %(user_id,APP_ACCESS_TOKEN)
    print 'Get request url %s' %request_url
    user_media=requests.get(request_url).json()

    #check if server give response to our request or not
    if user_media['meta']['code']==200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'there is no recent post of user'
            exit()

    else:
        print "code other than 200 recieved"
        exit()

