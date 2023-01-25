import tweepy
api_key = "API 키"
api_secret = "API 비밀키"
access_token = "액세스 토큰"
access_token_secret = "액세스 토큰 암호"
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword = '치맥'
search = []
cnt = 1
while(cnt <= 10) :
    tweets = api.search(q=keyword, count = 100)
    for tweet in tweets :
        search.append(tweet)
    cnt += 1
    
data = {}
i = 1
print('['+keyword+'에 대한 트윗 글]')
for tweet in search :
    data['text'] = tweet.text
    print(i, ":", data)
    i += 1