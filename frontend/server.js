const http = require('http');


const html = `<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <title>Page Title</title>
        <link rel="stylesheet" href="app.css"> 
    </head>
    <body>
        <div class="root">
        </div>
        <script src="app.js"></script>
    </body>
</html>`
let css;
let js = `
let url = 'http://127.0.0.1:8000/api/v1/userlist/';
let root = document.querySelector('.root');
fetch(url)
.then(res => res.json())
.then(result => {
    for (let i of result) {
        let newElem = document.createElement('div');
        newElem.id = i.user_id;
        newElem.innerHTML = '<p>'+ i.username + '</p>'
        document.body.insertBefore(newElem, root);
    }
})
    `


http.createServer((req, res) => {
    switch (req.url) {
        case '/':
            res.writeHead(200, { 'Content-Type': 'text/html' })
            res.end(html);
            break;

        case '/app.css':
            res.writeHead(200, { 'Content-Type': 'text/css' })
            res.end(css);
            break;

        case '/app.js':
            res.writeHead(200, { 'Content-Type': 'text/javascript' })
            res.end(js);
            break;

        default:
            res.writeHead(404, { 'Content-Type': 'text/plain' })
            res.end('404 not found');
            break;
    }
}).listen(3000, () => console.log('running'));

