require 'watir-webdriver'
require 'headless'

headless = Headless.new
headless.start

b = Watir::Browser.new
b.goto 'fortuna.tony-wang.com'

b.button(:id => 'btnRandBeer').wait_until_present

b.button(:id => 'btnRandBeer').click

puts "Success"

b.close

headless.destroy