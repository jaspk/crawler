from urllib.parse import urlparse

# Get domain name(Example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# Get subdomain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

# print(get_sub_domain_name('https://help.ubuntu.com/16.04/ubuntu-help/index.html'))