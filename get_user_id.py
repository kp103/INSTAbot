import  requests
from constants import BASE_URL ,APP_ACCESS_TOKEN

def get_user_id(insta_username):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' %(request_url)
  user_info=requests.get(request_url).json()
  if user_info['meta']['code'] ==200:
      if len(user_info['data']):
          return user_info['data'][0]['id']
      else:
          print "user not exist"
  else:
      print "unable to acces the info"
      exit()
