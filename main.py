print("¡DEBES DE ESCRIBIR UN AÑOS QUE ABAJO DE 2005 PARA CONTINUAR CON EL PROGRAMA!");
nombre=str(input("Ingrese su nombre"));
año_nac=int(input("Ingrese su año de nacimiento"));

edad=2022-año_nac;

if edad>=18:
 semestre1=int(input("Ingrese las ventas del primer semenestre"));
 semestre2=int(input("Ingrese las ventas del segundo semestre"));
 ventas = int(semestre1+semestre2);
 if semestre1>semestre2:
  mayor="MEJOR SEMESTRE 1RO"
 elif semestre1==semestre2:
  mayor="LOS SEMESTRES SON IGUALES"
 else:
  mayor="MEJOR SEMESTRE 2DO";

 if (ventas <= 100000):
   medalla = "MEDALLA DE BRONCE";
   premio = "UN DIA LIBRE";
 elif (ventas >= 100001 and ventas <= 500000):
   medalla = "MEDALLA DE PLATA";
   premio = "UN DIA LIBRE CON UN BONO DE Q250";
 elif (ventas >= 500001 and ventas <= 1000000):
   medalla = "MEDALLA DE ORO";
   premio = "UN DIA LIBRE CON UN BONO DE Q 500";
 else:
   medalla = "MEDALLA DE DIAMENTE";
   premio = "DOS DIAS LIBRES Y UN BONO DE Q 1000"
 print("VENDEDOR:",nombre);
 print("VENTAS ANUALES:Q",ventas);
 print("MEJOR SEMESTRE:",mayor);
 print("MEDALLA ACREDITADA:",medalla);
 print("PREMIO:",premio)

else:
 print("ADIOS HASTA PRONTO ERES MENOR DE EDAD");