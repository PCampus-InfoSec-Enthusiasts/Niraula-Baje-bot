import requests, json

def covid19_data_country(country):
    url = 'https://covid19.mathdro.id/api/countries/' #country-specific result
    
    try:
        data = requests.get(url+country).json()

        confirmed = data['confirmed']['value']
        recovered = data['recovered']['value']
        deaths = data['deaths']['value']

        return f"__COVID-19: Latest data for **{country}**__: \n\nConfirmed: {confirmed} \nRecovered: {recovered} \nDeaths: {deaths}"

    except:
        return "Looks like something is not right. Please check and try again."


def covid19_data_global():
    url = 'https://covid19.mathdro.id/api/countries/'

    try:
        data = requests.get(url).json()

        confirmed = data['confirmed']['value']
        recovered = data['recovered']['value']
        deaths = data['deaths']['value']

        return f"__COVID-19: Latest **gobal** data__: \n\nConfirmed: {confirmed} \nRecovered: {recovered} \nDeaths: {deaths}"

    except:
        return "Looks like something is not right. Please check and try again."











'''for data from MoHP Nepal:

    if place == 'global' or place == 'world':

        positive = data.get('nepal').get('positive')
        deaths = data.get('nepal').get('deaths')
        recovered = data.get('nepal').get('extra1')
    
        today_death = data.get('nepal').get('today_death')
        today_newcase = data.get('nepal').get('today_newcase')
        today_recovered = data.get('nepal').get('today_recovered')

        updated_on = data.get('nepal').get('updated_at')

        response = f"__All time data__: \nConfirmed: {positive} \nDeaths: {deaths} \nRecovered: {recovered} \n\n__Today's data:__ \nConfirmed: {today_newcase} \nDeaths: {today_death} \nRecovered: {today_recovered} \n\nLast updated on: {updated_on} +5:45 NPT \nSource: Corona Info - Ministry of Health and Population(https://covid19.mohp.gov.np/)"
        
        pass


    if place == 'nepal':
        positive = data.get('nepal').get('positive')
        deaths = data.get('nepal').get('deaths')
        recovered = data.get('nepal').get('extra1')
    
        today_death = data.get('nepal').get('today_death')
        today_newcase = data.get('nepal').get('today_newcase')
        today_recovered = data.get('nepal').get('today_recovered')

        updated_on = data.get('nepal').get('updated_at')

        response = f"__All time data__: \nPositive: {positive} \nDeaths: {deaths} \nRecovered: {recovered} \n\n__Today's data:__ \nPositive: {today_newcase} \nDeaths: {today_death} \nRecovered: {today_recovered} \n\nLast updated on: {updated_on} \nSource: Corona Info - Ministry of Health and Population(https://covid19.mohp.gov.np/)"
    
    return response
'''
    
