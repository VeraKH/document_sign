import re
from sign_document_page import SignDocumentPage
from playwright.sync_api import Page

def test_document_signed(page: Page):
    sign_document_page = SignDocumentPage(page)
    sign_document_page.open()
    sign_document_page.fill_name('Vera')
    sign_document_page.click_next_button()
    sign_document_page.click_sign_button()
    sign_document_page.verify_document_signing_confirmation_text_appears()
