import pytest
import json

from pages.internal_pages.dashbord_page import DashboardPage

with open("data/post.json", encoding="utf8") as f:
    post_text_list = json.load(f)


@pytest.mark.parametrize("post_text", post_text_list)
def test_create_new_post(driver, login, post_text):
    dashboard_page = DashboardPage(driver)
    number_of_posts = dashboard_page.count_posts()
    dashboard_page.create_new_post(post_text)
    dashboard_page.wait_new_post_appear(number_of_posts)
    posts = dashboard_page.get_posts()
    assert post_text in posts[0].text


# # @pytest.mark.parametrize(......)
# def test_create_new_post(app, login):
#     number_of_posts = app.count_posts()
#     app.create_new_post("New text")
#     app.wait_new_post_appear(number_of_posts)


# def test_create_empty_post(app, login):
#     number_of_posts = app.count_posts()
#     app.create_new_post(post_text='')
#     app.wait_new_post_appear(number_of_posts)


# def test_login(app):
#     app.login_as('admin', 'pasdf')
