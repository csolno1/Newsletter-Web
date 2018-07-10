$(function () {

})
function submitVal(e) {
    alert("4");
    var inputVal = $('#search-content').val();
    if (inputVal == "") 
        e.preventDefault();
    else {
<<<<<<< HEAD
        alert("1");
        xmlhttp.open("GET", "#inputVal", true);
        xmlhttp.send();
=======
        url = "/search/" + inputVal;
        window.location.href = url
>>>>>>> upstream/master
    }
    return false;
}