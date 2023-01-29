import WebSocket, { WebSocketServer } from 'ws';
import {v4 as uuid} from "uuid";


const wss = new WebSocketServer({port: 5000});
const clients = {}
// const messages = [];

wss.on('connection', (ws, req) => {
    const id = uuid();
    clients[id] = ws;
    console.log(`new client ${id}`);

    ws.on('message', (rawMsg) => {
        let msg = JSON.parse(rawMsg);
        console.log(msg);
        if (msg.notification) {
            // messages.push({});
            for (let id in clients) {
                clients[id].send(JSON.stringify({notification:{name: msg.notification.user,
                    status: msg.notification.status,
                }}));
            };
        } else {
            for (let id in clients) {
                clients[id].send(JSON.stringify({content:{name: msg.content.user,
                    text: msg.content.text,
                }}));
            };
        };
    });

    wss.on('close', () => {
        console.log('client closed');
    });
});

