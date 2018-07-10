$(function () {
    var xmlhttp;

})
function submitVal(e) {
    alert("4");
    var inputVal = $('#search-content').val();
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    if (inputVal == "") 
        e.preventDefault();
    else {
        alert("1");
        xmlhttp.open("GET", "#inputVal", true);
        xmlhttp.send();
    }
}