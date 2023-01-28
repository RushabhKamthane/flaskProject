import paralleldots
paralleldots.set_api_key('sXr2iZqRBldNxeG9e78vq77TeR2AO3Cw2E3hN6kkcUM')
def ner(text):

    ner = paralleldots.similarity(text)
    return ner

def ser(text):

    sentiment = paralleldots.sentiment(text)
    return sentiment

def abuse(text):
    abuse = paralleldots.abuse(text)
    return abuse
