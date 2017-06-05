Banner grabbing script I hacked up in python. Nothing fancy, but it does the job.

Usage: bannerman.py [host] [method] [uri] [port]

[uri] is optional, defaults to /

[port] is optional, defaults to 80

allowed methods: get, put, connect, trace, head, options

example usage: python bannerman.py www.google.com head / 80


bannerman-edit.py is a version of the script that uses the same arguements, but adds in a parser to retrieve the Server version from the header returned from the server.
