from seleniumbase import SB

with SB(uc=True, test=True) as oncello:

    url = "https://kick.com/brutalles"
    oncello.uc_open_with_reconnect(url, 4)
    oncello.sleep(4)
    oncello.uc_gui_click_captcha()
    oncello.sleep(1)
    oncello.uc_gui_handle_captcha()
    oncello.sleep(4)
    if oncello.is_element_present('button:contains("Accept")'):
        oncello.uc_click('button:contains("Accept")', reconnect_time=4)
    if oncello.is_element_visible('#injected-channel-player'):
        oncello2 = oncello.get_new_driver(undetectable=True)
        oncello2.uc_open_with_reconnect(url, 5)
        oncello2.uc_gui_click_captcha()
        oncello2.uc_gui_handle_captcha()
        oncello.sleep(10)
        if oncello2.is_element_present('button:contains("Accept")'):
            oncello2.uc_click('button:contains("Accept")', reconnect_time=4)
        while oncello.is_element_visible('#injected-channel-player'):
            oncello.sleep(10)
        oncello.quit_extra_driver()
    oncello.sleep(1)
