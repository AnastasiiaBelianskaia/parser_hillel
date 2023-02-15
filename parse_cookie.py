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
