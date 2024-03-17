import os
from dotenv import load_dotenv

# for testing enable the line below
# load_dotenv()

usernames['wikipedia']['*'] = 'SodiumBot'
usernames['meta']['*'] = 'SodiumBot'
usernames['commons']['*'] = 'SodiumBot'
usernames['wikidata']['*'] = 'SodiumBot'
usernames['wiktionary']['*'] = 'SodiumBot'
usernames['wikibooks']['*'] = 'SodiumBot'
usernames['wikinews']['*'] = 'SodiumBot'
usernames['wikiquote']['*'] = 'SodiumBot'
usernames['wikisource']['*'] = 'SodiumBot'
usernames['wikiversity']['*'] = 'SodiumBot'
usernames['wikivoyage']['*'] = 'SodiumBot'
  
info = (os.environ.get('CONSUMER_TOKEN'),os.environ.get('CONSUMER_SECRET'), os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_SECRET'))
authenticate['*.wikipedia.org'] = info
authenticate['*.wikimedia.org'] = info
authenticate['*.wikidata.org'] = info
authenticate['*.wiktionary.org'] = info
authenticate['*.wikibooks.org'] = info
authenticate['*.wikinews.org'] = info
authenticate['*.wikiquote.org'] = info
authenticate['*.wikisource.org'] = info
authenticate['*.wikiversity.org'] = info
authenticate['*.wikivoyage.org'] = info
authenticate['*.mediawiki.org'] = info
  
