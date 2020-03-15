## We will use a binary tree during our truth evaluation of a particular 
## formula.

class Node: 
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left 
    self.right = right 

  def insert_left(self, new_node):
    self.left = new_node 
  
  def insert_right(self, new_node):
    self.right = new_node


class Variable:
  ''' 
  The propositional variable Variable can only be a Single letter
  '''

  def __init__(self, name, neg = 0, subscript=None):
    if len(name) > 1:
      raise Exception("Please pass a 1 letter variable")
    else:
      self.name = name
      self.neg = neg 

  def __str__(self):
    if self.neg == 0:
      return self.name 
    else:
      return "~" + self.name

  def negate(self):
    self.neg = self.neg ^ 1

class Formula:
  '''
  A formula requires an array of Variable objects and strings 
  Acceptable strings: (for now) (Perhaps we will replace the array with strings)
    "or"
    "and"
    "->"
    "iff"
  ''' 
  
  def __init__(self, variables, eval=None): 
    self.variables = variables
    self.eval = self.evaluate()

  def __str__(self):
    temp_string = ""
    for i in self.variables: 
      if type(i) != str: 
        temp_string += str(i) + " "
      else:
        temp_string += i + " "
    return temp_string

  def evaluate(self):
    ''' 
    evaluate(self) will determine whether the formula is true or false 
    based on the condition of its constituent variables
    ''' 

    # One point of interest may be in finding the deepest nested bracket
    # from which we use to construct our tree. 

    left_bracket_indices = [i for i, x in enumerate(self.variables) 
                              if x == "("]
    right_bracket_indices = [j for j, y in enumerate(self.variables)
                              if y == ")"]
    length = len(left_bracket_indices)

    for i in range(length): 
      x = left_bracket_indices[length - 1 - i] 
      y = right_bracket_indices[i]
      print(self.variables[x: y + 1])

    # After constructing the tree, we evaluate using certain rules. 
    return 0
    

class TruthTable:
  pass 

class HornFormulas:
  pass 

## We also need a function that converts a string to a proper formula 

A = Variable("A")
B = Variable("B") 
C = Variable("C")

A.negate()

form_a = Formula(["(", "(", A, "or", B, ")", "or", C,  ")"])

print(form_a)



