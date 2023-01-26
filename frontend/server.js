const http = require('http');


const html = `<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Page Title</title>
</head>
<body>
    <div class="root">
        <h4 class="error-str"></h4>
        <form class="reg-form" onsubmit="submitForm(event)">
            <p>username <input name="username" type="text"></p>
            <p>password1 <input name="password1" type="text"></p>
            <p>password2 <input name="password2" type="text"></p>
            <p><input type='submit' value="submit">
            <input type="reset" value="reset">
        </form>
        <h3 class="success-str"></h3>
    </div>
    <script>
        function submitForm(event){
            event.preventDefault();
            let username = event.target.elements['username'].value;
            let password1 = event.target.elements['password1'].value;
            let password2 = event.target.elements['password2'].value;
            let errorBlock = document.querySelector('.error-str');
            if (username.length < 4) {
                errorBlock.innerHTML = 'username should contatin at least 4 chars';
            } else if (username.toLowerCase() === username.toUpperCase()) {
                errorBlock.innerHTML = 'username should contain at least one letter';
            } else if (password1.length < 8) {
                errorBlock.innerHTML = 'password should consist of at least 8 chars';
            } else if (password1 != password2) {
                errorBlock.innerHTML = 'passwords dont match';
            } else {
                errorBlock.innerHTML = '';
                let user = {
                    username: username,
                    password: password1,
                    author: 1,
                };
                let url = 'http://127.0.0.1:8000/api/v1/user/'

                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json;charset=utf-8',
                    },
                    body: JSON.stringify(user)
                }).then(res => res.json())
                .then(result => {
                    document.querySelector('.reg-form').style.display = 'none';
                    let success = document.querySelector('.success-str');
                    success.innerHTML = 'Registration complete, log in'
                })
            }
        };
    </script>
</body>
</html>`
let css;
let js;


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

