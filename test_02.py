from gb import auth, get_title_posts_page, create_post


def test_step1():
    assert auth()[1] == 200, "step1 FAIL"


def test_step2(authorization, found_title):
    assert found_title in get_title_posts_page(authorization[0], 0)[0], "step2 FAIL"


def test_step3(authorization, new_title):
    create_post(authorization[0], new_title, "description", "test content")
    assert new_title in get_title_posts_page(authorization[0], 0, not_own=False)[0], "step3 FAIL"



