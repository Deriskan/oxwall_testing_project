import pytest
import json
import os.path
from conftest import PROJECT_DIR
from data.random_string import random_string
from pages.internal_pages.dashbord_page import DashboardPage

with open(os.path.join(PROJECT_DIR, "data", "post.json"), encoding="utf8") as f:
    post_text_list = json.load(f)

post_text_list.extend([random_string(min_len=3, max_len=255) for _ in range(3)])


@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.parametrize("post_text", post_text_list)
def test_create_new_post(driver, logged_user, post_text, db):
    dashboard_page = DashboardPage(driver)
    # number_of_posts = dashboard_page.count_posts()
    number_of_posts = len(dashboard_page.posts)
    dashboard_page.create_new_post(post_text)
    dashboard_page.wait_new_post_appear(number_of_posts)
    assert db.get_last_text_post() == post_text
    first_post = dashboard_page.posts[0]
    assert first_post.text == post_text
    assert first_post.user == logged_user
    assert first_post.time == "within 1 minute"

    # first_post.delete()
    # dashboard_page.posts[-1].delete()

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
