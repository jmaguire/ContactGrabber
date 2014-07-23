import MyTools as tools

infile = 'urls_improved'
outfile = 'urls_no_wiki_google'

blacklist = ['google','wiki','city-data','mapquest','infoplease']

data = tools.getJSONData(infile)
new_data = dict(data)


def inBlackList(url):
    for item in blacklist:
        if item in url:
            return True
    return False


for key in data:
    url = data[key]['url']
    if inBlackList(url):
        print 'removing', data[key]['city'], data[key]['url'] 
        del new_data[key]
tools.saveJSONData(new_data,outfile)
