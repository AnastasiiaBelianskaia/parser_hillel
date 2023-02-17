# PARSER
* This code was written in learning objectives. 
* It contains two functions, that can parse url and cokkies without urllib module.
```python
def parse(query: str) -> dict:
    url_to_dict = {}
    division_by_question_mark = query.split('?', maxsplit=1)
    for pairs in division_by_question_mark:
        pairs = pairs.split('&')
        for pair in pairs:
            if '=' in pair:
                pair = pair.split('=', maxsplit=1)
                url_to_dict[pair[0]] = pair[1]
    return url_to_dict
```
```python
def parse_cookie(query: str) -> dict:
    cookie_to_dict={}
    pairs = query.split(';')
    for pair in pairs:
        if '=' in pair:
            pair = pair.split('=', maxsplit=1)
            cookie_to_dict[pair[0]] = pair[1]
    return cookie_to_dict
```
