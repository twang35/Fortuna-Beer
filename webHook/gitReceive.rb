require 'sinatra'
require 'json'
require 'headless'

headless = Headless.new
headless.start

set :port, 4321

$watirLog = nil

def runTest(name)
	return $watirLog.write("#{name}: " << `ruby ../testing/#{name}` << "\n")
end

post '/payload' do
  $watirLog = File.open("../testing/watirLog.txt", 'a')

  push = JSON.parse(request.body.read)

  $watirLog.write(push["commits"][0]["message"] << "\n\n")

  puts "\n\n" << push["commits"][0]["message"] << "\n"

  runTest("login.rb")
  runTest("login_logout.rb")
  runTest("login_randBeer.rb")
  runTest("login_rate.rb")
  runTest("randBeer.rb")
  
  $watirLog.write("=====\n\n\n")

  $watirLog.close
end

headless.destroy