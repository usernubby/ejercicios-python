const formulario = document.getElementById("formulario");

const numeroInput = document.getElementById("numero");

const resultado = document.getElementById("resultado");


formulario.addEventListener("submit", async function(evento) {

    evento.preventDefault();


    const numero = numeroInput.value;


    if (numero === "") {

        resultado.textContent = "Ingrese un número.";

        return;

    }


    const respuesta = await fetch("/tabla", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            numero: numero

        })

    });


    const datos = await respuesta.json();


    resultado.innerHTML = "";


    if (datos.resultados) {

        datos.resultados.forEach(function(fila) {

            const parrafo = document.createElement("p");

            parrafo.textContent =
                `${datos.numero} x ${fila.multiplicador} = ${fila.resultado}`;

            resultado.appendChild(parrafo);

        });

    }

    else {

        resultado.textContent = datos.resultado;

    }

});