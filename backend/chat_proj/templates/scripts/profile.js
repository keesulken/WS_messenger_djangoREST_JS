let url = 'http://127.0.0.1:8000/api/v1/profile/';
let root = document.querySelector('.root');
fetch(url)
.then(res => res.json())
.then(result => {
    for (let i in result) {
        let newElem = document.createElement('div');
        newElem.className = i;
        newElem.innerHTML = '<p>'+ result[i] + '</p>'
        document.body.insertBefore(newElem, root);
    }
});
