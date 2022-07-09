$(document).ready(function () {
        //Validacion PERFIL
        $("#inputPassword4").on("input", function () {
            if ($("#inputPassword4").val().length < 8) {
                $("#mensajecontra3").html("La Contraseña tiene que tener 8 caracteres!");
            } else {
                $("#mensajecontra3").html("");
            }
        });
        $("#inputAddress").on("input", function () {
            if ($("#inputAddress").val() == "") {
                $("#mensajedirec").html("La Direccion es obligatoria!");
            } else {
                $("#mensajedirec").html("");
            }
        });
        $("#inputCity").on("input", function () {
            if ($("#inputCity").val() == "") {
                $("#mensajeCiudad").html("La Ciudad es obligatoria!");
            } else {
                $("#mensajeCiudad").html("");
            }
        });
        $("#inputZip").on("input", function () {
            if ($("#inputZip").val() == "") {
                $("#mensajePostal").html("El Codigo Postal es obligatorio!");
            } else {
                $("#mensajePostal").html("");
            }
        });
});
