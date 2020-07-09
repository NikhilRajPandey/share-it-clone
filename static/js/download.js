(function () {
    let navbar = document.getElementsByTagName('nav')[0];
    navbar.className = 'navbar navbar-expand-lg navbar-light';

    let unique_code_upload = document.getElementById('unique_upload');
    let current_href = window.location.href;
    let unique_code = current_href.slice(current_href.search('unique_code')+12,);
    unique_code_upload.value = unique_code;
    unique_code_upload.disabled = 'true';
    
    if (no_of_links < 5) {
        document.getElementById('load_more').style.display = 'none';
    }
})();
// I have written like (function()){})(); means that this will call when document will be ready https://stackoverflow.com/questions/9899372/pure-javascript-equivalent-of-jquerys-ready-how-to-call-a-function-when-t
let loaded = 0; // Means Not loaded and 1 means loaded
function load_more() {
    let your_uploads = document.getElementById('your-uploads');
    let load_more = document.getElementById('load_more');
    if (loaded == 0) {
        your_uploads.innerHTML += "{% for file in list_of_files[5:] %}<h3 class='your-upload-file'><a href='{{url_for('static',filename='Downloads/%s'%file)}}'>{{file}}</a></h3>{% endfor %}";
        load_more.innerText = "Show Less";
        loaded = 1;
    }
    else {
        let dom_of_your_uploads = your_uploads.getElementsByClassName("your-upload-file"); // Sorry for my bad variable naming
        let last_index = dom_of_your_uploads.length - 1;
        while (dom_of_your_uploads.length > 5) { // Run the loop until this var don't get empty
            let file_element = dom_of_your_uploads[last_index];
            last_index = last_index - 1;
            file_element.remove();
        }
        load_more.innerText = "Show More";
        loaded = 0;
    }
}