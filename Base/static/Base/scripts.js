let anchoVentana = window.innerWidth

function openNav() {

  if (anchoVentana < 768) {
    document.getElementById("mySidenav").style.width = "100%";
    document.getElementById("openBtn").style.hidden = true;
    document.getElementById("main").style.marginLeft = "12em";

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
}