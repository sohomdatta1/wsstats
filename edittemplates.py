import os
import pywikibot as pwb

bottmpldomains = [
    'en',
    'bn'
]

def safe_put(page, num):
    page.text = num
    page.save('Unattended update of statistics templates (ping [[User talk:Sohom Datta|Sohom Datta]] for questions)')

def spaced_int(i,sep):
    result = repr(i)[-3:]
    if i>999: 
        result = repr(i)[-6:-3] + sep + result
    if i>999999:
        result = repr(i)[:-6] + sep + result
    return result

def edittemplates(stats):
    if not os.environ.get( 'ENABLE_BOT' ):
        return
    
    for dom in bottmpldomains:
        sep = ''
        if dom=='fr':
            sep=' '
        elif dom == 'en':
            sep=','
        else:
            sep = ''

        num, num_q0, num_q2, num_q3, num_q4, num_tr, num_texts, num_disambig = stats[dom]
        percent = num_tr*100./(num_texts-num_disambig)
        num_q1 = num - (num_q0 + num_q2 + num_q3 + num_q4 )

        site = pwb.Site(dom,fam='wikisource')
        page = pwb.Page(site,"Template:PAGES_NOT_PROOFREAD")
        safe_put(page, spaced_int(num_q1,sep))
        page = pwb.Page(site,"Template:ALL_PAGES")
        safe_put(page, spaced_int(num,sep))
        page = pwb.Page(site,"Template:PR_TEXTS")
        safe_put(page, spaced_int(num_tr,sep))
        page = pwb.Page(site,"Template:ALL_TEXTS")
        safe_put(page, spaced_int(num_texts - num_disambig,sep))
        page = pwb.Page(site,"Template:PR_PERCENT")
        safe_put(page, "%.2f"%percent)