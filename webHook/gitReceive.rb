require 'sinatra'
require 'json'

set :port, 4321

$watirLog = nil

def runTest(name)
	return $watirLog.write("#{name}: " << `ruby ../testing/#{name}` << "\n")
end

post '/payload' do
  $watirLog = File.open("../testing/watirLog.txt", 'a')

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