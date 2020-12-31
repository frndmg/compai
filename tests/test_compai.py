from compai import dict_map


def test_dict_map():
    assert dict_map(a=int)(dict(a='123')) == dict(a=123)
