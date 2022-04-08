def waf(url, title):
    """Don't XSS!"""
    black_list = "<>'\""
    for c in black_list:
        if c in url or c in title:
            return False
    return True


def make_exhibition_page(url, title):
    valid = waf(url, title)
    if valid:
        return f"<div><img src={url}></div><div>Title: {title}</div>"
    else:
        return "<div>Are you hacker?</div>"
