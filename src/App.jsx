import React from 'react';

function App() {
  const [video, setVideo] = React.useState('disgrace.mov');

    React.useEffect(() => {
      const eventSource = new EventSource('/play');

      eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setVideo(data.vid);
      };

      return () => eventSource.close();
    }, []);
    // cannot autoplay unless video is muted as a <video tag limitation
    return <div style={{width: "50vw"}}>
      <video controls autoPlay muted src={`/videos/${video}`}/>
    </div>
}

export default App
