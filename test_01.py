from check_text import check_text


def test_step1(incorrect_word, correct_word):
    assert correct_word in check_text(incorrect_word), "step1 FAIL"
