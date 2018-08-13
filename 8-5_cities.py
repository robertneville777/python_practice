def describe_city(city,country='america'):
    """Print relationship between city and country"""
    print(city.title() + ' is in ' + country.title() + '.')

describe_city('new york')
describe_city('los angeles')
describe_city('florence','italy')
