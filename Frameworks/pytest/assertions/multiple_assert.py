def test_multiple_assert():
    num_list=[1,2,3,4,5]
    assert len(num_list)==5
    assert num_list[0]==1
    assert 3 not in num_list
    