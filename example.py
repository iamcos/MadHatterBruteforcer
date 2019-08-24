# -*- coding: utf-8 -*-
"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from __future__ import print_function, unicode_literals

import regex
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_3


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


print('Hi, welcome to Python Pizza')

questions = [
    {
        'type': 'confirm',
        'name': 'toBeDelivered',
        'message': 'Is this for delivery?',
        'default': False
    },
    {
        'type': 'input',
        'name': 'phone',
        'message': 'What\'s your phone number?',
        'validate': PhoneNumberValidator
    },
    {
        'type': 'list',
        'name': 'acconts',
        'message': 'Select account',
        'choices': [guids],
    },
    {
        'type': 'input',
        'name': 'comments',
        'message': 'Any comments on your purchase experience?',
        'default': 'Nope, all good!'
    },
    {
        'type': 'list',
        'name': 'prize',
        'message': 'For leaving a comment, you get a freebie',
        'choices': ['cake', 'fries'],
        'when': lambda answers: answers['comments'] != 'Nope, all good!'
    }
]

answers = prompt(questions, style=custom_style_3)
print('Order receipt:')