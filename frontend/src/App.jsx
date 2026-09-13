import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState('Loading...')

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/message')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => {
        console.error(error)
        setMessage('Could not connect to Flask')
      })
  }, [])

  return (
    <div>
      <h1>Geography Game</h1>
      <p>{message}</p>
    </div>
  )
}

export default App