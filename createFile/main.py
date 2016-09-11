#!/usr/bin/env python
# -*- condig: utf-8 -*-

import getopt 
import sys
from random import shuffle

def createFile():
   try:
      #Recibe argumentos desde bash en un argumento
      opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
   except getopt.GetoptError as err:
      print str(err)
      usage()
      sys.exit(2)

   if len(args) != 0:
      arch = open(args[0]+'.txt','w')
      arch.close()
      #args[1] Tipo archivo args[2] Numero elementos
      generateFile(args[0]+'.txt',int(args[1]),int(args[2]))
   else:
      print ("(>**)> put parameters\n1- Name of file\n2- Type of file:\n\t* (1) Ordered\n\t* (2) Reverse\n\t* (3) Random\n3- # of items per file ")
      
   
def generateFile(file,type,elements):
   #i = 0
   arch = open(file,'w')
   arch.write(str(elements) + '\n')
   if type == 1:
      #Ordenado
      lista = range(elements)
      for i in lista:
         arch.write(str(i) + ' ')
   elif type == 2:
      #Inverso
      lista = range(elements,0,-1)
      for i in lista:
         arch.write(str(i) + ' ')
   elif type == 3:
      #Aleatorio
      lista = range(elements)
      shuffle(lista)
      for i in lista:
         arch.write(str(i) + '\n')
   else:
      print ("Error in file: Python")
   arch.close()
   
   
createFile()
