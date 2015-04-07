require 'sinatra'
require 'json'

set :port, 4321

post '/payload' do
  push = JSON.parse(request.body.read)
  puts "I got some JSON: #{push.inspect}"


  # test = `ruby ../testing/login.rb`
  # File.open("../testing/watirLog.txt", 'a') { |file| file.write("login.rb: " << test << "\n") }

  # test = `ruby ../testing/login-logout.rb`
  # File.open("../testing/watirLog.txt", 'a') { |file| file.write("login-logout.rb: " << test << "\n") }



  # File.open("../testing/watirLog.txt", 'a') { |file| file.write("=====\n\n\n") }
end