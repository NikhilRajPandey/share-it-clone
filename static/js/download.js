(function () {
    let navbar = document.getElementsByTagName('nav')[0];
    navbar.className = 'navbar navbar-expand-lg navbar-light';

    let delete_button = document.getElementById('delete_');
    delete_button.href = delete_button.href.concat('unique_code=',unique_code);

    let unique_code_upload = document.getElementById('unique_upload');
    unique_code_upload.value = unique_code;
    unique_code_upload.readOnly = true;
    
    if (no_of_links < 5) {
        document.getElementById('load_more').style.display = 'none';
    }
})();
// I have written like (function()){})(); means that this will call when document will be ready https://stackoverflow.com/questions/9899372/pure-javascript-equivalent-of-jquerys-ready-how-to-call-a-function-when-t
