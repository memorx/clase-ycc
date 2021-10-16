import tweepy

# API Key
ak = 'VEZPFDB7wqbweHSIKMavx12Kb'
# API Key Secret
aks = 'fkkcKqEw2usdYrUTH21TTsu9aqwYDDWwsrX43rg3eQkrusIIqU'
# Access Token
at = '36797317-Mi2Sqa0H8uabAcjagk5G5NFMcGgWEyy45RqPBwXD9'
# Access Token Secret
ats = 'Uhko1hfFIcFWuFKUIQ3udjipnZLClkyrlDvmxfiff4PDP'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(ak, aks)
        auth.set_access_token(at, ats)
        return auth
    except Exception as e:
        return none

oauth = OAuth()
apicall = tweepy.API(oauth)

api.update_status('run it')
print('Tweet created')


