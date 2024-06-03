import React from 'react';

function App() {
  const [video] = React.useState('disgrace.mov');

    // cannot autoplay unless video is muted as a <video tag limitation
    return <div style={{width: "50vw"}}>
      <video controls autoPlay muted src={`/videos/${video}`}/>
    </div>
}

export default App
