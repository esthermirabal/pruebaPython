document.addEventListener('DOMContentLoaded',() => {
    const modeloList = document.getElementById("persona-list")
})
function cargarDatos(){
    fetch("/prueba", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then(response => response.json())
    .then(data => {
        modeloList.innerHTML = "";

        data.forEach(prueba =>{
            const modeloDiv = document.createElement("div");
            <strong>Nombre:</strong> ${prueba.nombre} <br>
            <strong>Modelo:</strong> ${prueba.modelo} <br>
            <strong>Precio:</strong> ${prueba.precio} <br>
            modeloList.appendChild(modeloDiv);
        });
    });
}