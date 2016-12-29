from urllib.parse import urljoin

from allauth.account.models import EmailAddress
from behave import *
from django.contrib.auth import get_user_model

TEST_USERNAME = 'gymLogUserName'
TEST_USERMAIL = 'gymLogUserName@mail.com'
TEST_USERPASS = 'FGoTxAW6ld!K5*qsvhU*0d6A6'


@given("I am a logged-in user")
def given_i_am_logged_in(context):
    # create_pre_authenticated_session(context)
    # context.browser.get(context.base_url)

    # create test user
    User = get_user_model()
    u = User.objects.create_user(
        email=TEST_USERMAIL, username=TEST_USERNAME, password=TEST_USERPASS)

    EmailAddress.objects.create(user_id=u.id, verified=True)

    # login
    context.browser.get(context.base_url + '/accounts/login/')

    input = context.browser.find_element_by_id('id_login')
    input.send_keys(TEST_USERNAME)
    input = context.browser.find_element_by_id('id_password')
    input.send_keys(TEST_USERPASS)
    input.send_keys('\n')


@when('I will see a link to "{link_text}"')
def see_a_link(context, link_text):
    context.browser.find_element_by_link_text(link_text)


@when('I go to "{url}"')
def goto_url(context, url):
    context.browser.get(urljoin(context.base_url, url))


@then("I will see an invintation to create a new program")
def see_text(context):
    context.test.assertIn('Create a new program', context.browser.page_source)
