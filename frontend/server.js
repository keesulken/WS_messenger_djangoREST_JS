import WebSocket, { WebSocketServer } from 'ws';
import {v4 as uuid} from "uuid";


const wss = new WebSocketServer({port: 5000});
const clients = {}
const messages = [];

wss.on('connection', (ws, req) => {
    console.log({'req': req});
    const id = uuid();
    clients[id] = ws;
    console.log(`new client ${id}`);

    ws.on('message', (rawMsg) => {
        let msg = JSON.parse(rawMsg);
        console.log(msg);
        console.log(msg.initial)
        // messages.push({name, message});
        // for (let id in clients) {
        //     clients[id].send(JSON.stringify([{name, message}]));
        // }
    });

    wss.on('close', () => {
        console.log('client closed');
    });
});

