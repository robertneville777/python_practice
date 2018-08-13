def build_profile(first,last,**user_info):
    """ Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key,val in user_info.items():
        profile[key] = val
    
    return profile

clint_profile = build_profile('clint','schad',field='engineering',
    level='scrub',place='springfield')

print(clint_profile)
