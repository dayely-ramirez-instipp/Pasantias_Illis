function validarFormulario() {
  const cedula = document.getElementById('cedula').value.trim();
  const celular = document.getElementById('celular').value.trim();
  const correo = document.getElementById('correo').value.trim();
  const fecha = document.getElementById('fecha').value.trim();
  const soloNumeros = /^\d+$/;
  const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!soloNumeros.test(cedula)) {
    alert("La cédula debe contener solo números.");
    return false;
  }
  if (!soloNumeros.test(celular)) {
    alert("El celular debe contener solo números.");
    return false;
  }
  if (!correoValido.test(correo)) {
    alert("Correo electrónico no válido.");
    return false;
  }
  if (!fecha) {
    alert("Debe ingresar la fecha de nacimiento.");
    return false;
  }
  const edad = calcularEdad(new Date(fecha));
  if (edad < 18) {
    alert("Debe ser mayor de edad para registrarse. Edad: " + edad);
    return edad;
  }
  return true;
}
function calcularEdad(fechaNacimiento) {
  const hoy = new Date();
  let edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
  const mes = hoy.getMonth() - fechaNacimiento.getMonth();
  if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
    edad--;
  }
  return edad;
}
