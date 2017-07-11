#import library and fuction from another files
import requests
from constants import *
from get_post_id import get_post_id

#def a fuction for comment on a post
def post_comment(insta_username):
    post_id=get_post_id(insta_username)
    comment=raw_input("write the comment:>")
    payload={'access_token':APP_ACCESS_TOKEN,'text':comment}
    request_url=BASE_URL+'media/%s/comments' %post_id
    print "POST request url %s" %request_url

    #send post request to the server and and store the response in a make_commect variable
    make_comment=requests.post(request_url,payload).json()

    #check what is the response from server
    if make_comment['meta']['code']==200:
        print "\n\n\t\t............commect successfull posted "

    else:
        print "commect not posted"


#calling the defined f