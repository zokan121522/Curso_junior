function Child(props){
    const {msg,person} = props;
    
    return (
        
        <div>
            <h3> Esto es un componente hijo</h3>
            <p>{msg}</p>
            <h3>Persona</h3>
            <p>La persona es {person.sex} - tiene {person.age} años</p>
        </div>

    

    )
}

export default Child