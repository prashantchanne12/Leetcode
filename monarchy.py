class Person:
  def __init__(self, name):
    self.name = name
    self.is_alive = True
    self.children = []


class Monarchy:
  
  def __init__(self, king):
    self.king = Person(king)
    self.persons = {
        self.king.name : self.king
    }

  def birth(self, child, parent):
    
    new_child = Person(child)
    self.persons[child] = new_child

    parent = self.persons[parent]
    parent.children.append(new_child)
    


  def death(self, name):
    person = self.persons[name]
    person.is_alive = False

  def get_order_of_succession(self):
    order = []

    self.dfs(self.king, order)

    return order

  def dfs(self, person, order):
    
    if person.is_alive:
      order.append(person.name)

    for children in person.children:
      self.dfs(children, order)



m = Monarchy('Jake')

m.birth('Catherine', 'Jake')
m.birth('Tom', 'Jake')
m.birth('Celine', 'Jake')

m.birth('Jane', 'Catherine')
m.birth('Mark', 'Catherine')
m.birth('Farah', 'Jane')

m.birth('Peter', 'Celine')


print(m.get_order_of_succession())



  



