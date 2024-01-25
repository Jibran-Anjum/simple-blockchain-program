# Simple Blockchain Program

## Required Skills

1. know about [Blockchain](#Blockchain?)
2. know about [OOP-Python](#OOP-Python)
3. learn how to use the [hashlib module](#hashlib)
4. learn how to use the [datetime module](#datetime)

### Blockchain?
It is a database or ledger shared among computers network's nodes. It is a system for maintaining a secure and decentralized record of transactions. Blockchains can be used to make data in any industry immutable —  the term used to describe the inability to be altered.

### OOP-Python
Object oriented programming is a programming paradigm that can be used in order to solve real-world problems. In object oriented programming we're gonna have classes and objects created basedd on those classes.

### hashlib
In order to use the hashlib module we first need to import it.

After importing the hashlib module we create a variable that is to hold the hashing algorithm (we're using sha-256). Then we simply provide the string or any other type of value that we want to be coverted into hash of type byte.

You can now feed this object with bytes-like objects (normally bytes) using the update method.

Note:- A prefix of 'b' or 'B' is ignored in Python 2; it indicates that the literal
should become a bytes literal in Python 3

### datetime
In order to get the current date and time we use the datetime module. I did read that there are other cooler things that you can do with this module. But since, we're only going to be using it in order to get the current time in which the transaction happens, we don't really need to go into too much details.


