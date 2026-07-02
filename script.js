const formulario = document.getElementById("formProyecto");

const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const mensaje = document.getElementById("mensaje");
const lista = document.getElementById("listaProyectos");
const total = document.getElementById("total");

const errorNombre = document.getElementById("errorNombre");
const errorDescripcion = document.getElementById("errorDescripcion");
const errorCategoria = document.getElementById("errorCategoria");

let contador = 0;

/* =========================
   VALIDACIONES
========================= */

function validarNombre() {

    if (nombre.value.trim().length < 3) {

        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");

        errorNombre.textContent = "Debe ingresar mínimo 3 caracteres.";

        return false;
    }

    nombre.classList.remove("is-invalid");
    nombre.classList.add("is-valid");

    errorNombre.textContent = "";

    return true;
}

function validarDescripcion() {

    if (descripcion.value.trim().length < 10) {

        descripcion.classList.add("is-invalid");
        descripcion.classList.remove("is-valid");

        errorDescripcion.textContent =
        "La descripción debe tener al menos 10 caracteres.";

        return false;
    }

    descripcion.classList.remove("is-invalid");
    descripcion.classList.add("is-valid");

    errorDescripcion.textContent = "";

    return true;
}

function validarCategoria() {

    if (categoria.value === "") {

        categoria.classList.add("is-invalid");
        categoria.classList.remove("is-valid");

        errorCategoria.textContent =
        "Seleccione una categoría.";

        return false;
    }

    categoria.classList.remove("is-invalid");
    categoria.classList.add("is-valid");

    errorCategoria.textContent = "";

    return true;
}

/* =========================
   EVENTOS EN TIEMPO REAL
========================= */

nombre.addEventListener("input", validarNombre);
descripcion.addEventListener("input", validarDescripcion);
categoria.addEventListener("change", validarCategoria);

nombre.addEventListener("blur", validarNombre);
descripcion.addEventListener("blur", validarDescripcion);
categoria.addEventListener("blur", validarCategoria);

/* =========================
   SUBMIT
========================= */

formulario.addEventListener("submit", function(event){

    event.preventDefault();

    if (
        !validarNombre() ||
        !validarDescripcion() ||
        !validarCategoria()
    ) {

        mensaje.innerHTML = `
        <div class="alert alert-danger">
            Corrija los errores antes de registrar.
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

        if (contador > 0) {
            contador--;
        }

        total.textContent = contador;
    });

    body.appendChild(titulo);
    body.appendChild(texto);
    body.appendChild(boton);

    card.appendChild(body);

    lista.appendChild(card);

   card.remove();

contador = lista.children.length;
total.textContent = contador;

    formulario.reset();

    nombre.classList.remove("is-valid", "is-invalid");
    descripcion.classList.remove("is-valid", "is-invalid");
    categoria.classList.remove("is-valid", "is-invalid");

    errorNombre.textContent = "";
    errorDescripcion.textContent = "";
    errorCategoria.textContent = "";

    mensaje.innerHTML = "";
});