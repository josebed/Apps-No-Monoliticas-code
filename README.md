## Propiedades de los Alpes

### Escenario de calidad trabajado
En esta entrega se trabajó el escenario de calidad #2 de escalabilidad, sobre Actualización de información de compañías


## Ejecutar Aplicación

1. Abra el proyecto con Gitpod
2. Correr docker-compose pulsar para el broker de eventos
```bash
docker-compose --profile pulsar up
```
3. Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/propdalpescoleccioncomp/api run
```
4. Use el método POST para crear compañías:

    POST /companias/compania-comando

   {
    "nombre": "comp1",
    "numero": 12,
    "tipo": "industrial"
  }

   
5. Use el método GET para obtener información de una compañía previamente creada

   GET /companias/compania-consulta/compania-id
