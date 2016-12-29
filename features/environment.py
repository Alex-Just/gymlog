from selenium import webdriver


def before_all(context):
    context.browser = webdriver.PhantomJS()
    # context.browser = webdriver.Chrome()

    context.browser.implicitly_wait(2)

    if context.browser.get_window_size()['width'] < 800:
        context.browser.set_window_size(1280, 1024)


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
