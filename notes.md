# Notas útiles para el desarrollo del proyecto.

# Revisión 1
- Quitar el usuario, no se especifica en el proyecto, agregarlo es sobre diseño
- Cada servidor tiene sus servicios
  - Almacén de servidores
  - Almacén de servicios
- Proteger más los procesos
  - Detallar la tabla de amenazas
  - Alguién que no se haya autenticado, que no pueda hacer peticiones
    - Peticiones autenticadas con token
- Protección de almacenes
  - Cifrado
  - Hashing está bien
  - Agregar algunas relacionadas con privilegios, análisis y limitaciones
- Los flujos no son propensos al spofing, quitar validación de tokens

## Explicación del profe
- agregar entidad externa que representa un sistema que realiza las operaciones del lado de cada servidor
- administrador -> levantar (flutter) -> servidor (flask)
- agregar capa de autenticación de peticiones críticas
  - JWT
  - SSH

# Seguridad en inicios de sesión
- Limitar intentos

## Políticas
- Tienes **n** cantidad de intentos inmediatos
- Si agotas los intentos de sebe esperar **m** cantidad de segundos
- Mientras sigas intentando sin descanso, sigues bloqueado
- Cada **m** cantidad de segundos se reinician los intentos

### Información necesaria
- IP del cliente
- Conteno de intentos, durante ventana de tiempo **m**
- No ha alcanzado el valor de **n**

### Solución
- Manejar el contador desde la base de datos
- ip_addr = request.remote_addr

---

# Hashes

**Recomendación**
Usar **sha256** como mínimo.
El hash **sha512** es una cadena más larga y tiene mayor protección ante preimagenes y colisiones.

---

hash(b) = XXXXX

El dominio es infinito, **b** puede tomar cualquier valor, pero el hash siempre será de un número definido de caracteres.

En el caso: h(b) = 35

Los posibles valores de **b** son un conjunto infinito.

**Por ejemplo:**
```python
par(num)

# retorna 0 o 1
```
El tamaño de hash de la función `par` es de longitud 1.

## Preimagen
Para la preimagen necesitamos un hash, siguiendo el ejempo de h(b)=35, sería 35.

Son todos los valores de entrada que generan la salida que conocemos, es decir, todos posibles valores de **b** que generen 35.

**Por ejemplo:**
```python
par(2)
# 0
par(222222)
# 0
```
La preimagen de 0 serían todos los números pares.

## Resistencia de preimagen
**Algoritmo de hash seguro.**
Debe ser casi imposible encontrar un elemento de la preimagen del hash.

## Resistencia a colisiones
Aunque la preimagen es infinita, es posible que no haya colisiones.
El hash **md5** es débil ante colisiones.


# Uso de CAPTCHAS
- reCaptcha de Google


# Ámbito
- Alcance de identificadores.
  - Cualquier cosa que un programador nombra, como variables, clases, o funciones.

### Introducción
- El ámbito se refiere a la sección de código donde algo nombrado mediante un identificador vive.
- El ámbito es diferente al tiempo de vida del objeto.
- Es diferente al tiempo de vida de un objeto.
- Establece acceso y tiempo de vida solo de identificadores.

```{python}
l = [1,2,3]
def sumar(lista):
    return sum(lista)
```

Cuando termina la llamada de **sumar**, **l** sigue en memoria.
Y se puede referenciar a la misma memoria.

> WARNING
> Puede causar efectos colaterales.

### Niveles de Ámbito
- Global
- Objeto
- Método
- Bloque

#### Global
- Una forma de crear variables globales
- El uso de variables globales es una mala práctica de programación, se generan efectos colaterales.

```{python}
def f():
    var = 1
    def g():
        v = var + 2
    # no es valido
    # v6 = v2 + 1

    # sí es válido, g() está definido dentro de f()
    v6 = g() + var
```

#### Objeto
- Son variables que viven en el ámbito del objeto una vez creado.
- Definimos la clase, pero no viven en ee ámbito.
- Existen apuntadores al propio objeto, como **this.** o **self.()**.
- Las propiedades y métodos se definen directamente dentro de una clase.
- Cuando el objeto desaparece, su ámbito muere.
- Comienza cuando se abre el bloque de la clase.

