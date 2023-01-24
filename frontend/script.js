let url = 'http://127.0.0.1:8000/api/v1/userlist/';
let root = document.querySelector('.root');
fetch(url)
.then(res => res.json())
.then(result => {
    for (let i of result) {
        let newElem = document.createElement('div');
        newElem.id = i.user_id;
        newElem.innerHTML = '<p>'+ i.username + '</p>'
        root.insertAdjacentHTML('afterbegin', newElem);
    }
})

