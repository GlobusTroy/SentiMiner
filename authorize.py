import tweepy

auth = tweepy.OAuthHandler('WuOEiRzGJzlHt1H2imTCPUpfR','X47THIKVxHqGxdHv8AkrcwyU3bH1NW91gIBang8mamhGim7n2Z')

print '>>Attempting to Authorize<<'

try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print 'Error!  Unable to get request token'

print 'Go to the URL below to authorize this application.'
print '---'
print redirect_url
print '---'

verifier = raw_input('Enter the verifier key from the webpage:')

try:
	auth.get_access_token(verifier)
except tweepy.TweepError:
	print 'Error! Unable to retrieve access token'

print 'Save or store the values below to use the access tokens'
print '---'
print 'access_token: '+auth.access_token
print 'access_token_secret: '+auth.access_token_secret
print '---'

print '>>Authorization complete<<'


