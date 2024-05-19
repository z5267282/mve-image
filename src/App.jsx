import React from 'react';

function App() {
  const item = null;

  if (item !== null) {
    document.title = item;
  }

  return (item === null) ?
    <div>waiting for a video to be played</div>
  :
    // cannot autoplay unless video is muted as a <video tag limitation
    <div style={{width: "50vw"}}>
      <video controls autoPlay muted src={`/videos/${item}`}/>
    </div>
}

export default App
