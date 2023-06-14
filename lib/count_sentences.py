#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self._value = value
# passes first pytest- MyString in count_sentences.py is a class with the name "MyString". .    
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)
# this clears pytest #2- MyString in count_sentences.py prints "The value must be a string." if not string. . 

  def is_sentence(self):
    return self._value.endswith('.')
# this clears number 3-MyString in count_sentences.py returns True if value ends with a period and False otherwise. .
  
  def is_question(self):
    return self._value.endswith("?")
# clears number 4- MyString in count_sentences.py returns True if value ends with a question mark and False otherwise. F   
  
  def is_exclamation(self):
    return self._value.endswith("!")
  # clears number 5 -MyString in count_sentences.py returns True if value ends with an exclamation mark and False otherwise. F 
  
  def count_sentences(self):
    value = self.value
    for marks in ['!' , '?']:
      value = value.replace(marks, '.')
    
    sentences = [ s for s in value.split('.') if s]

    return len(sentences)
  # clears final pytest- MyString in count_sentences.py returns the number of sentences in the value. .                                                                                             [100%]
