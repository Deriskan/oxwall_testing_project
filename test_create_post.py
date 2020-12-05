import pytest

from pages.internal_pages.dashbord_page import DashboardPage


def test_create_new_post(driver, login):
    dashboard_page = DashboardPage(driver)
    number_of_posts = dashboard_page.count_posts()
    dashboard_page.create_new_post("New text")
    dashboard_page.wait_new_post_appear(number_of_posts)


# # TODO: parametrize test
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
