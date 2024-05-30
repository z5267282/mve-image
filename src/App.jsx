import React from 'react';
import io from 'socket.io-client';

const socket = io('ws://localhost:6000');

function App() {
  const [video, setVideo] = React.useState('disgrace.mov');

    useEffect(() => {
      socket.on('connect', () => {
          console.log('Connected to WebSocket');
      });

      socket.on('message', (vid) => {
          setVideo(vid);
      });

      return () => {
          socket.disconnect();
      };
    }, []);

    // cannot autoplay unless video is muted as a <video tag limitation
    return <div style={{width: "50vw"}}>
      <video controls autoPlay muted src={`/videos/${video}`}/>
    </div>
}

export default App
