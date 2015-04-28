Banner grabbing script I hacked up in python. Nothing fancy, but it does the job.

Usage: bannerman.py [host] [method] [uri] [port]
[uri] is optional, defaults to /
[port] is optional, defaults to 80

allowed methods: get, put, connect, trace, head, options

example usage: python bannerman.py www.google.com head / 80
