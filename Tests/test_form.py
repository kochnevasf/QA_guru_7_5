import os
from selene import browser
from selene import be, have


def test_positive(browser_management):
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Svetlana')
    browser.element('#lastName').should(be.blank).type('Ko')
    browser.element('#userEmail').should(be.blank).type('test@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('8971234567')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select>option[value='11']").click()
    browser.element(".react-datepicker__year-select>option[value='1988']").click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('files/san-diego-night-view-united-states-boats.jpeg'))
    browser.element('#currentAddress').type("Moscow Region")
    browser.element('#react-select-3-input').type('ncr').press_enter()
    browser.element('#react-select-4-input').type('delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Svetlana Ko'
                                               and 'test@mail.ru'
                                               and 'Female'
                                               and '8971234567'
                                               and '19 December,1988'
                                               and 'Maths'
                                               and 'Music'
                                               and 'san-diego-night-view-united-states-boats.jpeg'
                                               and 'Moscow Region'
                                               and 'NCR Delhi'))
    print("выполнено успешно")