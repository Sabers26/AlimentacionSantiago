-requiere tener permisos de admin Add_cliente

-Listar
-Modificar
-Eliminar

-subir actualizacion sin eliminar

Luis: 1.-el modificar, era usar el mismo html de registro (duplicado) y que cargara los datos, es decir no hay que trabajar con el de django

2.- El eliminar, en la confirmacion, le pasas validaciones de formulario pero si al confirmar no tiene que validar nada, lo unico que tiene es que eliminar el cliente sin mas, la validacion nunca da verdadera asi que puede dar problemas a la hora de eliminar
