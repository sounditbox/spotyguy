//let audioDataBuffer = '';  // Buffer to store received audio data
//
//const socket = new WebSocket('ws://127.0.0.1:8000/ws/audio_player/');
//
//socket.onopen = function(event) {
//    console.log('WebSocket connection established.');
//    // Send initial message if needed
//};
//
//socket.onmessage = function(event) {
//    const chunk = event.data;  // Received base64-encoded chunk
//    audioDataBuffer += chunk;  // Append chunk to buffer
//    // Example: Check if complete audio data is received
//    console.log(chunk);
//    if (completeAudioDataReceived()) {
//        console.log(atob(chunk));
//        console.log('Complete Audio Data Received.');
//
//        // Process the complete audio data (e.g., play the audio)
//        const audioElement = new Audio();
//        audioElement.src = 'data:audio/mp3;base64,' + audioDataBuffer;
//        audioElement.play();
//    }
//};
//
//
//socket.onclose = function(event) {
//    console.log('WebSocket connection closed.');
//    // Handle WebSocket connection closure
//};
//
//function playAudio() {
//    // document.getElementById("button_play_pause").value = "<img src=''>"
//    const message = {
//        type: 'play',
//        // Additional data if needed (e.g., audio file name, playback timestamp)
//    };
//    socket.send(JSON.stringify(message));
//}
//
//
//function completeAudioDataReceived() {
//    // Logic to determine if all audio data is received
//    // Example: Check if buffer contains end-of-audio marker
//    return audioDataBuffer.includes('END_OF_AUDIO_MARKER');
//}

const socket = new WebSocket('ws://127.0.0.1:8000/ws/audio_player/');
        let audioDataBuffer = '';

        socket.onopen = function(event) {
            console.log('WebSocket connection established.');
            document.getElementById('startButton').onclick = function() {
                const message = JSON.stringify({command: 'start_audio_transfer'});
                socket.send(message);
            };
        };

        socket.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.error) {
                console.error('Error:', data.error);
                return;
            }
            if (data.end) {
                console.log('data received');
                console.log(audioDataBuffer);

                const audioElement = document.getElementById('audioPlayer');
                audioElement.src = 'data:audio/mp3;base64,' + audioDataBuffer;
                audioElement.play();
                audioDataBuffer = '';  // Reset buffer after playing
            } else if (data.chunk) {
                audioDataBuffer += data.chunk;
            }
        };

        socket.onerror = function(event) {
            console.error('WebSocket error observed:', event);
        };

        socket.onclose = function(event) {
            console.log('WebSocket connection closed.');
        };