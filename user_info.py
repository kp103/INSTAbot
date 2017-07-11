#import all nessassry libararid
import requests
from constants import *
import urllib
#function for fetch own info of instagram account
def self_info():
    request_url=BASE_URL +'users/self/?access_token=%s' %(APP_ACCESS_TOKEN)
    print 'GET request url :%s' %(request_url)
    user_info=requests.get(request_url).json()

    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print "Username: %s" %user_info['data']['username']
            print "User_id: %s" % user_info['data']['id']
            print "No of follower: %s" % (user_info['data']['counts']['followed_by'])
            print "no of post :%s" %(user_info['data']['counts']['media'])

            image_url=user_info['data']['profile_picture']
            image_name=user_info['data']['id']+'.jpeg'
            urllib.urlretrieve(image_url,image_name)
            print "image downloaded"
        else:
            print "user does not exist"
    else:
        print "Not able to access user instagram info"
