require 'watir-webdriver'
b = Watir::Browser.new
b.goto 'fortuna.tony-wang.com'

b.button(:id => 'btnRandBeer').wait_until_present

b.button(:id => 'btnRandBeer').click

puts "Success"

b.close