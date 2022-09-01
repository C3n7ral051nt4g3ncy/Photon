import os


def mirror(url, response):
    if response == 'dummy':
        return
    clean_url = url.replace('http://', '').replace('https://', '').rstrip('/')
    parts = clean_url.split('?')[0].split('/')
    root = parts[0]
    webpage = parts[-1]
    parts.remove(root)
    try:
        parts.remove(webpage)
    except ValueError:
        pass
    prefix = f'{root}_mirror'
    try:
        os.mkdir(prefix)
    except OSError:
        pass
    suffix = ''
    if parts:
        for directory in parts:
            suffix += f'{directory}/'
            try:
                os.mkdir(f'{prefix}/{suffix}')
            except OSError:
                pass
    path = f'{prefix}/{suffix}'
    trail = ''
    if '.' not in webpage:
        trail += '.html'
    name = 'index.html' if webpage == root else webpage
    if len(url.split('?')) > 1:
        trail += '?' + url.split('?')[1]
    with open(path + name + trail, 'w+') as out_file:
        out_file.write(response.encode('utf-8'))
