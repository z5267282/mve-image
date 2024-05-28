import React from 'react';

function App() {
    // cannot autoplay unless video is muted as a <video tag limitation
    return <div style={{width: "50vw"}}>
      <video controls autoPlay muted src={`/videos/disgrace.mov`}/>
    </div>
}

export default App
