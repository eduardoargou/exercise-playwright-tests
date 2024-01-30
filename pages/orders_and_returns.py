from playwright.sync_api import Page, expect

class OrdersAndReturns:
    # Locators
    input_order_id = '#oar-order-id'
    input_last_name = '#oar-billing-lastname'
    select_by = '#quick-search-type-id'
    input_email = '#oar_email'
    input_zipcode = '#oar_zip'
    button_continue = 'button.submit'
    error_message = 'div.message-error'
    order_page_title = 'span.base'
    error_text = "You entered incorrect data. Please try again."

    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_order_id(self, order_id: str) -> None:
        input = self.page.locator(self.input_order_id)
        expect(input).to_be_visible()
        input.fill(order_id)

    def fill_last_name(self, last_name: str) -> None:
        input = self.page.locator(self.input_last_name)
        expect(input).to_be_visible()
        input.fill(last_name)

    def select_find_order_by(self, opt: str) -> None:
        select = self.page.locator(self.select_by)
        expect(select).to_be_visible()
        select.select_option(opt)

    def fill_email(self, email: str) -> None:
        input = self.page.locator(self.input_email)
        expect(input).to_be_visible()
        input.fill(email)

    def fill_zipcode(self, zipcode: str) -> None:
        input = self.page.locator(self.input_zipcode)
        expect(input).to_be_visible()
        input.fill(zipcode)

    def click_continue(self) -> None:
        input = self.page.locator(self.button_continue)
        expect(input).to_be_visible()
        input.click()

    def validate_error_message(self) -> None:
        error = self.page.locator(self.error_message)
        expect(error).to_be_visible()
        print('Expected:', self.error_text)
        print('Actual:', error.inner_text())
        assert error.inner_text().strip() == self.error_text

    def validate_order_page_title(self, order_id: str) -> None:
        title = self.page.locator(self.order_page_title)
        expect(title).to_be_visible()
        title_order_id = title.inner_text().split()[-1]
        assert title_order_id == order_id
