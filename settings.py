template_path = 'templates'

def get_config(author, name):
    return {
        'PROJ_NAME': name,
        'PROJ_DESC': name,
        'PROJ_URL': 'https://github.com/%s/%s/' % (author, name),
        'AUTHOR_NAME': author,
        'AUTHOR_EMAIL': '%s@gmail.com' % author,
    }
