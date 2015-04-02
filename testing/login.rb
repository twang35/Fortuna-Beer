require 'watir-webdriver'
b = Watir::Browser.new
b.goto 'fortuna.tony-wang.com'
b.text_field(:id => 'id_username').wait_until_present
b.text_field(:id => 'id_username').when_present.set 'a'
b.text_field(:id => 'id_password').wait_until_present
b.text_field(:id => 'id_password').set 'a'

b.select_list(:id => 'entry_1').selected? 'Ruby'
b.button(:name => 'submit').click
b.text.include? 'Thank you'