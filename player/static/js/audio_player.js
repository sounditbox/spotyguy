const socket = new WebSocket('ws://127.0.0.1:8000/ws/audio_player/');

socket.onopen = function(event) {
    console.log('WebSocket connection established.');
    // Send initial message if needed
};

socket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    // Handle incoming WebSocket messages
    // Example: Update audio player UI based on received message
};

socket.onclose = function(event) {
    console.log('WebSocket connection closed.');
    // Handle WebSocket connection closure
};

function playAudio() {
    // document.getElementById("button_play_pause").value = "<img src=''>"
    const message = {
        type: 'play',
        // Additional data if needed (e.g., audio file name, playback timestamp)
    };
    socket.send(JSON.stringify(message));
}
