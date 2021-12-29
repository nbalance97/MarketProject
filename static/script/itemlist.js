
function deleteButtonEvent(self) {    
    console.log('hello world!');
    let url = "/item/" + self.dataset.id;
    // window.location = "{{ url_for('index') }}";
    fetch(url, {
        method: "DELETE"
    }).then(response => {
        window.location = "/";
    });
}