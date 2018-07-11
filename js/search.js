$(function () {

})
function submitVal(e) {
    alert("4");
    var inputVal = $('#search-content').val();
    if (inputVal == "") 
        e.preventDefault();
    else {
        url = "/search/" + inputVal;
        window.location.href = url
    }
    return false;
}