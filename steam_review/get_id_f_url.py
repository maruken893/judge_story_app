def get_id(url):
    url = url[35:]
    id = ''
    for w in url:
        if w != '/':
            id += w
        else:
            break
    return id