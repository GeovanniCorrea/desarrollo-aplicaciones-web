const formulario = document.getElementById("formProyecto");

const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const mensaje = document.getElementById("mensaje");
const lista = document.getElementById("listaProyectos");
const total = document.getElementById("total");

let contador = 0;

formulario.addEventListener("submit", function(event){

    event.preventDefault();

    if (
        nombre.value.trim() === "" ||
        descripcion.value.trim() === "" ||
        categoria.value === ""
    ) {

        mensaje.innerHTML = `
        <div class="alert alert-danger">
            Todos los campos son obligatorios.
        </div>`;

        return;
    }

    mensaje.innerHTML = `
    <div class="alert alert-success">
        Proyecto registrado correctamente.
    </div>`;

    const card = document.createElement("div");
    card.className = "card mt-3";

    const body = document.createElement("div");
    body.className = "card-body";

    const titulo = document.createElement("h5");
    titulo.className = "card-title";
    titulo.textContent = nombre.value;

    const texto = document.createElement("p");
    texto.className = "card-text";
    texto.innerHTML =
        "<strong>Descripción:</strong> " + descripcion.value +
        "<br><strong>Categoría:</strong> " + categoria.value;

    const boton = document.createElement("button");
    boton.textContent = "Eliminar";
    boton.className = "btn btn-danger btn-sm mt-2";

    boton.addEventListener("click", function () {
        card.remove();
        contador--;
        total.textContent = contador;
    });

    body.appendChild(titulo);
    body.appendChild(texto);
    body.appendChild(boton);

    card.appendChild(body);

    lista.appendChild(card);

    contador++;
    total.textContent = contador;

    formulario.reset();

});