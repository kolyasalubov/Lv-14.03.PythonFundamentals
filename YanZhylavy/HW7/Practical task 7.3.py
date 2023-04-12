def characters(word:str)->dict:
  """
  The function returns dictionary, whitch keys are characters from
  entered string and values are numbers of their appearances.
  """
  out = {}
  for item in word:
    out.update({item:word.count(item)})
  return out
 