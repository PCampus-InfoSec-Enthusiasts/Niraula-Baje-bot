import requests, random

def get_joke():      

    def request_joke():
        url1 = 'https://official-joke-api.appspot.com/random_joke'
        url2 = 'https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=single'
        url3 = 'https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart'

        url_list = [url1, url2, url3]

        #choose one of the urls randomly from the above list
        joke_choice = random.choice(url_list)

        request = requests.get(joke_choice)

        #check status code, i.e. whether the website returns 200 or error
        if request.status_code == 200:
            joke = request.json()       #requests json from the website

            if joke_choice == url1:
                return joke['setup'] + '\n' + joke['punchline']
            
            elif joke_choice == url2:
                return joke['joke']     #for one-liner/one-part joke

            elif joke_choice == url3:
                return joke['setup'] + '\n' + joke['delivery']      #for two-liner/two-part joke

        return "Uh-oh...couldn't get a joke. Try again later. :("

    reply = request_joke()

    return reply







'''
#below part is for programming jokes::
************************************
global URL
    joke_choice = ['official-joke-api', 'joke-api']

    choice = random.choice(joke_choice)

    if choice == 'official-joke-api':
        request = requests.get(URL+'programming/random')
        data = check_valid_status_code(request)
        
    else:
        URL_joke_api = 'https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist'
        request = requests.get(URL_joke_api)
        data = check_valid_status_code(request)

    return data

'''
