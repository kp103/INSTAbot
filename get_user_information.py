#import library and python file for supporting fuction
from __future__ import print_function
from get_user_id import *
from constants import *
import time

#def function for user information
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print ('User does not exist!')
    exit()

  request_url = BASE_URL + 'users/%s?access_token=%s' %(user_id, APP_ACCESS_TOKEN) #url of user along with  usr id and your access token
  print ('GET request url : %s' % (request_url))
  user_info = requests.get(request_url).json()#fetch data from content of url query


  #check what is the result of query
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):

          #fetch from json format and store in variable
          user='Username: %s' % (user_info['data']['username'])
          id= 'ID: %s' % (user_info['data']['id'])
          follower= 'No.of followers: %s' % (user_info['data']['counts']['followed_by'])
          following='No. of people you are following: %s' % (user_info['data']['counts']['follows'])
          no_of_post='No. of posts: %s' % (user_info['data']['counts']['media'])

          #user information store in list
          info_list=[user,id,follower,following,no_of_post]
          for x in range(len(info_list)):
              print(info_list[x],end="   ")
              time.sleep(.700)#wait .700 microsecond then loop again

      else:
          print ('There is no data for this user!')
  else:
      print ('Status code other than 200 received!')