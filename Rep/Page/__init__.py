from selenium.webdriver.common.by import By
"""
    添加通讯录
"""
# 添加用户按钮
add_user = (By.ID, "com.android.contacts:id/floating_action_button")
# 点击本地保存
save_local = (By.XPATH, "//*[contains(@text,'本地')]")
# 定位姓名
send_name = (By.XPATH, "//*[contains(@text,'姓名')]")
# 定位手机号
send_phone = (By.XPATH, "//*[contains(@text,'电话')]")
# 点击返回保存按钮
click_save_back = (By.XPATH, "//*[contains(@content-desc,'向上导航')]")

"""
    设置
"""
search_btn = (By.ID, "com.android.settings:id/search")
search_text = (By.ID, "android:id/search_src_text")
search_return = (By.CLASS_NAME, "android.widget.ImageButton")