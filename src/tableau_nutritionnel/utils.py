def soft_pop(dic: dict, key, default) :
    """
     Return dic[key] if it exists, else default
       @ input  : dic {dictionnary} Dictionnary
                  key {} Potential key
                  default {} Value to return if dic[key] does not exists
       @ output : {} dic[key] if key in dic else default
    """
    try :
        return(dic[key])
    except KeyError :
        return(default)

def unique(liste) :
  """
  Return a list of one sample of each element in the list
    @ input  : liste {list} Liste
    @ output : {list} Liste with exactly one sample of each of the unique element 
  """
  already_seen = {} 
  result = []
  for val in liste :
    if val in already_seen :
      pass
    else :
      already_seen[val] = True
      result.append(val)
  return result

if __name__ == "__main__" : 
  pass
