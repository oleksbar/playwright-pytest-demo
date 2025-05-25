def test_date_picker(page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.click("#dateOfBirthInput")
    page.select_option(".react-datepicker__month-select", "2")  #March
    page.select_option(".react-datepicker__year-select", "1993")
    page.click(".react-datepicker__day--023:not(.react-datepicker__day--outside-month)")
    selected_date = page.locator("#dateOfBirthInput").input_value()
    assert selected_date == "23 Mar 1993"

def test_file_upload(page, tmp_path):
    page.goto("https://demoqa.com/automation-practice-form")

    # Create a dummy file
    dummy_file = tmp_path / "dummy.txt"
    dummy_file.write_text("This is a test file.")

    page.set_input_files("#uploadPicture", str(dummy_file))

    uploaded_name = page.locator("#uploadPicture").input_value()
    assert "dummy.txt" in uploaded_name

def test_select_state_city(page):
    page.goto("https://demoqa.com/automation-practice-form")

    # Scroll to the dropdowns if necessary
    page.locator("#state").scroll_into_view_if_needed()

    # Click and select state
    page.click("#state")
    page.click("div[id^='react-select-3-option-0']")  # NCR

    # Click and select city
    page.click("#city")
    page.click("div[id^='react-select-4-option-0']")  # Delhi
    page.click("#currentAddress")

    # Verify state and city text
    assert page.locator("#state").text_content().strip() == "NCR"
    assert page.locator("#city").text_content() == "Delhi"

