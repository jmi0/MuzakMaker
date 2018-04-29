def stayInKey(root):
  full_scale = []
  pattern = [2, 2, 1, 2, 2, 2, 1]
  i = 0
  j = 0
  full_scale.append(root)
    
  while i < 127:
    i = root + pattern[j]
    root = i
    full_scale.append(i)
    
    if j == 6:
      j = 0
    else:
      j +=  1
    i += 1
  return full_scale
