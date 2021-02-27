# PatronObservador
## El presente trabajo fue realizado por los siguientes alumnos:
- Nicolas Rivarola
- Evelin Herrera
- Tomas Baldi

### Se implementaron 3 patrones observadores que se encuentran en 'observers.py':

1) El observador **"observadorAlta"** reconoce cada vez que hay un registro nuevo en 'tablaarticulos' y hace lo siguiente.
Pasa el registro nuevo a 'tablaaltas', donde se registra Titulo, Descripcion y fecha/hora en que se dio de alta el registro.

2) El observador **"observadorModificar"** reconoce cada vez que se modifica un registro en 'tablaarticulos' y hace lo siguiente.
Pasa el evento a 'tablamodif', donde se registran los siguientes elementos:
  - ID modificado
  - Titulo original
  - Titulo modificado
  - Descripcion original
  - Descripcion modificado
  - Fecha/hora de cuando se modifico el registro.

3) El observador **"observadorEliminar"** reconoce cada vez que se elimina un registro en 'tablaarticulos' y hace lo siguiente.
Pasa un registro a 'tablaelim', donde se registra ID eliminado, Titulo, Descripcion y fecha/hora de cuando se elimino.
