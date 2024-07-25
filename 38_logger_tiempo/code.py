import time #libreria para calcular el tiempo de inicio y final

def logger_con_tiempo_de_ejecucion(funcion):
  def wrapper():
  #Imprimir el tiempo de ejecucion
    inicio=time.time()
    print(f"Invocando a la funcion '{funcion.__name__}' ...")

    try:
      resultado=funcion()
    except Exception as e:
      print(f" Se produjo un error en la funcion '{funcion.__name__}': {e}")
      raise
    #Llamar al tiempo final de ejecucion
    fin=time.time()
    print(f"La funcion '{funcion.__name__}' ha tardado {fin-inicio} segundo en ejecutarse ")

    return resultado

  return wrapper


@logger_con_tiempo_de_ejecucion
#Funcion principal que calcula la serie de fibonacci
def mi_funcion():
  fib_series=[0,1]
  for i in range(2,20):
    fib_series.append(fib_series[i-1]+fib_series[i-2])
  return fib_series
print(mi_funcion())