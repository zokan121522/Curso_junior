import React from 'react'

import Child from './components/Child'

function App() {

  const text = "Mensaje desde el componente padre"
  const person = {
    sex : "hombre",
    age : 41
  }
  return (
    <div>
      <h2>Componente hijo</h2>
      <Child msg ={text} person = {person} ></Child>
    </div>
  )
}

export default App