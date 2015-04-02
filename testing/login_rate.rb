require 'watir-webdriver'
b = Watir::Browser.new
b.goto 'fortuna.tony-wang.com'
b.input(:id => 'login-username').wait_until_present
b.text_field(:id => 'login-username').when_present.set 'a'
b.text_field(:id => 'login-password').wait_until_present
b.text_field(:id => 'login-password').set 'a'

b.button(:id => 'btnLogIn').click
b.button(:id => 'btnLogOut').wait_until_present

b.radio(:id => 'id_rating_3').set

b.button(:id => 'btnRate').click

puts "Success"