from playwright.sync_api import Page, expect

class SignDocumentPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.get_by_label("Full name")
        self.next_button = page.get_by_role("button", name="Next")
        self.sign_button = page.get_by_role("button", name="Sign")
        self.document_signed_title = page.get_by_text("Document signed!")

    def open(self):
        self.page.goto("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")

    def fill_name(self, name: str):
        self.name_input.type(name)

    def click_next_button(self):
        self.next_button.click()

    def click_sign_button(self):
        self.sign_button.click()

    def verify_document_signing_confirmation_text_appears(self):
        expect(self.document_signed_title).to_be_visible()
