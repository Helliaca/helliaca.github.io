/* When the mobile button is pressed, we add the class "responsive" to #topbar-links-mobile */
function toggleMobileMenu() {
    var x = document.getElementById("topbar-links-mobile");
    if(x.classList.contains("responsive")) {
        x.classList.remove("responsive");
    }
    else {
        x.classList.add("responsive");
    }
}
