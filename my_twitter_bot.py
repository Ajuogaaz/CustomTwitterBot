import tweepy

print("This is my twitter bot")

CONSUMER_KEY = '6qOlQgVqAIGF2QCPGi25f1FLa'
CONSUMER_SECRET ='QGlEJnB4ULitV1lSKT2oSAkad9seBtr49G0cYHf5Aq5pexdsl4'
ACCESS_KEY = '923578658509516801-sdJrjp0ChM6frDANbZILlm0mcKcQPi2'
ACCESS_SECRET = 'XgQMpXy293CakkitoT32vl7iLXdAyFJdXvwJY5PDOhS4E'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode= 'extended')

for mention in reversed(mentions):
    print(str(mention.id) + " " + mention.text)
    if '#kenya' in mention.text.lower():
        print("found #kenya")
        print("Responding back...")
