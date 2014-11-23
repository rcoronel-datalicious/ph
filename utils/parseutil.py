

def process(val):
    if val == '':
        return ''

    val = "%s" % (val)
    val = val.replace('[rc]', '; ')
    return val