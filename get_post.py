from constants import *
import requests
def get_posts():
    url=BASE_URL+'users/self/media/recent/?access_token=%s' %(APP_ACCESS_TOKEN)
    print "GET request url %s " % url
    request=requests.get(url).json()

    if request['meta']['code']==200:
        if len(request['data']):
            return request['data'][0]['id']

        else:
            print "data not recieved"

    else:
        print "user does not exist"