```{java}
public class Punto {
    private int x; // clase
    private int y;
    public Punto(int x ,int y){
        this.x = x; // apuntador al propio objeto
        this.y = y;
    }
    public sumarPuntos(Punto p){
        // x del propio objeto = x de p
        this.x = p.x;
        this.y = p.y;
    }
}
```

```{java}
public class Punto {
    private Integer x; // clase
    private Integer y;
    public Punto(int x ,int y){
        this.x = x; // apuntador al propio objeto
        this.y = y;
    }
    public sumarPuntos(Punto p){
        // x del propio objeto = x de p
        this.x = p.x;
        this.y = p.y;
    }
}


Punto punto1 = new Punto(1, 2);
Integer aux = punto1.x;
```

#### Método
- Una vez termina el método, todos los identificadores dentro de él también desaparecen.
- Puede ser que los objetos referenciados no desaparezcan porque están siendo referenciados en un ámbito vivo.
- Comienza cuando se abre el bloque del método o función.

#### Bloque
- Surge cuando se utiliza alguna sentencia de control, cini **if**, **while**, **for**.
- **Python** no tiene ámbito de bloque.

```{java}
public class Ejemplo{
    public static void main(String[] args){
        if (true) {
            int var = 33;
        } // aquí termina el ámbito
        System.out.println(var); // error: var no está definido, porque el ámbito termina al cerrar el bloque
    }
}
```

## Ámbito (continuación)
- Si están en el mismo ámbito, evitar la creación de identificadores con el mismo nombre.
- Al hacer referencia a un identificador, si no se encuentra en ese ámbito, se buscará en el siguiente nivel de ámbito.

## Ámbito - Mejores Prácticas
- Definir los identificadores en el ámbito más cercano a donde será utilizado.
  - Definirlo justo antes de usarlo.
- **Nunca** usar variables globales, a menos que sean constantes.
- Los métodos que modifican el estado de un atributo deben declarar de forma directa esta intención en el ámbito a nivel clase/objeto.
- Utilizar referencias en el ámbito conel tiempo de vida más corto.

## Código Amigable a la Recolección de Basura
- Se refiere a la liberación automática de memoria que ya no es utilizada por el programa.
- Está automatizado en distintas plataformas, **Java** y **Python** lo hacen con su máquina virtual.
- En lenguajes de bajo nivel se debe hacer manual, como en **C** o **C++**.
- Es un proceso especial, que analiza memoria, y cuando detecta que un bloque de memoria no es referenciado por alguna referencia.
- Hacerlo manualmente aumenta la eficiencia, pero se puede dejar automáticamente. 
- Siempre que nu ámbito termina, todas las referencias creadas en él, mueren.
  - En consecuencia, mucha memoria se puede liberar.
- Mientras más corto sea el tiempo de vida del ámbito, más rápido se libera memoria.
- En ocaciones la memoria ya no se necesita, pero quedó referenciada en un ámbito que sigue vivo.


## Memoria de un Proceso
- Stack: lo gestiona el SO
- Heap: lo gestiona el programador

# Manejo de Entradas
- Son el punto más crítico de seguridad que le corresponde a un programador.
- Se pueden explotar vulnerabilidades de inyección, romper por fuerza bruta claves de acceso, realizar fuzzing para localizar posibles errors en el manejo de memoria.
- En temas web, un atacante podría desactivar JS o manipular el html.

> IMPORTANT
> Siempre validar entradas del lado del cliente y del servidor.

### Validación de cadenas
- Revisar que la cadena se adapte a una longitud mínima y máxima para mitigar posibles ataques de desbordamiento de buffer.
- Establecer el mismo máximo en el input del usuario y en el servidor de bases de datos.
- Evitar caracteres especiales como [ ; / " - ? ].
  - Si son necesarios, se debe sanitizar la entrada.
- No utilizar cadenas directamente en el código.

```{java}
def validar(user, pass){
    query = "'select * from usuarios where user=" + user + " and password=" + pass + "'"
}
```

### Validación de números
- Revisar que los valores sean números del tipo necesario antes de procesarlos.


