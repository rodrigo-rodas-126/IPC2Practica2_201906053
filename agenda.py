import os
import webbrowser

class contacto:
  def __init__(self, nombre, apellido, num):
    self.nombre = nombre
    self.apellido = apellido
    self.num = num


class node_de:
  def __init__(self, contacto=None, next=None, previous=None):
    self.contacto = contacto
    self.next = next
    self.previous = previous


class linked_list_de:
  def __init__(self, head=None):
    self.head = head
    self.last = head
    self.size = 0

  def insertar(self, contacto):
    if self.size == 0:
      self.head = node_de(contacto=contacto)
      self.last = self.head
    else:
      new_node = node_de(contacto=contacto, next=self.head)
      self.head.previous = new_node
      self.head = new_node
    self.size += 1

  def imprimir(self):
    if self.head is None:
      return
    node = self.head
    print(node.contacto.nombre, end = " => ")
    while node.next:
      node = node.next
      print(node.contacto.nombre, end=" => ")
    print('\n')

  def eliminar(self, num):
    node = self.head
    while node is not None:
      if node.contacto.num == num:
        if node.previous is not None:
          if node.next:
            node.previous.next = node.next
            node.next.previous = node.previous
          else:
            node.previous.next = None
            self.last = node.previous
        else:
          self.head = node.next
          node.next.previous = self.head
        self.size -= 1
        return True
      else:
        node = node.next
    return False

  def buscar(self, num):
    node = self.head
    while node is not None:
      if node.contacto.num == num:
        return True
      else:
        node = node.next
    return False

  def buscar_retorno(self, num):
    node = self.head
    while node is not None:
      if node.contacto.num == num:
        return node
      else:
        node = node.next
    return None
  
  def grafo(self):
    contador = 0
    node = self.head
    with open('grafo.dot', 'w') as re:
      re.write('digraph G {' + '\n')
      re.write('  Nodo'+str(contador)+' [label=" Nombre: '+str(node.contacto.nombre)+'\n Apellido: '+str(node.contacto.apellido)+'\n Numero: '+str(node.contacto.num)+'", color="pink", shape="square"]' + '\n')
      while node.next:
        contador += 1
        node = node.next
        re.write('  Nodo'+str(contador)+' [label=" Nombre: '+str(node.contacto.nombre)+'\n Apellido: '+str(node.contacto.apellido)+'\n Numero: '+str(node.contacto.num)+'", color="pink", shape="square"]' + '\n')
        re.write('  Nodo'+str(contador - 1) + ' -> ' + 'Nodo'+ str(contador) + '\n')
        re.write('  Nodo'+str(contador) + ' -> ' + 'Nodo'+ str(contador - 1) + '\n')
      re.write('}')
      re.close
    os.system('dot -T png grafo.dot -o grafo.png')
    webbrowser.open('grafo.png')

Agenda = linked_list_de()
while True:
  print('\n')
  print('--------------------')
  print('1. Ingresar Contacto')
  print('2. Buscar Contacto')
  print('3. Visualizar Agenda')
  op = input('>>  ')

  if op == "1":
    print('Ingrese Nombre: ')
    nombre = input('>>  ')
    print('Ingrese Apellido: ')
    apellido = input('>>  ')
    print('Ingrese Numero Telefonico: ')
    telefono = input('>>  ')
    if Agenda.buscar(telefono):
      print('Contacto ya Existe\n')
    else:
      Agenda.insertar(contacto(nombre, apellido, telefono))
      print('Contacto Guardado\n')

  elif op == "2":
    print('Ingrese Numero a Buscar: ')
    num_b = input('>>  ')
    nodo_aux = Agenda.buscar_retorno(num_b)
    if nodo_aux is not None:
      print('Nombre de Contacto:')
      print('>>' + str(nodo_aux.contacto.nombre))
      print('Apellido de Contacto:')
      print('>>' + str(nodo_aux.contacto.apellido))
      print('Numero de Contacto:')
      print('>>' + str(nodo_aux.contacto.num))
    else:
      print('El numero del contacto no existe, ¿Desea agregarlo? (S/N)')
      val = input('>>  ')
      if val == "S":
        print('Ingrese Nombre: ')
        nombre = input('>>  ')
        print('\nIngrese Apellido: ')
        apellido = input('>>  ')
        Agenda.insertar(contacto(nombre, apellido, num_b))
        print('Contacto Guardado\n')
      elif val == "N":
        continue

  elif op == "3":
    #Agenda.imprimir()
    Agenda.grafo()

  else:
    continue 
