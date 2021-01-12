How to get a random quote:

curl -u root -X Get -i http://0.0.0.0:3000/api/v1/get-quote

How to post a quote:

curl -u <username> -i -H "Content-Type: application/json" -X POST -d '{"quote":"Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve. -- Mary Kau Ash"}' http://0.0.0.0:3000/api/v1/set-quote