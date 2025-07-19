export default function SaludoCondicional ({esAdmin}){

    return(
        <div>
            {esAdmin ?
             (<h2>Admin: acceso total</h2>) 
                : 
             (<h2>Usuiario: acceso limitado</h2>)
            }
        </div>
    );

}

