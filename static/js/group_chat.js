const group_id = JSON.parse(document.getElementById('json-groupname').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const socket = new WebSocket(
    'wss://' + window.location.host + '/ws/group/' + group_id + '/'
);
socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function (e) {
    console.log("CLOSED");
}

socket.onerror = function (e) {
    console.log("ERROR");
}
socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const d = new Date();
    if (data.username == message_username) {
        document.querySelector('#chat-body').innerHTML += `
                            <tr> 
                                <td>
                                    <p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">
                                        ${data.message}
                                        <small class="p-1 shadow-sm" style="font-size: 0.5em">
                                            ${d.toTimeString().slice(0, 5)}
                                        </small>
                                        <a href="/delete/${data.thread_name}/${data.id}">
                                            <small style="font-size:0.5em;color: #000;">delete</small>
                                        </a>
                                    </p>
                                </td>
                              </tr>`
    } else {
        document.querySelector('#chat-body').innerHTML += `<tr >
        <td>
            <div class="float-left">
                <p class="m-0">${data.username}</p>
                <div class="bg-primary rounded p-2 shadow-sm        text-white text-wrap" style="max-width: 400px; word-break: break-all;">
                    ${data.message}
                    <small class="p-1 shadow-sm" style="font-size: 0.5em">
                        ${d.toTimeString().slice(0, 5)}
                    </small>
                    <a href="/delete/${data.thread_name}/${data.id}">
                        <small style="font-size:0.5em;color: #000;">
                            delete
                        </small>
                    </a>
                </div>
            </div>
        </td>
      </tr>`
    }
    document.querySelector(".message-table-scroll").scrollTo(0, document.querySelector(".message-table-scroll").scrollHeight);
}

document.querySelector('#chat-message-submit').onclick = function (e) {
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username
    }));

    message_input.value = '';
}