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


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name==Dima') == {'name': '=Dima'}
    assert parse('https://example.com/path/to/page?name=') == {'name': ''}
    assert parse('https://example.com/path/to/page?name=?&color') == {'name': '?'}
    assert parse('https://example.com/path/to/page?name=ferret=main&') == {'name': 'ferret=main'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&user=main') == {'name': 'ferret', 'color': 'purple', 'user': 'main'}
    assert parse('https://example.com/?path/to/page?name=ferret&color=purple') == {'path/to/page?name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&=') == {'name': 'ferret', '': ''}
    assert parse('https://example.com/path/to/page?1=?') == {'1': '?'}
    assert parse('https://example.com/path/to/page?name=ferret=') == {'name': 'ferret='}
    assert parse('https://example.com/path/to/page?&') == {}


def parse_cookie(query: str) -> dict:
    cookie_to_dict={}
    pairs = query.split(';')
    for pair in pairs:
        if '=' in pair:
            pair = pair.split('=', maxsplit=1)
            cookie_to_dict[pair[0]] = pair[1]
    return cookie_to_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=') == {'name': ''}
    assert parse_cookie('name') == {}
    assert parse_cookie('=') == {'': ''}
    assert parse_cookie('name===Dima;age=28;') == {'name': '==Dima', 'age': '28'}
    assert parse_cookie('name==;') == {'name': '='}
    assert parse_cookie('name;=Dima;') == {'': 'Dima'}
    assert parse_cookie('name=Dima;name=Olga') == {'name': 'Olga'}
    assert parse_cookie('name=Dima;age=28;id=0000;') == {'name': 'Dima', 'age': '28', 'id': '0000'}
    assert parse_cookie('=;=') == {'': ''}
    assert parse_cookie(';name=Dima;') == {'name': 'Dima'}