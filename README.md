Author: Eric Engstfeld

Date: 3 July 2017

# Security Manager
For demo purpose.

# Basics
Simple Flask REST API which allows user accounts security handlement. Default roles are:

  * 1: admin 
  * 2: worker


# API Rest

## User Creation

  * URL: /api/user
  * Method: POST
  * Requirements: Sent message must be in JSON format contaning user information. i. e.:

<pre>
{
    "username": "david",
    "name": "David Bowie",
    "password": "bowie",
    "role_id": 1,
    "email": "davidbowie@gmail.com"
}
</pre> 

  * Returns: On success (a), returns user object. On error or failure (b) returns a message explaining the issue.

(a)

<pre>
{
    "success": True,
    "data": {
        "username": "david",
        "name": "David Bowie",
        "role_id": 1,
        "email": "davidbowie@gmail.com"
    }
}
</pre>

(b)

<pre>
{
    "success": False,
    "data": "User 'david' already exists"
}
</pre>

## User Edition

  * URL: /api/user/{username}
  * Method: PUT
  * Requirements: Sent message must be in JSON format contaning user information to edit. i. e.:

<pre>
{
    "email": "david_bowie@gmail.com"
}
</pre> 

  * Returns: On success (a), returns the modified user object. On error or failure (b) returns a message explaining the issue.

(a)

<pre>
{
    "success": True,
    "data": {
        "username": "david",
        "name": "David Bowie",
        "role_id": 1,
        "email": "david_bowie@gmail.com"
    }
}
</pre>

(b)

<pre>
{
    "success": False,
    "data": "User 'david2' has not been found"
}
</pre>


## Get User information

  * URL: /api/user/{username}
  * Method: GET
  * Headers: Authorization header contaning the login TOKEN
  * Returns: On success (a), returns a message with requested user information. On error or failure (b) returns a message explaining the issue.

(a)

<pre>
{
    "success": True,
    "data": {
        "username": "david",
        "name": "David Bowie",
        "role_id": 1,
        "email": "davidbowie@gmail.com"
    }
}
</pre>

(b)

<pre>
{
    "success": False,
    "data": "User 'david22' has not been found"
}
</pre>

## Delete User

  * URL: /api/user/{username}
  * Method: DELETE
  * Headers: Authorization header contaning the login TOKEN
  * Returns: On success (a), returns the modified user information. On error or failure (b) returns a message explaining the issue.

(a)

<pre>
{
    "success": True,
    "data": {
        "username": "david",
        "name": "David Bowie",
        "role_id": 1,
        "email": "davidbowie@gmail.com"
    }
}
</pre>

(b)

<pre>
{
    "success": False,
    "data": "User 'david2' has not been found"
}
</pre>


## Login 

  * URL: /api/login
  * Method: POST
  * Requirements: Sent message must be in JSON format contaning username and password information. i. e.:

<pre>
{
    "username": "david",
    "password": "bowie"
}
</pre> 

  * Returns: On success (a), returns a TOKEN which can be used on Authorization header to access protected services. On error or failure (b) returns a message explaining the issue.

(a)

<pre>
{
    "success": True,
    "data": { 
        "token": "DQWIDQWJDOQIDJIJO98$WQD",
        "user": {
            "username": "david",
            "name": "David Bowie",
            "groups": ["admin"],
            "email": "davidbowie@gmail.com"
        }
    }
}
</pre>

(b)

<pre>
{
    "success": False,
    "data": "Invalid credentials"
}
</pre>

## My Movements (not implemented yet)

  * URL: /api/audit?username={username}
  * Method: GET
  * Headers: Authorization header contaning the login TOKEN
  * Returns: On success (a), returns all user movements (login information, requests done, etc). On error or failure (b) returns a message explaining the issue.

(a)

<pre>
{
    "success": True,
    "data": [{
        "username": "david",
        "action": "login",
        "date": "29 June 2017 12:23",
        "origin_ip": "127.0.0.1"
    },{
        "username": "david",
        "action": "user_creation",
        "date": "29 June 2017 12:45",
        "additional_data": "eric" # Created user username,
        "origin_ip": "127.0.0.1"
    }]
}
</pre>

(b)

<pre>
{
    "success": False,
    "data": "Not authorized"
}
</pre>

# TO DO List

  * Implement a good and secure authentication mechanism (encrypt password)
  * Use REDIS for token/session management 
  * Add token timeout mechanism and automatically renewal when used
  * Add email verification system
  * Add Front-end to manage accounts

# Contact
For more information about this you can send me an email: exengstfeld@gmail.com
