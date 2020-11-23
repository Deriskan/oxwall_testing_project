import pytest

# TODO: parametrize test
# @pytest.mark.parametrize(......)
def test_create_new_post(app, login):
    number_of_posts = app.count_posts()
    app.create_new_post("New text")
    app.wait_new_post_appear(number_of_posts)


# def test_create_empty_post(app, login):
#     number_of_posts = app.count_posts()
#     app.create_new_post(post_text='')
#     app.wait_new_post_appear(number_of_posts)


def test_login(app):
    app.login_as('admin', 'pasdf')
