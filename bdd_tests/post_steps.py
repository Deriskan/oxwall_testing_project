from pytest_bdd import given, when, then


@given("I as a logged user")
def logged_admin(admin, main_page, login_page):
    user = admin
    main_page.sign_in_menu_click()
    login_page.input_username(user.username)
    login_page.input_password(user.password)
    login_page.sign_in_click()
    return user


@given("initial amount of post in Oxwall database")
def initial_posts(dashboard_page):
    return len(dashboard_page.posts)


@when("I add a new post with <input_text> in Dashboard page")
def create_post(dashboard_page, input_text):
    dashboard_page.create_new_post(input_text)


@then("a new post block appears before old table of posts")
def wait_new_post(dashboard_page, initial_posts):
    dashboard_page.wait_new_post_appear(initial_posts)


@then('this post block has this <output_text> and author as this user and time "within 1 minute"')
def verify_post(dashboard_page, db, output_text, logged_admin):
    first_post = dashboard_page.posts[0]
    assert first_post.text == output_text, f"Visible post text is not equal input text: {first_post.text} != {output_text}"
    assert first_post.user == logged_admin, f"User of post  is not logged user: {first_post.user} != {logged_admin}"
    assert first_post.time == "within 1 minute", f"Post time is not 'within 1 minute: {first_post.time}'"
