#!/usr/bin/python

# https://stackoverflow.com/questions/55596379/ansible-enumerate-list-when-looping-on-list-product-nested-loop

def filter_enumerate(v):
    return list(enumerate(v))


class FilterModule (object):
    def filters(self):
        return {
            'enumerate': filter_enumerate,
        }
