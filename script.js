// ==============================
// DATOS DE LOS SERVICIOS
// ==============================

const servicios = [

{
    titulo: "Gestión de Proyectos",
    descripcion: "Control integral y administración de obras civiles.",
    color: "primary"
},

{
    titulo: "Control de Recursos",
    descripcion: "Gestión de materiales, maquinaria y personal.",
    color: "success"
},

{
    titulo: "Reportes Técnicos",
    descripcion: "Generación automática de informes y seguimiento.",
    color: "warning"
}

];

// ==============================
// MOSTRAR SERVICIOS
// ==============================

const listaServicios = document.getElementById("listaServicios");

servicios.forEach(servicio => {

    listaServicios.innerHTML += `

    <div class="col-md-4">

        <div class="card m-3">

            <div class="card-body text-center">

                <h5>${servicio.titulo}</h5>

                <p>${servicio.descripcion}</p>

                <button class="btn btn-${servicio.color}">
                    Ver más
                </button>

            </div>

        </div>

    </div>

    `;

});

// ==============================
// ELEMENTOS DEL FORMULARIO
// ==============================

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

// ==============================
// ARREGLO DE PROYECTOS
// ==============================

let proyectos = [

{
    nombre: "Edificio Central",
    descripcion: "Construcción de edificio administrativo.",
    categoria: "Edificación"
},

{
    nombre: "Puente Norte",
    descripcion: "Construcción de puente vehicular.",
    categoria: "Puentes"
}

];

// ==============================
// VALIDACIONES
// ==============================

function validarNombre(){

    if(nombre.value.trim().length < 3){

        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");

        errorNombre.textContent =
        "Debe ingresar mínimo 3 caracteres.";

        return false;

    }

    nombre.classList.remove("is-invalid");
    nombre.classList.add("is-valid");

    errorNombre.textContent="";

    return true;

}

function validarDescripcion(){

    if(descripcion.value.trim().length < 10){

        descripcion.classList.add("is-invalid");
        descripcion.classList.remove("is-valid");

        errorDescripcion.textContent =
        "La descripción debe tener mínimo 10 caracteres.";

        return false;

    }

    descripcion.classList.remove("is-invalid");
    descripcion.classList.add("is-valid");

    errorDescripcion.textContent="";

    return true;

}

function validarCategoria(){

    if(categoria.value===""){

        categoria.classList.add("is-invalid");
        categoria.classList.remove("is-valid");

        errorCategoria.textContent =
        "Seleccione una categoría.";

        return false;

    }

    categoria.classList.remove("is-invalid");
    categoria.classList.add("is-valid");

    errorCategoria.textContent="";

    return true;

}

// ==============================
// EVENTOS
// ==============================

nombre.addEventListener("input",validarNombre);
descripcion.addEventListener("input",validarDescripcion);
categoria.addEventListener("change",validarCategoria);

nombre.addEventListener("blur",validarNombre);
descripcion.addEventListener("blur",validarDescripcion);
categoria.addEventListener("blur",validarCategoria);

// ==============================
// MOSTRAR PROYECTOS
// ==============================

function mostrarProyectos(){

    lista.innerHTML="";

    if(proyectos.length===0){

        lista.innerHTML=`

        <div class="alert alert-warning">

        No existen proyectos registrados.

        </div>

        `;

    }else{

        proyectos.forEach((proyecto,index)=>{

            lista.innerHTML += `

            <div class="card mt-3">

                <div class="card-body">

                    <h5>${proyecto.nombre}</h5>

                    <p>

                    <strong>Descripción:</strong>

                    ${proyecto.descripcion}

                    <br>

                    <strong>Categoría:</strong>

                    ${proyecto.categoria}

                    </p>

                    <button
                    class="btn btn-danger btn-sm"
                    onclick="eliminarProyecto(${index})">

                    Eliminar

                    </button>

                </div>

            </div>

            `;

        });

    }

    total.textContent = proyectos.length;

}

// ==============================
// ELIMINAR PROYECTO
// ==============================

function eliminarProyecto(indice){

    proyectos.splice(indice,1);

    mostrarProyectos();

}

// ==============================
// REGISTRAR PROYECTO
// ==============================

formulario.addEventListener("submit",function(e){

    e.preventDefault();

    if(

        !validarNombre() ||

        !validarDescripcion() ||

        !validarCategoria()

    ){

        mensaje.innerHTML=`

        <div class="alert alert-danger">

        Corrija los errores antes de registrar.

        </div>

        `;

        return;

    }

    proyectos.push({

        nombre:nombre.value,

        descripcion:descripcion.value,

        categoria:categoria.value

    });

    mostrarProyectos();

    mensaje.innerHTML=`

    <div class="alert alert-success">

    Proyecto registrado correctamente.

    </div>

    `;

    formulario.reset();

    nombre.classList.remove("is-valid","is-invalid");
    descripcion.classList.remove("is-valid","is-invalid");
    categoria.classList.remove("is-valid","is-invalid");

    errorNombre.textContent="";
    errorDescripcion.textContent="";
    errorCategoria.textContent="";

    setTimeout(()=>{

        mensaje.innerHTML="";

    },3000);

});

// ==============================
// INICIAR
// ==============================

mostrarProyectos();