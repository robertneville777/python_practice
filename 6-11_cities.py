cities = {'ridgecrest':{'country':'U.S.','population':25000,
    'fact':'Too damn hot there in the summer.'},
    'springfield':{'country':'U.S.','population':'30000',
    'fact':'Rains there in the summer.'},
    'san diego':{'country':'U.S.','populatin':1500000,
    'fact':'Overall temperate year around.'}
    }

for outer_key,outer_val in cities.items():
    print(outer_key.title() + " info: ")
    for inner_key, inner_val in outer_val.items():
        print("\t" + inner_key.title() + ": " + str(inner_val))
    print()
