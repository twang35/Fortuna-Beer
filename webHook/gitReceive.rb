require 'sinatra'
require 'json'

set :port, 4321
set :environment, :production

$watirLog = nil

def runTest(name)
	return $watirLog.write("#{name}: " << `ruby ../testing/#{name}` << "\n")
end

post '/payload' do
  pull = `git pull`
  
  $watirLog = File.open("../testing/watirLog.txt", 'a')

  push = JSON.parse(request.body.read)

  $watirLog.write("Commit message: " << push["commits"][0]["message"] << "\n\n")

  $watirLog.write(pull << "\n\n")
  # runTest("login.rb")
  # runTest("login_logout.rb")
  # runTest("login_randBeer.rb")
  # runTest("login_rate.rb")
  # runTest("randBeer.rb")
  
  $watirLog.write("=====\n\n\n")

  $watirLog.close
end