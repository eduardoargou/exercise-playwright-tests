from playwright.sync_api import Page
from pages.orders_and_returns import OrdersAndReturns

orders_url = "/sales/guest/form"

email = "automated@test.com"
last_name = "Test"
order_id = "000042360"
zipcode = "12345"

incorrect_email = "automated2@test.com"
incorrect_last_name = "Testing"
incorrect_zipcode = "12348"
inexisting_order_id = "000042363"

def test_track_order_with_email(page: Page) -> None:
    page.goto(orders_url)
    orders = OrdersAndReturns(page)
    orders.fill_order_id(order_id)
    orders.fill_last_name(last_name)
    orders.select_find_order_by('email')
    orders.fill_email(email)
    orders.click_continue()
    orders.validate_order_page_title(order_id)

def test_track_order_with_zipcode(page: Page) -> None:
    page.goto(orders_url)
    orders = OrdersAndReturns(page)
    orders.fill_order_id(order_id)
    orders.fill_last_name(last_name)
    orders.select_find_order_by('zip')
    orders.fill_zipcode(zipcode)
    orders.click_continue()
    orders.validate_order_page_title(order_id)

def test_track_inexisting_order_error(page: Page) -> None:
    page.goto(orders_url)
    orders = OrdersAndReturns(page)
    orders.fill_order_id(inexisting_order_id)
    orders.fill_last_name(last_name)
    orders.select_find_order_by('email')
    orders.fill_email(email)
    orders.click_continue()
    orders.validate_error_message()

def test_track_order_with_incorrect_last_name(page: Page) -> None:
    page.goto(orders_url)
    orders = OrdersAndReturns(page)
    orders.fill_order_id(order_id)
    orders.fill_last_name(incorrect_last_name)
    orders.select_find_order_by('email')
    orders.fill_email(email)
    orders.click_continue()
    orders.validate_error_message()

def test_track_order_with_incorrect_email(page: Page) -> None:
    page.goto(orders_url)
    orders = OrdersAndReturns(page)
    orders.fill_order_id(order_id)
    orders.fill_last_name(last_name)
    orders.select_find_order_by('email')
    orders.fill_email(incorrect_email)
    orders.click_continue()
    orders.validate_error_message()

def test_track_order_with_incorrect_zipcode(page: Page) -> None:
    page.goto(orders_url)
    orders = OrdersAndReturns(page)
    orders.fill_order_id(order_id)
    orders.fill_last_name(last_name)
    orders.select_find_order_by('zip')
    orders.fill_zipcode(incorrect_zipcode)
    orders.click_continue()
    orders.validate_error_message()
