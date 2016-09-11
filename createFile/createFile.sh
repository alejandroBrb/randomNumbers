#!/bin/bash
# Primer parametro-Numero de ciclos (archivos)
# Segundo parametro-Tipo de archivo que se generara
# Tercer parametro-Numero de elementos por archivo
INDICE=0
if [[ $1 ]] && [[ $2 ]] && [[ $3 ]]; then
   while [ $INDICE -lt $1 ]
   do
      if [[ $2 -eq 1 ]]; then
         NOMBRE="O-$3-$INDICE"
      fi
      if [[ $2 -eq 2 ]]; then
         NOMBRE="I-$3-$INDICE"
      fi
      if [[ $2 -eq 3 ]]; then
         NOMBRE="A-$3-$INDICE"
      fi
      #Nombre/Tipo/Numero de elementos
      #Truena cuando no pasas numeros --Validar--
      #Manda a llamar archivo en python con el parametro de python
      python main.py "$NOMBRE" $2 $3
      let INDICE=INDICE+1
   done
   echo "Well done! File create."
else
   echo -e "(>**)> put parameters\n1- # of File's\n2- Type of file:\n\t* (1) Ordered\n\t* (2) Reverse\n\t* (3) Random\n3- # of items per file "
fi
