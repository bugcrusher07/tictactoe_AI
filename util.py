class Node():
  def _init_(self,dict,action):
    self.dict = dict
    self.action = action

class StackFrontier():
  def _init_(self):
    self.frontier = []

  def add(self,node):
    self.frontier.append(node)

  def empty(self):
    return len(self.frontier) == 0

  def remove(self):
    if self.empty():
      raise Exception (f"bruh the list is empty innit")
    else:
      node = self.frontier[-1]
      self.frontier = self.frontier[:-1]
      return node

class QueueFrontier(StackFrontier):
  def remove(self):
    if self.empty():
      raise Exception (f"bruh the list is empty innit")
    else:
      node = self.frontier[0]
      self.frontier = self.frontier[1:]
      return node
