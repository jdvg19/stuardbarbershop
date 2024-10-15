let anchoVentana = window.innerWidth
//Funcion que realiza cambios al momento de abrir y cerrar el menu
function openNav() {

  if (anchoVentana < 768) {
    document.getElementById("mySidenav").style.width = "100%";
    document.getElementById("openBtn").style.hidden = true;
    document.getElementById("main").style.hidden = true;
  } else {
    document.getElementById("mySidenav").style.width = "12em";
    document.getElementById("openBtn").style.hidden = true;
    document.getElementById("main").style.marginLeft = "12em";
  }

}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("openBtn").style.marginLeft = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("mySidenav").style.paddingLeft = "0";
}
//Funcion para los susbmenus
let dropdown = document.getElementsByClassName("dropdown-btn");
let i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    this.classList.toggle("active");
    let dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

//Funcion de la paginación
$(document).ready(function () {
  $('#data').after('<div id="nav"></div>');
  if (anchoVentana < 768) {
    let rowsShown = 6;
    let rowsTotal = $('#data tbody tr').length;
    let numPages = rowsTotal / rowsShown;
    for (i = 0; i < numPages; i++) {
      let pageNum = i + 1;
      $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
    }
    $('#data tbody tr').hide();
    $('#data tbody tr').slice(0, rowsShown).show();
    $('#nav a:first').addClass('active');
    $('#nav a').bind('click', function () {

      $('#nav a').removeClass('active');
      $(this).addClass('active');
      let currPage = $(this).attr('rel');
      let startItem = currPage * rowsShown;
      let endItem = startItem + rowsShown;
      $('#data tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
        css('display', 'table-row').animate({ opacity: 1 }, 300);
    });
  }
  else{
    let rowsShown = 10;
    let rowsTotal = $('#data tbody tr').length;
    let numPages = rowsTotal / rowsShown;
    for (i = 0; i < numPages; i++) {
      let pageNum = i + 1;
      $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
    }
    $('#data tbody tr').hide();
    $('#data tbody tr').slice(0, rowsShown).show();
    $('#nav a:first').addClass('active');
    $('#nav a').bind('click', function () {

      $('#nav a').removeClass('active');
      $(this).addClass('active');
      let currPage = $(this).attr('rel');
      let startItem = currPage * rowsShown;
      let endItem = startItem + rowsShown;
      $('#data tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
        css('display', 'table-row').animate({ opacity: 1 }, 300);
    });
  }
});

//Funcion para visualizar imagen
const $seleccionArchivos = document.querySelector("#foto"),
  $imagenPrevisualizacion = document.querySelector("#imagenPrevisualizacion");

// Escuchar cuando cambie
$seleccionArchivos.addEventListener("change", () => {
  // Los archivos seleccionados, pueden ser muchos o uno
  const archivos = $seleccionArchivos.files;
  // Si no hay archivos salimos de la función y quitamos la imagen
  if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    return;
  }
  // Ahora tomamos el primer archivo, el cual vamos a previsualizar
  const primerArchivo = archivos[0];
  // Lo convertimos a un objeto de tipo objectURL
  const objectURL = URL.createObjectURL(primerArchivo);
  // Y a la fuente de la imagen le ponemos el objectURL
  $imagenPrevisualizacion.src = objectURL;
});