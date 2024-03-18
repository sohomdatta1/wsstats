import pywikibot as pwb

bottestlist = [
    'it',
    'en',
    'bn',
    'pa',
    'pl',
    'fr',
]

for dom in bottestlist:
    site = pwb.Site(dom,fam='wikisource')
    page = pwb.Page(site,"User:SodiumBot/sandbox")
    page.text = 'Test'
    page.save('Test edit to validate infra for statistics task')
